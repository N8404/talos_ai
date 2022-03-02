from speaker import speak, play_sound
import requests

def handle_intent():
    play_sound('assets/correct.wav')
    speak(f"Here is a joke sir")
    joke = get_random_joke()
    speak(joke)
    
def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

if __name__ == "__main__":
    handle_intent ()