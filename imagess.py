import streamlit as st
from PIL import Image

# Local paths to the image (update the paths with the actual location on your machine)
image_paths = [
    'C:/Users/sarim/OneDrive/Desktop/New folder/imagess1.jpeg',  # Make sure this path is correct
    'C:/Users/sarim/OneDrive/Desktop/New folder/imagess2.jpg',
    'C:/Users/sarim/OneDrive/Desktop/New folder/imagess1.jpeg'
]

# Initialize session state for image index if not already set
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# Function to display the current image
def display_image(index, width=None):
    try:
        image = Image.open(image_paths[index])
        st.image(image, use_column_width=width is None, width=width)
    except FileNotFoundError:
        st.error(f"File not found: {image_paths[index]}")

# App title
st.title("Image Slideshow")

# Display the current image with an adjustable width (e.g., 500 pixels)
display_image(st.session_state.current_index, width=500)

# Add navigation buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Previous"):
        if st.session_state.current_index > 0:
            st.session_state.current_index -= 1
        else:
            st.warning("This is the first image.")
with col2:
    if st.button("Next"):
        if st.session_state.current_index < len(image_paths) - 1:
            st.session_state.current_index += 1
        else:
            st.warning("This is the last image.")

# Add instructions or descriptions here
st.write("Use the buttons to navigate through the images.")
