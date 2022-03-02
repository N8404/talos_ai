from speaker import speak, play_sound
import requests

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def handle_intent():
    play_sound('assets/correct.wav')
    ip_address = find_my_ip()
    speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
    print(f'Your IP Address is {ip_address}')
    
    
if __name__ == "__main__":
    handle_intent (None)