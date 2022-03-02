import logging
import random
from datetime import datetime
from random import random
from decouple import config
import dispatch
from listener import take_user_input
from speaker import play_sound, speak

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

def greet_user():
    """Greets the user according to the time"""
    speak(f"Hello {USERNAME}, {BOTNAME} here.")

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
            print(f"T.A.L.O.S.> I havent heard anything in {no_response_count} requests.")
        else:
            query = query.lower()
            no_response_count = 0
            dispatch.start_dispatch(query)            

if __name__ == '__main__':
    try:
        level = logging.WARNING
        format = '[%(levelname)s] %(asctime)s - %(message)s'
        logging.basicConfig(level=level, format=format)
    
        main()
    except KeyboardInterrupt:
        print ("T.A.L.O.S.> Now Exiting, Goodbye!")
