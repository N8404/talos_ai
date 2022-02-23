import requests
from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message, get_word_meaning
from decouple import config
from datetime import datetime
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord
from random import choice
from utils import opening_text
from pprint import pprint
from random import random
import time 
from playsound import playsound
from speaker import speak,play_sound
from listener import take_user_input


def start_dispatch(query):
    if query is None:
        print(f"I havent heard anything.")
    else:
        query = query.lower()
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

        elif 'what time is it' in query:
            play_sound('assets/correct.wav')
            current_time = datetime.now()
            formatted = current_time.strftime('%I:%M %p, on %A, %b %d %Y')
            message = f'The current time is {formatted}'
            print (message)
            speak (message)

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

        elif 'definition' in query:
            play_sound('assets/correct.wav')
            speak(f'What word do you want me to look up, sir?')
            query = take_user_input().lower()
            result=get_word_meaning(query)
            print (result)
            speak (result)
        
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
            
        elif 'what is your favorite color' in query:
            play_sound('assets/correct.wav')
            speak (f"Robots dont usually have favorite colors, but i perfer blue.")                
        
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
        
def main():
    print ("No Default Functionality-Import From An Existing script.")
    
    
if __name__ == "__main__":
    main()