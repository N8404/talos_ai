from datetime import datetime

first_name="T.A.L.O.S."
age=10
has_value= False


if has_value:
    print (f" My name is {first_name} and I am {age} weeks old: {has_value}")
else: 
    print ("No Value")

def write_message (message:str="nothing was given"):
    now=datetime.now()
    print (f" {now} {message}")
    
    
    
write_message (f" My name is {first_name} and I am {age} weeks old: {has_value}")
write_message (f"{first_name} {age}")
write_message ()    
    
    
