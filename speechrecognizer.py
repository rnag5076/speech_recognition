import speech_recognition as sr
import webbrowser as wb
import pyttsx3
engine=pyttsx3.init()
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
while(1):
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('say something')
        audio=r.listen(source)
        print('done')

    try:
        text=r.recognize_google(audio)
        print('sexy thinks you said:\n'+r.recognize_google(audio))
        lang='en'
        engine.say(text)
        engine.runAndWait()
        f_text="https://www.google.co.in/search?q="+text
        wb.get(chrome_path).open(f_text)
    except Exception as e:
        print(e)
        
