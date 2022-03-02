from listener import take_user_input
from speaker import play_sound, speak
import requests
from decouple import config
from intents.myipintent import find_my_ip

OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")

def handle_intent():
    play_sound('assets/correct.wav')
    ip_address = find_my_ip()
    city = requests.get(f"https://ipapi.co/{ip_address}/region/").text
    speak(f"Getting weather report for {city}")
    weather, temperature, feels_like = get_weather_report(city)
    speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
    speak(f"Also, the weather report talks about {weather}")



def get_weather_report(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=imperial"
    res = requests.get(url).json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}°F", f"{feels_like}°F" # alt and 0176 on right keypad = degree symbol

if __name__ == "__main__":
    handle_intent ()