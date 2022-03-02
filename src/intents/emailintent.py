from email.message import EmailMessage
import smtplib
from speaker import speak, play_sound
from listener import take_user_input
from decouple import config

EMAIL_ACCOUNT = config("EMAIL_ACCOUNT")
EMAIL_PASSWORD = config("EMAIL_PASSWORD")

def handle_intent():
    print("T.A.L.O.S>>> What is the e-mail adddress: ")
    speak("What is the e-mail adddress: ")
    receiver_address = take_user_input() \
                        .replace('at sign','@') \
                        .replace('ampersand','@') \
                        .replace('at','@') \
                        .replace('dot','.') \
                        .replace(' ','')
    if receiver_address.lower() == 'me' or receiver_address.lower() == 'myself':
        receiver_address = config('USER_EMAIL')
    if receiver_address.lower() == 'cancel':
        print(f'Cancelling...')
        speak('Cancelling.')
        return
    print(f'  >> Email: {receiver_address}')
    
    print("T.A.L.O.S>>> What should be the subject?")
    speak("What should be the subject?")
    subject = take_user_input().capitalize()
    
    if subject.lower() == 'cancel':
        print(f'Cancelling...')
        speak('Cancelling.')
        return
    print(f'  >> Subject: {subject}')
    
    print("T.A.L.O.S>>> What is the message?")
    speak("What is the message?")
    message = take_user_input().capitalize()
    if message.lower() == 'cancel':
        print(f'Cancelling...')
        speak('Cancelling.')
        return
    
    # confirm = ''
    # while 'yes' not in confirm or 'confirmed' not in confirm:
    #     print("T.A.L.O.S>>> Are you sure you want to send this? ")
    #     speak("Are you sure you want to send this?")
    #     confirm = take_user_input().lower()
        
    #     if 'cancel' in confirm or \
    #         'exit' in confirm or \
    #         'no' in confirm:
    #         print(f'Cancelling...')
    #         speak('Cancelling.')
    #         return
    
    
    if send_email(receiver_address, subject, message):
        speak("I've sent the email.")
    else:
        speak("Im sorry sir, something went wrong while I was sending the mail. Please check the console for more information.")

def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL_ACCOUNT
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False


class EmailIntentError(Exception):
    """T.A.L.O.S>: EmailIntentError
    This is an exception for errors that might occur within this intent.
    Args:
        msg (str): Human readable string describing the exception.
        code (:obj:`int`, optional): Error code.
    Attributes:
        msg (str): Human readable string describing the exception.
        code (int): Exception error code.
    """

    def __init__(self, msg, code):
        self.msg = msg
        self.code = code

def main():
    """The main entrypoint for this module, when running from the command-line."""
    print(f'NOTE: There is no default functionality for this intent. Please use from an import.')


if __name__ == '__main__':
    main()