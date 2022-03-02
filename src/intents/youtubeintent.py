from listener import take_user_input
from speaker import play_sound, speak
import pywhatkit as kit

def handle_intent():    
    play_sound('assets/correct.wav')
    speak('What do you want to play on Youtube, sir?')
    video = take_user_input().lower()
    kit.playonyt(video)
    
    
if __name__ == "__main__":
    handle_intent ()