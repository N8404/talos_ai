from listener import take_user_input
from speaker import play_sound, speak
import pywhatkit as kit

def handle_intent():
    play_sound('assets/correct.wav')
    speak('What do you want to search on Google, sir?')
    query = take_user_input().lower()
    kit.search(query)