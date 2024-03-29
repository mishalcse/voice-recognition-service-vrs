import speech_recognition as sr
import webbrowser as wb

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
from gtts import gTTS

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from pygame import mixer
mixer.init()
while (True == True):

  r = sr.Recognizer()
  with sr.Microphone() as source:
  
    r.adjust_for_ambient_noise(source, duration=1)
    print("Say something!")
    audio = r.listen(source,phrase_time_limit=5)

  try:
    
    response = r.recognize_google(audio)
    print("you have said '" + response + "'")
    tts = gTTS(text="you said "+str(response), lang='bn')
    tts.save("response.mp3")
    mixer.music.load('response.mp3')
    mixer.music.play()
    f_response = 'https://www.google.co.in/search?q=' + response
    wb.get(chrome_path).open(f_response)
    
    
  except sr.UnknownValueError:
    print("Sphinx could not understand audio")
  except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
