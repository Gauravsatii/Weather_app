import requests
import json
import pyttsx3
city = input("enter the city")
url=f"https://api.weatherapi.com/v1/current.json?key=ba0c41fb61244ed1ac6212702242401&q={city}"

r=requests.get(url)

wdic=json.loads(r.text)
cel=wdic["current"]["temp_c"]

text_speech=pyttsx3.init()

text_speech.say(f"the cuurent temperature of {city} is {cel}")
text_speech.runAndWait()
