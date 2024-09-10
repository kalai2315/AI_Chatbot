#F:\project\.venv\Scripts\Activate.ps1

import speech_recognition as sr

def recognize_speech():
    # Initialize recognizer
    r = sr.Recognizer()

    # Use the microphone as a source for input
    with sr.Microphone() as source:
        print("Please say something:")
        # Adjust for ambient noise and listen to the input
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        # Initialize voice_data
        voice_data = ""

        try:
            # Recognize the speech using Google Speech Recognition
            voice_data = r.recognize_google(audio)
            print("You said: " + voice_data)
            return voice_data
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Sorry, there was an error with the service.")

    return None  # Return None if an exception occurs

# Call the function
recognize_speech()
