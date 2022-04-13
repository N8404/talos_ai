"""Module to handle wikipedia searches."""

from listener import take_user_input
from speaker import speak,play_sound
import wikipedia

def search_on_wikipedia(query:str):
    """Search for a topic on wikipedia.

    Args:
        query (str): The topic to look up.

    Returns:
        str: Returns the first five sentences of the wikipedia result page.
    """
    results = wikipedia.summary(query, sentences=1)
    return results

def handle_intent (query):
    """Handles the intent.

    Args:
        query (str): The topic to look up.
    """
    play_sound('assets/correct.wav')
    speak('What do you want to search for on Wikipedia, sir?')
    search_query = take_user_input().lower()
    if search_query.lower() == 'cancel':
        print(f'T.A.L.O.S.> Cancelling...')
        speak('Cancelling.')
        return
    results = search_on_wikipedia(search_query)
    speak(f"Wikipedia says, {results}")
    
if __name__ == "__main__":
    handle_intent (None) 