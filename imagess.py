import streamlit as st
from PIL import Image
import time

# Function to display the slideshow
def display_slideshow(image_paths, delay):
    img = st.empty()  # Placeholder for the slideshow
    for image_path in image_paths:
        image = Image.open(image_path)
        img.image(image, use_column_width=True)
        time.sleep(delay)  # Pause between images

# List of image paths (update with your actual image paths)
image_paths = [
    'C:/Users/sarim/OneDrive/Desktop/New folder/imagess1.jepg',
    'C:/Users/sarim/OneDrive/Desktop/New folder/imagess1.jepg',
    'C:/Users/sarim/OneDrive/Desktop/New folder/imagess1.jepg'
]

# Slideshow delay (in seconds)
delay = 3  # Change image every 3 seconds

# App title
st.title("Image Slideshow")

# Add instructions or descriptions here
st.write("The slideshow will automatically change images every 3 seconds.")

# Start the slideshow
if st.button("Start Slideshow"):
    display_slideshow(image_paths, delay)
