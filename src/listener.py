import speech_recognition as sr
import datetime
from speaker import speak,play_sound

def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Thinking...')
        query = r.recognize_google(audio, language='en-us')
        if  'exit' in query or 'stop' in query:
            play_sound('assets/correct.wav')
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        #speak('Sorry, I could not understand. Could you please say that again?')
        play_sound('assets/error.wav')
        query = None
    print (f"I Heard; {query}")
    return query


def main():
    print ("No Default Functionality-Import From An Existing script.")
    
    
if __name__ == "__main__":
    main()