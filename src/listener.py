import speech_recognition as sr
import datetime
from speaker import speak,play_sound

def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('T.A.L.O.S.> Listening....')
        r.pause_threshold = .5
        audio = r.listen(source)

    try:
        print('T.A.L.O.S.> Thinking...')
        query = r.recognize_google(audio, language='en-us')
        if  'exit' in query or 'stop' in query:
            play_sound('assets/correct.wav')
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("T.A.L.O.S.> Good night sir, take care!")
            else:
                speak('T.A.L.O.S.> Have a good day sir!')
            exit()
    except Exception:
        print('T.A.L.O.S.> Sorry, I could not understand.')
        play_sound('assets/error.wav')
        query = None
    print (f"T.A.L.O.S.> I heard: {query}")
    return query


def main():
    print ("No Default Functionality-Import From An Existing script.")
    
    
if __name__ == "__main__":
    main()