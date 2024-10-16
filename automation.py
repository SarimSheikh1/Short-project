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
    url = f"https://www.youtube.com/results?search_query={query}+full+movie"
    webbrowser.open(url)

# Function to open the Google search
def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

# Function to search for full movies on Google Play
def search_google_play_movies(query):
    url = f"https://play.google.com/store/search?q={query}+full+movie&c=movies"
    webbrowser.open(url)

# Function to search for full movies on Netflix
def search_netflix(query):
    url = f"https://www.netflix.com/search?q={query}"
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

# Function to search on GitHub
def search_github(query):
    url = f"https://github.com/search?q={query}"
    webbrowser.open(url)

# Function to open Meta AI homepage
def search_meta_ai():
    url = "https://ai.facebook.com"  # Meta AI homepage for research
    webbrowser.open(url)

# Function to open Google Search (as Gemini is not publicly available yet)
def search_gemini(query):
    url = f"https://www.google.com/search?q={query}+gemini"
    webbrowser.open(url)

# Function to search on Snapchat
def search_snapchat(query):
    url = f"https://story.snapchat.com/search?q={query}"
    webbrowser.open(url)

# Input field to take the search command from the user
query = st.text_input("Enter your command:")

# Buttons for each platform with emojis
if st.button("🎥 Search Full Movies on YouTube"):
    search_youtube(query)

if st.button("🎥 Search Full Movies on Google Play Movies"):
    search_google_play_movies(query)

if st.button("🎥 Search Full Movies on Netflix"):
    search_netflix(query)

if st.button("📸 Search on Instagram"):
    search_instagram(query)

if st.button("📘 Search on Facebook"):
    search_facebook(query)

if st.button("🐦 Search on X (formerly Twitter)"):
    search_x(query)

if st.button("🤖 Search on ChatGPT"):
    search_chatgpt(query)

if st.button("✨ Search on Gemini (Google)"):
    search_gemini(query)

if st.button("🐙 Search on GitHub"):
    search_github(query)

if st.button("🧠 Go to Meta AI Homepage"):
    search_meta_ai()

if st.button("👻 Search on Snapchat"):
    search_snapchat(query)
