from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message, get_word_meaning
from decouple import config
from datetime import datetime
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord
from random import choice
from utils import opening_text
from pprint import pprint
from random import random 
import random
import dispatch
from speaker import speak,play_sound
from listener import take_user_input

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

def greet_user():
    """Greets the user according to the time"""
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"Hello {USERNAME} I am {BOTNAME}, How may I help you?")

def get_user_name():
    user=config("USER")
    usernames=user.split(',')
    max_len = len(usernames)
    selected_username = usernames [int(random.uniform(0,max_len))]
    return selected_username

def main():
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
            dispatch.start_dispatch(query)            

if __name__ == '__main__':
    main()