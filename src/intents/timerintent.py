from listener import take_user_input
from speaker import speak,play_sound
from datetime import datetime, timedelta
import multiprocessing

def create_timer():
    """Handles the intent.

    """
    play_sound('assets/correct.wav')
    speak('How long would you like the timer?')
    timer_duration = take_user_input().lower()
    if timer_duration.lower() == 'cancel':
        print(f'T.A.L.O.S.> Cancelling...')
        speak('Cancelling.')
        return
    seconds=None
    # "30 seconds" = [ 30,"seconds"]
    time_parts=timer_duration.split(' ')    
    if time_parts [1]=="seconds":
        seconds=time_parts[0]
    elif time_parts [1] == "minutes":
        seconds=time_parts[0] * 60
    elif time_parts [1] == "hours":
        seconds=time_parts[0] * 60 * 60
    print (f"for the timer {seconds}")
    
    # Async
    running_proc=multiprocessing.Process(target=run_timer, args=( int(seconds), )) 
    running_proc.start()
    
    # Sync
    #run_timer(int(seconds))
    
def run_timer(seconds:int):   
    stop = False
    stop_time=str(datetime.now() + timedelta(seconds=seconds))
    print(f"Timer will trigger at {stop_time}")
    while stop == False:
        rn = str(datetime.now())
        if rn >= stop_time:
            stop = True
            play_sound ('assets/alarm.wav')