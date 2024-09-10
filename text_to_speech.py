

import pyttsx3

def text_recognizer(text):
    engine = pyttsx3.init()

    # Get available voices
    voices = engine.getProperty('voices')

    # Choose a female voice
    for voice in voices:
        if 'female' in voice.name.lower() or 'female' in voice.id.lower():
            engine.setProperty('voice', voice.id)
            break

    # Set speech rate (optional)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)  # Adjust rate if needed

    # Speak the text
    engine.say(text)
    engine.runAndWait()

# Example usage
text_recognizer("Hello, I am your AI assistant.")
