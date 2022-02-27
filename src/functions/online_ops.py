import json
import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

NEWS_API_KEY = config("NEWS_API_KEY")
OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")
TMDB_API_KEY = config("TMDB_API_KEY")
EMAIL_ACCOUNT = config("EMAIL_ACCOUNT")
EMAIL_PASSWORD = config("EMAIL_PASSWORD")


def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]


def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=5)
    return results


def play_on_youtube(video):
    kit.playonyt(video)


def search_on_google(query):
    kit.search(query)


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)


def send_email(receiver_address, subject, message):
    print (EMAIL_ACCOUNT)
    print (EMAIL_PASSWORD)
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL_ACCOUNT
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False


def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]


def get_weather_report(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=imperial"
    res = requests.get(url).json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}°F", f"{feels_like}°F" # alt and 0176 on right keypad = degree symbol


def get_trending_movies():
    trending_movies = []
    res = requests.get(
        f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5]


def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']


def get_word_meaning(word):
    WORDS_API_KEY=config("WORDS_API_KEY")
    try:
        res = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={WORDS_API_KEY}").json()          
        shortdef = res[0]['shortdef'][0]            
        message = f'The definition of {word} is:  {shortdef}'
    except Exception:
        message=(f'Sorry, I could not find the definition of {word}')
    
    return message


def get_word_synonym(word):
    THESAURUS_API_KEY=config("THESAURUS_API_KEY")
    message=""
    try:
        #https://www.dictionaryapi.com/api/v3/references/thesaurus/json/umpire?key=your-api-key
        res = requests.get(f"https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key={THESAURUS_API_KEY}").json()   
        #print (json.dumps(res))       
        top_five = res[0]['meta']['syns'][0]            
        message = f'The synonyms of {word} are:  {top_five}'
    except Exception:
        message=(f'Sorry, I could not find the synonyms for {word}')
    finally:
        return message