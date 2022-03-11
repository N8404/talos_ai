from wave import WAVE_FORMAT_PCM
import pyttsx3
from playsound import playsound
engine = pyttsx3.init()

# Set Rate
engine.setProperty('rate', 190)

# # Set Volume
engine.setProperty('volume', 1.0) 

 # Set Voice (Female)
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0].id)
engine.setProperty('voice','english_rp')

def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()

def play_sound(file_name):
    """Plays a sound."""
    pass
    #playsound(file_name)
        
def main():
    print ("No Default Functionality-Import From An Existing script.")   
    
if __name__ == "__main__":
    main()
