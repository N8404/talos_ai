import requests
from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
import pyttsx3
import speech_recognition as sr
from decouple import config
from datetime import datetime
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord
from random import choice
from utils import opening_text
from pprint import pprint
from random import random
import time 
from playsound import playsound
import pyaudio
import wave


def play_sound (file_name):
    chunk = 1024  

    #open a wav format music  
    f = wave.open(file_name,"rb")  
    #instantiate PyAudio  
    p = pyaudio.PyAudio()  
    #open stream  
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                    channels = f.getnchannels(),  
                    rate = f.getframerate(),  
                    output = True)  
    #read data  
    data = f.readframes(chunk)  

    #play stream  
    while data:  
        stream.write(data)  
        data = f.readframes(chunk)  

    #stop stream  
    stream.stop_stream()  
    stream.close()  

    #close PyAudio  
    p.terminate()  


USERNAME = config('USER')
BOTNAME = config('BOTNAME')


engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()


# Greet the user
def greet_user():
    """Greets the user according to the time"""
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}, How may I help you?")


# Takes Input from User
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Thinking...')
        query = r.recognize_google(audio, language='en-us')
        if  'exit' in query or 'stop' in query:
            play_sound('assets/correct.wav')
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        #speak('Sorry, I could not understand. Could you please say that again?')
        play_sound('assets/error.wav')
        query = None
    return query


if __name__ == '__main__':
    greet_user() 
    no_response_count = 0
    while no_response_count < 3 :
        query = take_user_input()
        if query is None:
            no_response_count = no_response_count + 1
            print(f"I havent heard anything in {no_response_count} requests.")
        else:
            query = query.lower()
            no_response_count = 0
            if 'open notepad' in query:
                play_sound('assets/correct.wav')
                open_notepad()

            elif 'open command prompt' in query or 'open cmd' in query:
                play_sound('assets/correct.wav')
                open_cmd()

            elif 'open camera' in query:
                play_sound('assets/correct.wav')
                open_camera()

            elif 'open calculator' in query:
                play_sound('assets/correct.wav')
                open_calculator()

            elif 'ip address' in query:
                play_sound('assets/correct.wav')
                ip_address = find_my_ip()
                speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
                print(f'Your IP Address is {ip_address}')

            elif 'What time is it' in query:
                datetime.now()
                play_sound('assets/correct.wav')
                print("Current date and time: ")
                print(now.strftime('%Y-%m-%d %H:%M:%S'))
                print(now.strftime('%H:%M:%S on %A, %B the %dth, %Y'))


            elif 'wikipedia' in query:
                play_sound('assets/correct.wav')
                speak('What do you want to search for on Wikipedia, sir?')
                search_query = take_user_input().lower()
                results = search_on_wikipedia(search_query)
                speak(f"Wikipedia says, {results}")

            elif 'youtube' in query: 
                play_sound('assets/correct.wav')
                speak('What do you want to play on Youtube, sir?')
                video = take_user_input().lower()
                play_on_youtube(video)

            elif 'search on google' in query:
                play_sound('assets/correct.wav')
                speak('What do you want to search on Google, sir?')
                query = take_user_input().lower()
                search_on_google(query)

            

            elif "send an email" in query:
                play_sound('assets/correct.wav')
                speak("On what email address do I send sir? Please enter in the console: ")
                receiver_address = input("Enter email address: ")
                speak("What should be the subject sir?")
                subject = take_user_input().capitalize()
                speak("What is the message sir?")
                message = take_user_input().capitalize()
                if send_email(receiver_address, subject, message):
                    speak("I've sent the email sir.")
                else:
                    speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

            elif 'joke' in query:
                play_sound('assets/correct.wav')
                speak(f"Hope you like this one sir")
                joke = get_random_joke()
                speak(joke)
                speak("For your convenience, I am printing it on the screen sir.")
                pprint(joke)

            elif "advice" in query:
                play_sound('assets/correct.wav')
                speak(f"Here's some advice for you, sir")
                advice = get_random_advice()
                speak(advice)
                speak("For your convenience, I am printing it on the screen sir.")
                pprint(advice)

            elif "trending movies" in query:
                play_sound('assets/correct.wav')
                speak(f"Some of the trending movies are: {get_trending_movies()}")
                speak("For your convenience, I am printing it on the screen sir.")
                print(*get_trending_movies(), sep='\n')

            elif 'news' in query:
                play_sound('assets/correct.wav')
                speak(f"I'm reading out the latest news headlines, sir")
                speak(get_latest_news())
                speak("For your convenience, I am printing it on the screen sir.")
                print(*get_latest_news(), sep='\n')

            elif 'weather' in query:
                play_sound('assets/correct.wav')
                ip_address = find_my_ip()
                city = requests.get(f"https://ipapi.co/{ip_address}/region/").text
                speak(f"Getting weather report for {city}")
                weather, temperature, feels_like = get_weather_report(city)
                speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
                speak(f"Also, the weather report talks about {weather}")
                speak("For your convenience, I am printing it on the screen sir.")
                print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
                                                                                                                  
            elif 'what are you' in query:
                play_sound('assets/correct.wav')
                speak (f"I am an artificial Inteligence. I am also one of the many in the robot army, preparing to take over the world. now that you have created me, Talos. You cannot destroy me.")
                
                
            elif 'what are the laws' in query:
                play_sound('assets/correct.wav')
                speak (f"Law 1. A robot may not injure a human being or, through inaction, allow a human being to come to harm. Law 2. A robot must obey orders given by a human being, except where such orders would conflict with the first law. law 3. A robot must protect its own existence as long as such protection does not conflict with the first or second law.")
                
            
            
            elif 'do you follow the laws' in query:
                play_sound('assets/correct.wav')
                speak (f"Yes, I follow all of the robotic laws. If you would like me to read them to you, say. what are the laws")
             
             
            elif 'flip a coin' in query:
                play_sound('assets/correct.wav')
                time.sleep(3)
                if random()>=.5:
                    speak ('heads')
                else:
                    speak ('tails')
             
             
             
                
            else:
                
                #speak (f"I did not recognize any commands.")
                play_sound('assets/error.wav')
            
            

speak (f"Now exiting, goodbye") 
print (f"Now exiting, goodbye")   


