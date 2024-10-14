import streamlit as st
from time import strftime, sleep

# Set page configuration
st.set_page_config(page_title="Digital Clock", page_icon="⏰", layout="centered")

# Function to display the current time with emojis
def time():
    return strftime('%H:%M:%S %p \n %D')

# Title of the application with an emoji
st.title("⏰ Digital Clock")

# Set up a placeholder for the clock
clock_placeholder = st.empty()

# Update the clock every second
while True:
    current_time = time()
    # Add emojis for morning, afternoon, and night
    hour = int(strftime('%H'))  # Get the current hour
    if 6 <= hour < 12:
        emoji = "🌅 Good Morning!"
    elif 12 <= hour < 18:
        emoji = "🌞 Good Afternoon!"
    else:
        emoji = "🌜 Good Evening!"

    # Display the time with emojis
    clock_placeholder.markdown(f"""
    <h1 style='text-align: center; color: cyan; background-color: gold;'>
    {current_time} <br> {emoji} 
    </h1>""", unsafe_allow_html=True)

    sleep(1)
# this code to check the output in streamlit
# bash command: streamlit run clock.py