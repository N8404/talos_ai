from speaker import play_sound, speak
import requests
from decouple import config

TMDB_API_KEY=config("TMDB_API_KEY")

def handle_intent():
    play_sound('assets/correct.wav')
    speak(f"Some of the trending movies are: {get_trending_movies()}")
    # speak("For your convenience, I am printing it on the screen sir.")
    # print(*get_trending_movies(), sep='\n')

def get_trending_movies():
    trending_movies = []
    res = requests.get(
        f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:10]


if __name__ == "__main__":
    handle_intent ()