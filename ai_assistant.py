import streamlit as st
import text_to_speech
import action
from PIL import Image
import speech_to_text

# Streamlit App
def main():
    # Set page configuration
    st.set_page_config(
        page_title="AI Assistant",
        page_icon="🤖",
        layout="centered",
        initial_sidebar_state="auto",
    )

    # Title
    st.title("AI Assistant")

    # Image
    try:
        image_path = r"F:\project\AI_Desktop\kalai_AI.jpg"  # Replace with your image path
        image = Image.open(image_path)
        st.image(image, caption="AI Assistant",  width=300)
    except Exception as e:
        st.error(f"Error loading image: {e}")

    st.sidebar.title("AI Assistant Questions")
    st.sidebar.write(
        """
        - What is your name?
        - Hello
        - Good morning
        - What is the time now?
        - Shutdown
        - Play music
        - YouTube
        - Open Google
        - What is the weather today
        """
    )

    # Text Area for Chat History
    chat_history = st.empty()

    # Initialize session state for chat
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    # User Input
    user_input = st.text_input("You:", "")

    # Process user input
    if user_input:
        st.session_state['history'].append(f"User: {user_input}")
        response = action.action(user_input)
        st.session_state['history'].append(f"BOT: {response}")

    # Display chat history
    chat_history.text_area("Chat History", value="\n".join(st.session_state['history']), height=300)

    # Button to use microphone for input
    if st.button("Use Microphone"):
        user_voice_input = speech_to_text.recognize_speech()
        if user_voice_input:
            st.session_state['history'].append(f"User: {user_voice_input}")
            response = action.action(user_voice_input)
            st.session_state['history'].append(f"BOT: {response}")

    # Clear button
    if st.button("Clear Chat"):
        st.session_state['history'] = []

if __name__ == "__main__":
    main()
