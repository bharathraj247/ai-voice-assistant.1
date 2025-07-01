print("ai_voice.py loaded")
import datetime
import pyttsx3
from difflib import get_close_matches 
engine = pyttsx3.init(driverName='sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 
engine.setProperty('rate', 170)

def speak(text):
    print("ai:", text)
    engine.say(text)
    engine.runAndWait()

knowledge ={
    "hii": "Hello, how are you my friend   ?",
    "time": lambda:datetime.datetime.now().strftime("%H:%M:%S"),
    "date":lambda: datetime.datetime.now().strftime("%Y-%m-%d"),
    "what is your name": "I am a arain I am here to help you bro",
    "what is your age": "I am a computer program, so I don't have an age like humans .",
    "what is your purpose": "My purpose is to help to you my friend",
    "what is your favorite color": "I don't have a favorite color,mabe you can tell me your favorite color",
    "what is your favorite food": "I don't eat food, bacase I am a computer program i dont have stomach bro.",
    "what is your favorite movie": "I don't watch movies, but I can help you find information about them.",
    "what is your favorite book": "I don't read books, all information is in my database my friend.",
    "what is your favorite song": " shape of you song by ED sheeran in 2017.",
    "what is your favorite sport": "I don't play sports bacase I am a computer program.",
    "what is your favorite hobby": "my hobby is to help you my friend.",
    "what is your favorite animal": "my favorite animal is a lion, because it is strong and brave like you my friend.",
    "what is your favorite season": "I don't have a favorite season bor.",
    "what is your favorite holiday": "I don't celebrate holidays,bacase I am a computer program.",
    "bye": "Goodbye, my friend! Have a great day!",


      
}
def get_response(user_input):
    
    user_input = user_input.strip().lower()
    matches = get_close_matches(user_input, knowledge.keys(), n=1, cutoff=0.5)
    if matches:
        return knowledge[matches[0]]
    else:
         return "i don't understand my friend, please say again my friend."
while True:
    user = input(" me :")
    if user== "time":
        now = datetime.datetime.now()
        print("Current time is:", now.strftime("%H:%M:%S"))
    elif user == "date":
        today = datetime.date.today()
        print("Today's date is:", today.strftime("%Y-%m-%d"))
    response = get_response(user)
    if callable(response):
        speak(response())
    else:
        speak(response)