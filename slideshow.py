import streamlit as st
from PIL import Image
from time import sleep

# Title of the app
st.title("Image Slideshow")

# Image uploader for user to upload multiple images
uploaded_files = st.file_uploader("Upload Images", type=['jpg', 'png', 'jpeg'], accept_multiple_files=True)

image_size = (245, 500)
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
