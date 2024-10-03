import re

# Define responses for HTML and CSS related questions
def chatbot_response(user_input):
    user_input = user_input.lower()

    # HTML-related responses
    if re.search(r"\bwhat is html\b", user_input):
        return "HTML stands for HyperText Markup Language. It is used to structure content on the web."
    elif re.search(r"\b(html tag|create)\b.*link", user_input):
        return "You can create a link using the <a> tag, like this: <a href='url'>Link</a>."
    elif re.search(r"\b(html tag|insert|embed)\b.*image", user_input):
        return "You can insert an image using the <img> tag, like this: <img src='image.jpg' alt='Description'>."

    # CSS-related responses
    elif re.search(r"\bwhat is css\b", user_input):
        return "CSS stands for Cascading Style Sheets, and it is used to style and layout web pages."
    elif re.search(r"\bchange\b.*background\b.*color", user_input):
        return "You can change the background color in CSS using the 'background-color' property, like this: background-color: blue;"
    elif re.search(r"\b(change|set)\b.*font.*size", user_input):
        return "You can set the font size in CSS using the 'font-size' property, like this: font-size: 16px;"

    # Closing response
    elif re.search(r"\b(exit|quit|goodbye)\b", user_input):
        return "Goodbye! Thanks for chatting about HTML & CSS."

    # Default response
    else:
        return "Sorry, I don't understand that. Try asking about HTML or CSS."

print("Ask me about HTML or CSS! Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print(f"Bot: {response}")
    if response == "Goodbye! Thanks for chatting about HTML & CSS.":
        break
