import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import os
import vlc
import os
from google import genai
import os
import API_KEY

client = genai.Client(api_key=API_KEY.Gemini_API_KEY)
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))  # set gemini api key as environment variable and uncomment this line
# newsapikey = os.getenv("NEWS_API_KEY")  # set newapi key as environment variable and uncomment this line

player = None

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def chat_ai(command):
    try:
        response = client.models.generate_content(
        model="gemini-flash-latest",  # <--- Change to this
        config=genai.types.GenerateContentConfig(
        system_instruction="Always keep your responses extremely short and concise. two to five sentences max.",
        ),
        contents=command
        )
        return response.text

    except Exception as e:
        print(f"Error: {e}")

def processCommand(c):

    #open social media 
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open linkdin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    
    # shout down Jarvis
    elif "exit" in c.lower():
        speak("Good By Narendra!!")
        speak("Ok...")
        exit()

    # YouTube Music play
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    # News teller
    elif "news" in c.lower():
        try:
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY.newsapikey}"
            r = requests.get(url)
            data = r.json()

            articles = data["articles"]

            speak("Here are the top headlines")

            for article in articles[:5]:      # first 5 headlines
                print(article["title"])
                speak(article["title"])

        except Exception as e:
            print("Error getting news:", e)
            speak("Sorry, I could not fetch the news")

    # Downloaded Music Player
    elif "music" in c.lower():
        try:
            music_dir = r"D:\Songs"
            songs = os.listdir(music_dir)

            import random
            song = random.choice(songs)

            speak("Playing a song for you")
            global player
            player = vlc.MediaPlayer(os.path.join(music_dir, song))
            player.play()
        except Exception as e:
            print(e)

    # how are you
    elif c.lower().startswith("how"):
        speak("I am fine Narendra, How about you")

    # YouTube Music play
    elif "play" in c.lower():
        song = c.lower().strip(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    # YouTube Music play
    elif "good night" in c.lower():
        speak("Good Night, Narendra... Have sweet dream....")
    
    elif "pause" in c.lower():
        if player:
            player.pause()

    elif "resume" in c.lower():
        if player:
            player.play()

    elif "stop" in c.lower():
        if player:
            player.stop()

    
    else:
        reply = chat_ai(c)
        print(reply)
        speak(reply)

if __name__=="__main__":
    speak("Initializing.....jarvis")
    # Listen for the wake word "Jarvis"
    # obtain audio from the microphone
    while True:
        r = sr.Recognizer()
        
        
        # recognize speech using Sphinx
        
        try:
            with sr.Microphone() as source:
                print("Listening......")
                # r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
                print("recognizing......")

                word = r.recognize_google(audio)
                print(word)

                if "jarvis" in word.lower():
                    speak("Ya")
                    #listen for command
                    with sr.Microphone() as source:
                        print("Jarvis Active.......")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)

                        processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))