import requests
from functions.online_ops import get_weather_report
from decouple import config
from datetime import datetime
from random import choice
from utils import opening_text
from pprint import pprint
from random import random
import time 
from playsound import playsound
from speaker import speak,play_sound
from listener import take_user_input
from intents import adviceintent, googleintent, jokeintent, myipintent, \
                    synonymintent, whattimeintent, wikipediaintent,\
                    wordlookupintent, youtubeintent, emailintent,\
                    movieintent, newsintent
from intents.myipintent import find_my_ip

USER=config("USER")


def start_dispatch(query):
    if query is None:
        print(f"I havent heard anything.")
    else:
        query = query.lower()
        
        if 'ip address' in query:
            myipintent.handle_intent()            

        elif 'time' in query:
            whattimeintent.handle_intent()
            
        elif 'wikipedia' in query:
            wikipediaintent.handle_intent(query)
            
        elif 'youtube' in query:
            youtubeintent.handle_intent()

        elif 'search on google'in query or 'google' in query:
            googleintent.handle_intent()
            
        elif 'definition' in query:
            wordlookupintent.handle_intent(query)
        
        
        elif "email" in query:
            emailintent.handle_intent()
            

        elif 'joke' in query:
            jokeintent.handle_intent()
            

        elif "advice" in query:
            adviceintent.handle_intent()
            

        elif "trending movies" in query:
            movieintent.handle_intent()
            

        elif 'news' in query:
            newsintent.handle_intent()
          

        elif 'weather' in query:
            play_sound('assets/correct.wav')
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/region/").text
            speak(f"Getting weather report for {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            
                                                                                                                
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
        
        elif 'synonym' in query or "thesaurus" in query:
            synonymintent.handle_intent(query)
            
            
        elif 'what can you do' in query:
            speak (f"Some commands you can ask me are, synonym, flip a coin, wikipedia, youtube, google, what is your favorite color, what are you, weather, news, trending movies, send an email, advice, joke, definition, what time is it , ip adress,  calculator, camera, cmd. hope this was helpfull.")
            
        else:
            
            print (f"I did not recognize any commands.")
            #play_sound('assets/error.wav')
        
def main():
    print ("No Default Functionality-Import From An Existing script.")
    
    
if __name__ == "__main__":
    main()