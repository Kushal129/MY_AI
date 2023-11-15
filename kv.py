import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.... ")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
            # audio = recognizer.listen(source)
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print("You said:", data)
            return data

        except sr.WaitTimeoutError:
            print("Listening timed out. No speech detected within 5 seconds.")
        except sr.UnknownValueError:
            print("No speech detected.")
        except sr.RequestError as e:
            print(
                f"Could not request results from Google Speech Recognition service; {e}")


def speech_to_text(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 170)
    engine.say(x)
    engine.runAndWait()


speech_to_text("hello ")
# program ne spiite karse uparno aalg ne niche no aalg
if __name__ == '__main__':
    while True:
        data1 = sptext()
        if data1 is not None:
            data1 = data1.lower()
            if "hey kv" in data1:
                while True:
                    data1 = sptext().lower()
                    if "your name" in data1:
                        name = "my name is kv sir"
                        speech_to_text(name)

                    elif "old are you" in data1:
                        name = "hahahahaha , i am 1 year old sir"
                        speech_to_text(name)

                    elif "boss name" in data1:
                        name = "The One and Only My hero Mr Kushal Pipaliya "
                        speech_to_text(name)

                    elif "time" in data1:
                        current_time = datetime.datetime.now().strftime("%I:%M %p")
                        print("The current time is", current_time)
                        speech_to_text("The current time is " + current_time)

                    elif "youtube" in data1:
                        webbrowser.open("https://www.youtube.com/")
                        speech_to_text("Opening youtube sir ")

                    elif "play song" in data1:
                        song_name = data1.split("play song")[1].strip()
                        search_query = "+".join(song_name.split())
                        youtube_url = f"https://www.youtube.com/results?search_query={search_query}"
                        webbrowser.open(youtube_url)
                        speech_to_text(
                            f"Opening YouTube and searching for {song_name} on YouTube")

                    elif "my github" in data1:
                        webbrowser.open("https://github.com/Kushal129/")
                        speech_to_text("Opening Your Github Sir ")

                    elif "joke" in data1:
                        joke_1 = pyjokes.get_joke(
                            language="en", category="all")
                        print(joke_1)
                        speech_to_text(joke_1)

                    elif "play song number " in data1:
                        add = "D:/song/Garba 2023"
                        listsong = os.listdir(add)
                        try:
                            number = int(data1.split(
                                "play song number")[1].strip())
                            if 1 <= number <= len(listsong):
                                song_to_play = os.path.join(
                                    add, listsong[number - 1])
                                os.startfile(song_to_play)
                                speech_to_text(f"Playing song number {number}")
                            else:
                                speech_to_text(
                                    "Invalid song number. Please choose a valid number.")
                        except ValueError:
                            speech_to_text(
                                "Invalid input. Please specify a valid song number.")

                    elif "chalo bye" in data1 or "exit" in data1:
                        speech_to_text("Thank you. Have a good day sir.")
                        break
                    time.sleep(7)

            else:
                print("Thank You")
                speech_to_text("Sorry sir i dont get")
        else:
            speech_to_text("No speech detected. Goodbye, sir.")
            break



# Kushal Pipaliya 