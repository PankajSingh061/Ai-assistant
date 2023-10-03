import webbrowser
import speech_recognition as sr
from gtts import gTTS
import os

def open_website(website):
    """
    Opens a specified website in the default web browser.

    Args:
        website (str): The URL of the website to open.
    """
    webbrowser.open(website)

def recognize_speech():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio).lower()
        return user_input
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError as e:
        print(f"Error: {e}")
    
    return ""

def text_to_speech(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")  # On Linux
    # For Windows, you can use: os.system("start response.mp3")

def main():
    while True:
        user_input = input("Hello! How can I assist you today? (Type 'exit' to quit or 'voice' for voice command) ").lower()
        
        if user_input == 'exit':
            print("Goodbye!")
            break
        elif user_input == 'voice':
            voice_command = recognize_speech()
            print(f"You said: {voice_command}")
            if 'youtube' in voice_command:
                open_website("https://www.youtube.com")
                text_to_speech("Opening YouTube.")
            elif 'instagram' in voice_command:
                open_website("https://www.instagram.com")
                text_to_speech("Opening Instagram.")
            elif 'linkedin' in voice_command:
                open_website("https://www.linkedin.com")
                text_to_speech("Opening LinkedIn.")
            else:
                response = "I'm not sure how to help with that. Try asking to open YouTube, Instagram, or LinkedIn."
                print(response)
                text_to_speech(response)
        else:
            print("I'm not sure how to help with that. Try asking to open YouTube, Instagram, or LinkedIn.")

import pygame
from gtts import gTTS

pygame.init()
pygame.mixer.init()

def text_to_speech(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

import os
from gtts import gTTS

def text_to_speech(text, savefile="response.mp3"):
    tts = gTTS(text)
    file_path = os.path.join(os.path.expanduser("~"), savefile)  # Save in the user's home directory
    tts.save(file_path)
    return file_path


if __name__ == "__main__":
    main()

