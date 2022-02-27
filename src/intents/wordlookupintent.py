"""Module to handle word lookups."""

from speaker import play_sound, speak
from decouple import config
import requests
from listener import take_user_input

def get_word_meaning(word:str):
    """Gets the meaning of a word from the API.

    Args:
        word (str): The word to look up.

    Returns:
        str: A sentence with the definition of the word.
    """
    WORDS_API_KEY=config("WORDS_API_KEY")
    try:
        res = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={WORDS_API_KEY}").json()          
        shortdef = res[0]['shortdef'][0]            
        message = f'The definition of {word} is:  {shortdef}'
    except Exception:
        message=(f'Sorry, I could not find the definition of {word}')
    
    return message

def handle_intent (intent):
    """Handles the intent.

    Args:
        intent (str): The original query from the user.
    """
    play_sound('assets/correct.wav')
    speak(f'What word do you want me to look up, sir?')
    search_query = take_user_input().lower()
    if search_query.lower() == 'cancel':
        print(f'T.A.L.O.S.> Cancelling...')
        speak('Cancelling.')
        return    
    result=get_word_meaning(search_query)
    speak (result)
    
    
if __name__ == "__main__":
    handle_intent (None) 