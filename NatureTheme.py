import streamlit as st
import os

# Set page configuration
st.set_page_config(page_title="Nature Theme", layout="centered")

# Sidebar for theme options
with st.sidebar:
    st.title("Nature Theme Options")
    st.write("Select your Nature Theme settings:")

    # Option to toggle between theme colors
    theme_color = st.selectbox("Choose your theme color", [
        'Light Mode', 'Dark Mode', 'Black', 'Yellow', 'Red', 
        'Pastel', 'Earthy Autumn', 'Neon', 'Sunset', 'Ocean'
    ])

    # Option to choose nature background image from different global locations
    bg_option = st.selectbox("Select a Nature Background", ["Forest", "Ocean", "Mountains", "Desert"])

    # Option to change font size for global accessibility
    font_size = st.slider("Adjust Font Size", 12, 24, 16)

# Define color schemes based on user selection
if theme_color == 'Light Mode':
    bg_color = "#E6F2E6"
    text_color = "#2E4600"
    button_color = "#9BBF30"
elif theme_color == 'Dark Mode':
    bg_color = "#2E4600"
    text_color = "#F4EBC3"
    button_color = "#617A55"
elif theme_color == 'Black':
    bg_color = "#000000"
    text_color = "#FFFFFF"
    button_color = "#FF0000"
elif theme_color == 'Yellow':
    bg_color = "#FFFF00"
    text_color = "#000000"
    button_color = "#FFCC00"
elif theme_color == 'Red':
    bg_color = "#FFCCCC"
    text_color = "#660000"
    button_color = "#FF0000"
elif theme_color == 'Pastel':
    bg_color = "#FFD1DC"  # Light pink
    text_color = "#3C3C3C"  # Dark gray
    button_color = "#FFB3B3"  # Light red
elif theme_color == 'Earthy Autumn':
    bg_color = "#C58C4D"  # Earthy brown
    text_color = "#FFF3E0"  # Light beige
    button_color = "#8A5B3B"  # Darker brown
elif theme_color == 'Neon':
    bg_color = "#39FF14"  # Neon green
    text_color = "#000000"  # Black
    button_color = "#FF005D"  # Neon pink
elif theme_color == 'Sunset':
    bg_color = "#FF7F50"  # Coral
    text_color = "#FFFFFF"  # White
    button_color = "#FFD700"  # Gold
elif theme_color == 'Ocean':
    bg_color = "#0099CC"  # Ocean blue
    text_color = "#FFFFFF"  # White
    button_color = "#006699"  # Darker blue

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

# this code to check the output in streamlit
# bash command: streamlit run NatureTheme.py