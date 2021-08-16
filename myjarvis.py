from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

def talkToMe(audio):
    print(audio)
    tts=gTTS(text=audio,lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')

def myCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('i am ready for your next command')
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)

    try:
        command=r.recognize_google(audio)
        print('you said:'+command+'/n')

    except sr.UnknownValueError:
        assistant(myCommand())

    return command

def assistant(command):

    if 'what\'s up' in command:
        talkToMe('chillin bro')
    if 'how are you' in command:
        talkToMe('i am fine')

talkToMe('i am ready for your command')

while(1):
    assistant(myCommand())
