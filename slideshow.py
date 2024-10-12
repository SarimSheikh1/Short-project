import streamlit as st
from PIL import Image
from time import sleep
import base64

# Title of the app
st.title("Image Slideshow and Video Player")

# Section to upload images
st.header("Image Slideshow")

# Image uploader for user to upload multiple images
uploaded_files = st.file_uploader("Upload Images", type=['jpg', 'png', 'jpeg'], accept_multiple_files=True)

image_size = (1080, 1080)

# Process uploaded images
if uploaded_files:
    images = [Image.open(uploaded_file).resize(image_size) for uploaded_file in uploaded_files]
    
    # Button to start slideshow
    if st.button('Start Slideshow'):
        # Create a placeholder to hold the image that will change
        image_placeholder = st.empty()
        
        for image in images:
            # Display image (replacing the previous one)
            image_placeholder.image(image)
            # Pause for 5 seconds between images
            sleep(5)
else:
    st.write("Please upload some images to start the slideshow.")

# Section to upload and display videos
st.header("Video Player")

# Video uploader for user to upload multiple videos
uploaded_videos = st.file_uploader("Upload Videos (max 5)", type=['mp4', 'mov', 'avi'], accept_multiple_files=True)

# Limit the number of videos to 5
if uploaded_videos and len(uploaded_videos) <= 5:
    for uploaded_video in uploaded_videos:
        # Read the video file and encode it in Base64
        video_bytes = uploaded_video.read()
        video_base64 = base64.b64encode(video_bytes).decode('utf-8')

        # Display the video using HTML to set dimensions
        st.markdown(
            f'<video controls width="480" height="850" style="object-fit: cover;">'
            f'<source src="data:video/mp4;base64,{video_base64}" type="video/mp4">'
            f'Your browser does not support the video tag.'
            f'</video>', 
            unsafe_allow_html=True
        )
else:
    st.write("Please upload up to 5 videos to play.")
