import speech_recognition as sr
import pyttsx3
import pywhatkit as pwk
import wikipedia 
import datetime
import pyjokes
import pyautogui as pg
import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.runAndWait()
listener = sr.Recognizer()

numbers = {
    'sofi': '+34635846377',
    'sophia': '+34635846377',
    'sophie': '+34635846377',
    'myself': '+584246501227',
    'diego': '+584146890212',
    'jesus':'+584246450016'
}

groups={
    'friends':'CAOqVn5yGhWKpaFVhbUhhZ'
}


def command_input():
    
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source, timeout=5, phrase_time_limit=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            return command
    except:
        print("error")


def run():
    talk('Hello, what can I do for you?') 
    command = command_input()

    if'how are you' in command:
        talk('I cant have feelings because i am an artificial intelligence but I am fine, thank you for asking')

    elif 'what is your name' in command:
        talk('My name is John, what is yours?')
        name = command_input()
        talk('Nice to meet you' + name)

    elif 'play' in command:
        song = command.replace('play', '')
        talk('Looking for' + song + 'on youtube')
        pwk.playonyt(song)

    elif 'your creator' in command or 'created you' in command or 'programmed you' in command:
        talk('I was created by Victor Kneider')
    
    elif 'send whatsapp message'in command or 'whatsapp message' in command:
        talk('What is the message?')
        message = command_input()
        talk('Do you want to deliver the message to a person or a group?')
        verify = command_input()
        if 'person' in verify:
            talk('To who are you sending it to?')
            number = command_input()
            pwk.sendwhatmsg_instantly(numbers[number], message,10)
        else:
            talk('To which group are you sending it to?')
            group = command_input()
            pwk.sendwhatmsg_to_group_instantly(groups[group], message,10)
        
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    
    elif('who is' in command):
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())
    

    elif 'crazy' in command:
        talk('Tell me the name of the person you want to send the messages to')
        person = command_input()
        message="hi " + person + " this is John"
        pwk.sendwhatmsg_instantly(numbers[person], message,10)
        for i in range(50):
            pg.write(message)
            pg.press('enter')

    elif 'bye' in command:
        talk('Goodbye')
        exit()
    
    elif 'dolar' in command or 'dollar' in command or 'bcv' in command:
        req = requests.get('https://www.bcv.org.ve/',verify=False)
        html_content = req.text
        soup = BeautifulSoup(html_content, "html.parser") 
        usd_value = soup.find_all('div', {'class': 'col-sm-6 col-xs-6 centrado'})[-1]
        usd_value=usd_value.text.strip().replace(',','.')
        usd_value=round(float(usd_value),2)
        talk(f'The price of the dollar based on the BCV exchange is {usd_value} Bolivares')
    
    

    talk('Do you want me to do something else?')
    answer = command_input()
    print(answer)
    if 'yes' in answer:
        run()
    else:
        talk('Ok, goodbye')


def talk(text):
    engine.say(text)
    engine.runAndWait()


run()



