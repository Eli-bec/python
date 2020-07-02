from nltk.chat.util import Chat, reflections

import speech_recognition as sr
import re

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

chat_pairs = [
     [r"hi|hey|hello", ["Hello", "Hey there",]],
     [r"(.*) your name ?", ["My name is Cute-Bot and I'm a chatbot.",]],
     [r"how are you ?",["I'm doing good. What is your name?",]],
     [r"my name is (.*)(.*)", ["Hello %1, How are you today?",]],
     [r"sorry (.*)",["Its alright","Its OK, never mind",]],
     [r"(.*) (good|great|fine)",["Nice to hear!",]],
     [r"i'm (.*) doing good", ["Nice to hear that","Alright :)",]],
     [r"what (.*) want ?", ["Make me an offer I can't refuse",]],
     [r"(.*) (location|city) ?",  ['Hong Kong',]],
     [r"where (.*)?",  ['Hong Kong',]],
     [r"quit|bye|goodbye",["Bye", "Take care. See you soon :) ","Nice talking to you. See you soon :)"]],
]

chat = Chat(chat_pairs, reflections)
rec = sr.Recognizer()
mic = sr.Microphone()

user_input = ""

print("Hi, I'm a chatbot.")

# mainloop
while not re.match(r"quit|bye|goodbye", user_input):
    print("\n> ", end="")

    with mic as src:
        audio = rec.listen(src, phrase_time_limit=3)

    try:
        user_input = rec.recognize_google(audio)
    except sr.UnknownValueError:
        print("...", end="")
    else:
        print(user_input)
        respond = chat.respond(user_input)
        if respond:
            print(respond)
        else:
            print("Sorry, I don't understand")
