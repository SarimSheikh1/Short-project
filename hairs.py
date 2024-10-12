import streamlit as st
import cv2
import numpy as np
from PIL import Image
import mediapipe as mp
import logging

logging.getLogger('tensorflow').setLevel(logging.ERROR)
logging.getLogger('google.protobuf').setLevel(logging.ERROR)


# Initialize mediapipe face detection
mp_face_mesh = mp.solutions.face_mesh
mp_draw = mp.solutions.drawing_utils

# Function to detect face landmarks using Mediapipe
def detect_face_landmarks(image):
    with mp_face_mesh.FaceMesh(static_image_mode=True) as face_mesh:
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_image)

        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0]
            return landmarks
        else:
            return None

# Updated function to determine the face shape based on landmarks
def determine_face_shape(landmarks):
    chin = landmarks.landmark[152]  # Chin landmark index
    left_cheek = landmarks.landmark[234]  # Left cheek landmark index
    right_cheek = landmarks.landmark[454]  # Right cheek landmark index
    forehead = landmarks.landmark[10]  # Forehead landmark index

    # Calculate distances to determine face shape
    chin_height = chin.y
    cheek_width = abs(left_cheek.x - right_cheek.x)
    forehead_width = forehead.x  # Rough estimate based on x coordinate

    if chin_height < 0.5 and cheek_width > forehead_width:
        return "Round"
    elif chin_height < 0.5 and cheek_width < forehead_width:
        return "Square"
    elif chin_height > 0.5 and cheek_width > forehead_width:
        return "Oval"
    else:
        return "Other"

# Function to overlay hairstyle on the detected face and add shapes
def overlay_hair_and_shapes(face_image, hair_image_path, landmarks):
    hair = Image.open(hair_image_path).convert("RGBA")

    # Calculate the position and size for the hairstyle based on landmarks
    nose_tip = (int(landmarks.landmark[168].x * face_image.size[0]),
                int(landmarks.landmark[168].y * face_image.size[1]))
    left_eye = (int(landmarks.landmark[263].x * face_image.size[0]),
                int(landmarks.landmark[263].y * face_image.size[1]))
    right_eye = (int(landmarks.landmark[373].x * face_image.size[0]),
                 int(landmarks.landmark[373].y * face_image.size[1]))

    hair_width = right_eye[0] - left_eye[0]
    hair_height = int(hair.size[1] * (hair_width / hair.size[0]))

    hair = hair.resize((hair_width, hair_height), Image.ANTIALIAS)

    y_offset = nose_tip[1] - hair_height // 2

    face_image.paste(hair, (left_eye[0], y_offset), hair)

    # Convert PIL image to OpenCV format for drawing shapes
    face_image_cv = cv2.cvtColor(np.array(face_image), cv2.COLOR_RGBA2BGR)

    # Draw shapes for face shape
    if determine_face_shape(landmarks) == "Round":
        cv2.circle(face_image_cv, (nose_tip[0], nose_tip[1]), 80, (0, 255, 0), 2)  # Green circle for round face
    elif determine_face_shape(landmarks) == "Square":
        cv2.rectangle(face_image_cv, (left_eye[0], left_eye[1]), (right_eye[0], right_eye[1]), (255, 0, 0), 2)  # Blue rectangle for square face
    elif determine_face_shape(landmarks) == "Oval":
        cv2.ellipse(face_image_cv, (nose_tip[0], nose_tip[1]), (80, 120), 0, 0, 360, (0, 0, 255), 2)  # Red ellipse for oval face

    return Image.fromarray(cv2.cvtColor(face_image_cv, cv2.COLOR_BGR2RGB))

# Streamlit UI
st.title("Virtual Hairstyle App")

option = st.radio("How would you like to provide your image?", ("Take a Selfie", "Upload a Face Image"))

if option == "Take a Selfie":
    selfie = st.camera_input("Take a selfie")

    if selfie:
        image = Image.open(selfie)
        image = np.array(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        st.image(image, caption='Selfie Taken', use_column_width=True)

        landmarks = detect_face_landmarks(image)

        if landmarks is not None:
            st.write("Face Detected!")
            face_shape = determine_face_shape(landmarks)
            st.write(f"Detected Face Shape: {face_shape}")

            uploaded_hair_file = st.file_uploader("Upload a hairstyle image (JPG, JPEG, PNG, etc.)", type=["jpg", "jpeg", "png", "bmp", "gif"])

            if uploaded_hair_file is not None:
                hair_image = Image.open(uploaded_hair_file).convert("RGBA")
                st.image(hair_image, caption='Uploaded Hairstyle Image', use_column_width=True)

                pil_image = Image.fromarray(image)
                pil_image = overlay_hair_and_shapes(pil_image, uploaded_hair_file, landmarks)

                st.image(pil_image, caption='With Hairstyle and Shape!', use_column_width=True)
            else:
                st.write("Please upload a hairstyle image to overlay.")
        else:
            st.write("No face detected. Try another image.")
else:
    uploaded_face_file = st.file_uploader("Choose a face image...", type=["jpg", "jpeg", "png"])

    if uploaded_face_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_face_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        st.image(image, caption='Uploaded Face Image.', use_column_width=True)

        landmarks = detect_face_landmarks(image)

        if landmarks is not None:
            st.write("Face Detected!")
            face_shape = determine_face_shape(landmarks)
            st.write(f"Detected Face Shape: {face_shape}")

            uploaded_hair_file = st.file_uploader("Upload a hairstyle image (JPG, JPEG, PNG, etc.)", type=["jpg", "jpeg", "png", "bmp", "gif"])

            if uploaded_hair_file is not None:
                hair_image = Image.open(uploaded_hair_file).convert("RGBA")
                st.image(hair_image, caption='Uploaded Hairstyle Image', use_column_width=True)

                pil_image = Image.fromarray(image)
                pil_image = overlay_hair_and_shapes(pil_image, uploaded_hair_file, landmarks)

                st.image(pil_image, caption='With Hairstyle and Shape!', use_column_width=True)
            else:
                st.write("Please upload a hairstyle image to overlay.")
        else:
            st.write("No face detected. Try another image.")
