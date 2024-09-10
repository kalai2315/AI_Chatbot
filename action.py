import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def action(data):
    """
    Processes the input data to perform actions based on voice commands.
    """

    # Check if data is None or not a string
    if not isinstance(data, str):
        return "Invalid input. Please provide a string."

    user_data = data.lower()

    if "what is your name" in user_data:
        response = "My name is Virtual Assistant"
        text_to_speech.text_recognizer(response)
        return response

    elif "hello" in user_data or "hey" in user_data:
        response = "Hey, how may I help you?"
        text_to_speech.text_recognizer(response)
        return response

    elif "good morning" in user_data:
        response = "Good morning!"
        text_to_speech.text_recognizer(response)
        return response

    elif "what is the time now" in user_data:
        current_time = datetime.datetime.now()
        time_str = f"The current time is {current_time.hour}:{current_time.minute}."
        text_to_speech.text_recognizer(time_str)
        return time_str

    elif "shutdown" in user_data:
        response = "Shutting down."
        text_to_speech.text_recognizer(response)
        return response

    elif "play music" in user_data:
        webbrowser.open("https://spotify.com/")
        response = "Spotify is ready to play."
        text_to_speech.text_recognizer(response)
        return response

    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        response = "YouTube is ready to open."
        text_to_speech.text_recognizer(response)
        return response

    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        response = "Google is now open."
        text_to_speech.text_recognizer(response)
        return response

    elif "what is the weather today" in user_data:
        output = weather.weather()  # Ensure this returns a string
        text_to_speech.text_recognizer(output)
        return output

    else:
        response = "Can you repeat that? I am not able to understand."
        text_to_speech.text_recognizer(response)
        return response

if __name__ == "__main__":
    # Example usage of the action function
    print(action("What is the time now?"))
