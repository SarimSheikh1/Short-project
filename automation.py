import streamlit as st
import webbrowser

# Set the title of the app
st.title("🌐 Automation by Sarim")

# Set the dark background color and text color in Streamlit using CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1e1e1e;  /* Dark background color */
        color: white;  /* Text color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to open the YouTube search
def search_youtube(query):
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

# Function to open the Google search
def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

# Function to open Instagram profile
def search_instagram(username):
    username = username.replace('@', "")
    url = f"https://www.instagram.com/{username}/"
    webbrowser.open(url)

# Function to open Facebook search
def search_facebook(query):
    url = f"https://www.facebook.com/search/top?q={query}"
    webbrowser.open(url)

# Function to search on X (formerly Twitter)
def search_x(query):
    url = f"https://twitter.com/search?q={query}"
    webbrowser.open(url)

# Function to search on ChatGPT
def search_chatgpt(query):
    url = f"https://chat.openai.com/?q={query}"
    webbrowser.open(url)

# Function to search on Gemini (Google's AI)
def search_gemini(query):
    url = f"https://gemini.google.com/search?q={query}"
    webbrowser.open(url)

# Function to search on GitHub
def search_github(query):
    url = f"https://github.com/search?q={query}"
    webbrowser.open(url)

# Function to search on Meta AI
def search_meta_ai(query):
    url = f"https://ai.facebook.com/search?q={query}"
    webbrowser.open(url)

# Function to search on Snapchat
def search_snapchat(query):
    url = f"https://story.snapchat.com/search?q={query}"
    webbrowser.open(url)

# Input field to take the search command from the user
query = st.text_input("Enter your command:")

# Buttons for each platform with emojis
if st.button("🔍 Search on YouTube"):
    search_youtube(query)

if st.button("🌐 Search on Google"):
    search_google(query)

if st.button("📸 Search on Instagram"):
    search_instagram(query)

if st.button("📘 Search on Facebook"):
    search_facebook(query)

if st.button("🐦 Search on X (formerly Twitter)"):
    search_x(query)

if st.button("🤖 Search on ChatGPT"):
    search_chatgpt(query)

if st.button("✨ Search on Gemini"):
    search_gemini(query)

if st.button("🐙 Search on GitHub"):
    search_github(query)

if st.button("🧠 Search on Meta AI"):
    search_meta_ai(query)

if st.button("👻 Search on Snapchat"):
    search_snapchat(query)
