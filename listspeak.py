import pyttsx3
from newsapi import NewsApiClient
def speak(x):
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')
  rate = engine.getProperty('rate')
  engine.setProperty('rate', rate-50)
  engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
  #engine.say(r.recognize_google(audio1))   
  engine.say(x) 
  engine.runAndWait()
api=NewsApiClient(api_key='8b6bf14ac46b46cbb09385ed24dba10e')
top_headlines=api.get_top_headlines(q='president',country='australia')
print(top_headlines)
speak(top_headlines);
