import tkinter as tk
import pyttsx3
import speech_recognition as sr
import threading
from bardapi import BardCookies

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize BardCookies
cookie_dict = {
    "__Secure-1PSID" : "aghohjAYlFljn3d8S7N5jGJ87KbEGmwsmnfiFxlnfpg58tYiGlghfVMg3_aoiM3l1Eeo3Q.",
    "__Secure-1PSIDTS" : "sidts-CjIB3e41heWc8QKFII5la74uG2gr9OxD0fu_76iH12arrih0O4-UsB7JUMFWyKZZZIjDUhAA",
    "__Secure-1PSIDCC" : "APoG2W8Mm_T4fA3lLiIJAOluv22oyhOxt_SeqmjAYADBgiq6bFXuzER2cEm1RA2H-R4bKTJlvFHb"
}
bard = BardCookies(cookie_dict=cookie_dict)

# Initialize the TTS engine
tts_engine = pyttsx3.init()

# Function to handle speech recognition and response
def handle_speech():
    # Capture speech input from the user
    with sr.Microphone() as source:
        instructions_label.config(text="Speak your query:")
        instructions_label.update_idletasks()  # Update the label text
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        audio = recognizer.listen(source)

    try:
        # Recognize the speech input
        query = recognizer.recognize_google(audio)
        input_text.delete(1.0, tk.END)  # Clear previous input
        input_text.insert(tk.END, query)

        # Get the reply from Bard
        reply = bard.get_answer(query)['content']

        # Display the reply
        response_label.config(text="Bard: " + reply)
        response_label.update_idletasks()  # Update the label text

        # Speak the reply
        tts_engine.say(reply)
        tts_engine.runAndWait()

    except sr.UnknownValueError:
        response_label.config(text="Sorry, I could not understand your speech.")
    except sr.RequestError as e:
        response_label.config(text=f"Could not request results; {e}")

# Function to run speech recognition and response logic in a separate thread
def run_speech_thread():
    speech_thread = threading.Thread(target=handle_speech)
    speech_thread.start()

# Create the main GUI window
root = tk.Tk()
root.title("Speech Interaction")

# Create GUI components
input_text = tk.Text(root, height=5, width=50)
instructions_label = tk.Label(root, text="Press 'Listen' and speak your query:")
listen_button = tk.Button(root, text="Listen and Respond", command=run_speech_thread)
response_label = tk.Label(root, text="Response will appear here.")

# Arrange GUI components
input_text.pack()
instructions_label.pack()
listen_button.pack()
response_label.pack()

root.mainloop()
