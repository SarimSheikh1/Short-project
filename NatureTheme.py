import streamlit as st 
from PIL import Image
import os

# Set page configuration
st.set_page_config(page_title="Nature Theme", layout="centered")

# Sidebar for theme options
with st.sidebar:
    st.title("Nature Theme Options")
    st.write("Select your Nature Theme settings:")

    # Option to toggle between theme colors
    theme_color = st.selectbox("Choose your theme color", ['Light Mode', 'Dark Mode', 'Black', 'Yellow', 'Red'])

    # Option to choose nature background image from different global locations
    bg_option = st.selectbox("Select a Nature Background", ["Forest", "Ocean", "Mountains", "Desert"])

    # Option to change font size for global accessibility
    font_size = st.slider("Adjust Font Size", 12, 24, 16)

# Define color schemes based on user selection
if theme_color == 'Light Mode':
    bg_color = "#E6F2E6"  # Light green
    text_color = "#2E4600"  # Deep earthy green
    button_color = "#9BBF30"  # Leafy green
elif theme_color == 'Dark Mode':
    bg_color = "#2E4600"  # Dark forest green
    text_color = "#F4EBC3"  # Light beige
    button_color = "#617A55"  # Earthy brown
elif theme_color == 'Black':
    bg_color = "#000000"  # Black background
    text_color = "#FFFFFF"  # White text
    button_color = "#FF0000"  # Red button
elif theme_color == 'Yellow':
    bg_color = "#FFFF00"  # Yellow background
    text_color = "#000000"  # Black text
    button_color = "#FFCC00"  # Dark yellow button
elif theme_color == 'Red':
    bg_color = "#FFCCCC"  # Light red background
    text_color = "#660000"  # Dark red text
    button_color = "#FF0000"  # Red button

# Define background image based on user selection
base_path = r"C:\Users\sarim\OneDrive\Desktop\New folder"  # Base path for images
image_paths = {
    "Forest": os.path.join(base_path, "forest.jpeg"),
    "Ocean": os.path.join(base_path, "ocean.jpeg"),
    "Mountains": os.path.join(base_path, "mountains.jpeg"),
    "Desert": os.path.join(base_path, "desert.jpeg")
}

# Now use bg_option to get the correct image path
selected_image_path = image_paths.get(bg_option)

# Debug: print the selected image path and check if the file exists
st.write(f"Selected image path: {selected_image_path}")
st.write(f"File exists: {os.path.exists(selected_image_path)}")

# Check if the image file exists
if os.path.exists(selected_image_path):
    # Apply background image using the relative path in CSS
    st.markdown(
        f"""
        <style>
        body {{
            background-image: url("file:///{selected_image_path.replace('\\', '/')}"); 
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.error(f"Background image for {bg_option} not found. Please ensure the image file is available.")

# Apply global styles
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};  /* Text color set here */
        font-size: {font_size}px;
    }}
    .stButton button {{
        background-color: {button_color};
        color: white;  /* Button text color */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# App content
st.title("Welcome to the Global Nature Theme!")
st.write(f"You're currently using the **{theme_color}** with the **{bg_option}** background.")
st.write("This theme is inspired by natural beauty from around the world, designed for global users on desktop.")

# Example button
if st.button("Learn More"):
    st.write("Nature-inspired designs foster calm and tranquility.")
