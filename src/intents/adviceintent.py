from speaker import play_sound, speak
import requests

def handle_intent():
    play_sound('assets/correct.wav')
    speak(f"Here's some advice, sir")
    advice = get_random_advice()
    speak(advice)
    
def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']    

if __name__ == "__main__":
    handle_intent ()