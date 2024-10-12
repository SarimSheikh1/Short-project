import streamlit as st
from PIL import Image
from time import sleep

# Title of the app
st.title("Image Slideshow")

# List of image paths
image_paths = [
    r"C:\Users\sarim\OneDrive\Desktop\Sarim important\hairstyle1.jpg",
    r"C:\Users\sarim\OneDrive\Desktop\Sarim important\IMG-20240922-WA0004.jpg",
    r"C:\Users\sarim\OneDrive\Desktop\Sarim important\IMG-20240922-WA0001.jpg",
    r"C:\Users\sarim\OneDrive\Desktop\Sarim important\IMG-20240922-WA0007.jpg",
    r"C:\Users\sarim\OneDrive\Desktop\Sarim important\IMG-20240922-WA0006.jpg"
]

image_size = (1080, 1080)

# Resize images
images = [Image.open(path).resize(image_size) for path in image_paths]

# Button to start slideshow
if st.button('Start Slideshow'):
    for image in images:
        # Display image
        st.image(image)
        # Pause for 5 seconds between images
        sleep(5)
