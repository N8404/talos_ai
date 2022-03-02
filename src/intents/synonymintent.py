"""Module for handeling synonyms."""
from listener import play_sound, take_user_input
from speaker import speak
from decouple import config
import requests

USER=config("USER")

def get_word_synonym(word):
    """Get synonym for word.

    Args:
        word (str): The word to get synonymed.

    Returns:
        str: Brings back synonyms for the inputed word.
    """
    

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

def handle_intent(query):
    """Handles the intent.

    Args:
        query (str): The original query from the user.
    """
    
    play_sound('assets/correct.wav')
    speak(f'What word do you want me to find the synonym for,{USER}')
    query = take_user_input().lower()
    result=get_word_synonym(query)
    speak (result)
    
if __name__ == "__main__":
    handle_intent (None) 