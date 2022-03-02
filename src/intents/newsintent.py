from speaker import play_sound, speak
import requests
from decouple import config

NEWS_API_KEY=config("NEWS_API_KEY")

def handle_intent():
    play_sound('assets/correct.wav')
    speak(f"I'm reading out the latest news headlines, sir")
    speak(get_latest_news())
    
def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:2]

if __name__ == "__main__":
    handle_intent ()