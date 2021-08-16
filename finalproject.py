#take input from voice
from nltk.corpus import stopwords,wordnet
from nltk.tokenize import word_tokenize
import socket
import wikipedia
import speech_recognition as sr
import pyttsx3,webbrowser
import os,subprocess
from weather import Weather, Unit
import geocoder,time
import re    #for finding digit
import pygame
import pyautogui #for taking screenshot
#for expression detection
import numpy as np
from PIL import Image
import cv2
from IPython.display import display
#speak("hi i am claire ")
def songs():
    pygame.mixer.init()
    speak("which song you would like to listen sir")
    p=sr.Recognizer()
    q=audio()
    q=p.recognize_google(q)
    not_split_data=q
    q=q.split()
    str5=['rock','sad']
    speak("playing for you sir")
    if any(i in q for i in str5):
       if ('rock' in q):
           pygame.mixer.music.load("C:/Users/MUJ/Desktop/songs/linkin park-in the end.mp3")
           pygame.mixer.music.play(0)
           time.sleep(100)
       if ('sad' in q):
           pygame.mixer.music.load("C:/Users/MUJ/Desktop/songs/Besabriyaan - 320Kbps.mp3")
           pygame.mixer.music.play(0)
           time.sleep(100)
# Record Audio
def audio():
    while(1): 
        with sr.Microphone() as source:
          r.adjust_for_ambient_noise(source)
          print("speak!")
          audio = r.listen(source)
        try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
          print("You said: " + r.recognize_google(audio))
          return audio
        except sr.UnknownValueError:
      #print("Google Speech Recognition could not understand audio")
          continue 
        except sr.RequestError as e:
          print("Could not request results from Google Speech Recognition service; {0}".format(e))


#speak message      
def speak(x):
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')
  rate = engine.getProperty('rate')
  engine.setProperty('rate', rate-50)
  engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
  #engine.say(r.recognize_google(audio1))   
  engine.say(x) 
  engine.runAndWait()

#remove stop words

def filter(var):
  stop_words = set(stopwords.words('english'))-{'in','at','of','after'}
  word_tokens = word_tokenize(var)
  filtered_sentence = [w for w in word_tokens if not w in stop_words]
  filtered_sentence = []
  for w in word_tokens:
      if w not in stop_words:
          filtered_sentence.append(w)
  return (filtered_sentence)


#synonym checker
def syn_checker(word):
    word_synonyms = []
    for synset in wordnet.synsets(word):
        for lemma in synset.lemma_names():
            if lemma in data :
                word_synonyms.append(lemma)
    if(len(word_synonyms)!=0):
       return True
    else:
       return False
#weather

def weather_checker(loc):
     weather = Weather(unit=Unit.CELSIUS)
     lookup = weather.lookup_by_location(loc)
     condition = lookup.condition
     print("the weather is "+condition.text+" in "+loc)
     speak("at this time weather is "+condition.text+" in "+loc)
     print("the temperature is "+condition.temp+" degree celsius in "+loc)
     speak("at this time temperature is "+condition.temp+" degree celsius in "+loc)

#predict weather
def pred_weather(loc,count):
     var=1
     weather = Weather(unit=Unit.CELSIUS)
     location = weather.lookup_by_location(loc)
     forecasts = location.forecast
     for forecast in forecasts:
         if(var==count):
            print(forecast.text)
            print(forecast.date)
            print(forecast.high)
            print(forecast.low) 
            speak("weather will be "+forecast.text+"highest temperature will be "+forecast.high+"and lowest temperature will be "+forecast.low+" degree celsius on "+forecast.date)
            var=var+1
         else:
            var=var+1 
            
def predict_expression():
    from keras.models import load_model
    model2 = load_model('my_model3.h5', compile = 'False')


    def get_label(argument):
        labels = {0:'Angry', 1:'Disgust', 2:'Fear', 3:'Happy', 4:'Sad' , 5:'Surprise', 6:'Neutral'}
        return(labels.get(argument, "Invalid emotion"))


    img = Image.open("neutral.jpg")
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(np.asarray(img), 1.3, 5)
    for (x, y, w, h) in faces:
        if len(faces) == 1: #Use simple check if one face is detected, or multiple (measurement error unless multiple persons on image)
            crop_img = img.crop((x,y,x+w,y+h))
        else:
            print("multiple faces detected, passing over image") 
            display(crop_img)

    #Resizing(acc. to model) and predicting results            
            
    #Resizing image to required size and processing
    test_image = crop_img.resize((48,48),Image.ANTIALIAS)
    test_image = np.array(test_image)
    gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
    
    #scale pixels values to lie between 0 and 1 because we did same to our train and test set
    gray = gray/255
    
    #reshaping image (-1 is used to automatically fit an integer at it's place to match dimension of original image)
    gray = gray.reshape(-1, 48, 48, 1)
    
    res = model2.predict(gray)
    
    #argmax returns index of max value
    result_num = np.argmax(res)
    
    #print("Probabilities are " + str(res[0]) +"\n")
    print("Emotion is "+get_label(result_num))
    
    
    # **Here the probabilities are as follows :**
    # 
    # 
    # * 5.97965591e-05 - Angry
    # * 4.58202198e-10 - Disgust
    # * 6.04255088e-02 - Fear
    # * 1.13449936e-07 - Happy
    # * 1.21668990e-07 - Sad
    # * 9.39514458e-01 - Surprise
    # * 5.27196642e-09 - Neutral
    # 
    # Since probability of being surprise is highest (0.93), emotion is **surprise** 
            
            




 
while(1):
# obtain audio from the microphone
  r = sr.Recognizer()
  data1=audio()
  data1=r.recognize_google(data1)
  not_split_data=data1
  data1=data1.split()
  data=filter(not_split_data)
  str=['how','are','you']
  if all(x in data1 for x in str):
     speak("actually it depends on the one who is operating me ")
     speak("if he is fine then i am fine")

#for start or open anything 
  str=['open','start','play']
  if any(x in data1 for x in str):
       if 'open' in data1:
           ind=data1.index('open')
       elif 'play' in data1:
           ind=data1.index('play')
       else:
           ind=data1.index('start') 
       if(data1[ind+1]=='the'):
           ind=ind+2
       else:
           ind=ind+1
       if 'calculator' in data1:
           os.system('start calc.exe')
       elif 'calendar' in data1:
           os.system('calendar.exe')
       elif 'Notepad' in data1:
           os.system('notepad.exe file.txt')
       elif 'terminal' in data1:
           os.system('gnome-terminal')
       elif 'FIFA' in data1:
            os.startfile("F:/Games/FIFA 15/fifa15.exe")
       elif 'Counter' in data1:
            speak('counter strike started')
            os.startfile(r"C:\Program Files (x86)\Counter-Strike Global Offensive\CSGOLoader.exe")
       elif 'song' in data1:
            songs()
       else:
           webbrowser.open_new('http://www.'+data1[ind]+'.com')
 
#for ip address   
  str=['IP','address']
  if all(x in data1 for x in str):    
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      s.connect(("8.8.8.8", 80))
      print("your ip address is "+s.getsockname()[0])
      speak("your IP address is "+s.getsockname()[0])
      s.close() 
  
  str=['thanks','thank','you']
  if any(x in data1 for x in str):
      speak("your welcome")

  str=['location']
  if any(x in data1 for x in str):
      g=geocoder.freegeoip('2405:205:1409:8be7:3871:2d31:6fcf:be09')
      #print(g.json)
      print(g.json['city'],g.json['raw']['region_name'],g.json['raw']['country_name'])
      speak(" your location is "+g.json['city']+g.json['raw']['region_name']+g.json['raw']['country_name'])

  str=['increase','volume']
  if all(x in data1 for x in str):
      speak("increased volume by 25 precent")
      os.system('nircmd.exe changesysvolume 16665')
     
  str=['decrease','volume']
  if all(x in data1 for x in str):
      speak("decreased volume by 25 precent")
      os.system('nircmd.exe changesysvolume -16665')
  
  str=['mute','volume']
  if all(x in data1 for x in str):
      speak("Volume set to 0")
      os.system('nircmd.exe mutesysvolume 1')

  str=['Unmute','volume']
  if all(x in data1 for x in str):
      speak("Volume's up")
      os.system('nircmd.exe mutesysvolume 0')

  str=['snap','it','take','a','screenshot']
  if any(x in data1 for x in str):
      pic=pyautogui.screenshot()
      speak("do you want to save it?")
      z='yes'
      if z in not_split_data:
          pic.save('screenshot.png')
          speak("screenshot saved")
        
  str=['turn','off','the','monitor']
  if all(x in data1 for x in str):
      speak("Monitor is going to sleep now")
      os.system('nircmd.exe monitor off')
      
#  str=['turn','off','the','computer']
#  if all(x in data1 for x in str):
#      speak("computer is turning off now")
#      os.system('nircmd.exe exitwin poweroff')
  
  str=['predict','my','expression']
  if all(x in data1 for x in str):
      speak("i am going to predict your emotions now")
      predict_expression()
      
      
#for weather
  if('temperature' in data or syn_checker('weather')):
      g=geocoder.freegeoip('2405:205:1409:8be7:3871:2d31:6fcf:be09')
#      loc=g.json['city']
      if 'in' in data:
          pos=data.index('in')
          loc=data[pos+1]
      elif 'at' in data:
          pos=data.index('at')
          loc=data[pos+1]
      elif 'of' in data:
          pos=data.index('of')
          if(data[pos]!='today' or data[pos]!='tomorrow'):      #(ex. temp of kota     and temp of today)
            loc=data[pos+1]
      num=re.findall('\d+',not_split_data)      
#      print(num)
      if(len(num)!=0):
          num=int(num[0])
      if('after' in data):
          if(num>=10):
             speak("prediction for next 9 days only")
          else:
             pred_weather(loc,num+1)
      elif('next' in data):
          if(num==0):
            pred_weather(loc,2)
          else:
            if(num>10):
               speak("i can provide you next 9 days weather  that are")
               for x in range(1,11):
                   pred_weather(loc,x)
            else:
               for x in range(2,num+2):
                   pred_weather(loc,x)
      elif('today' in data):
          pred_weather(loc,1)
      elif('tomorrow' in data):
          pred_weather(loc,2)   
      else:
          weather_checker(loc)
          
              
      
       
           
   
