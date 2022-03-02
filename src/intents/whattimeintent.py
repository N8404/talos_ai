from listener import take_user_input
from speaker import speak,play_sound
from datetime import datetime
import playsound


def handle_intent(query:str=""):
    play_sound('assets/correct.wav')
    current_time = datetime.now()
    formatted = current_time.strftime('%I:%M %p, on %A, %b %d %Y')
    message = f'The current time is {formatted}'
    #print (message)
    speak (message)


    
if __name__ == "__main__":
     (None)