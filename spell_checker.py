import streamlit as st
from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()
        
    def correct_text(self, text):
        words = text.split()
        corrected_words = []
        
        for word in words:
            corrected_word = self.spell.correction(word)  # Correct the word
            if corrected_word != word.lower():
                st.write(f'🔧 Correcting "{word}" to "{corrected_word}"')
            corrected_words.append(corrected_word)
        
        return ' '.join(corrected_words)

# Streamlit App
def main():
    st.title("🔍 Spell Checker App 📝")
    
    spell_checker = SpellCheckerApp()
    
    st.subheader("Check for spelling mistakes quickly and easily! 🎯")
    
    text = st.text_input("✍️ Enter text to check:")
    
    if st.button("🔎 Check Spelling"):
        if text:
            corrected_text = spell_checker.correct_text(text)
            st.success(f"✅ Corrected text: {corrected_text}")
        else:
            st.warning("⚠️ Please enter some text to check.")

if __name__ == '__main__':
    main()
