import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
import requests
import json
import random
import mysql.connector

#######################################
# NUTRITION DATA / DATABASE (MYSQL) 
#######################################

db = mysql.connector.connect(
    host='',
    user='',
    passwd='',
    database=''
)

mycursor = db.cursor()

#######################################
# MAIN VARIABLES
#######################################

API_KEY = ''
PROJECT_TOKEN = ''

r = sr.Recognizer()

#######################################
# WORKOUT DATA (WEB SCRAPING)
#######################################

class Workout:
    def __init__(self, api_key, project_token):
        self.api_key = api_key
        self.project_token = project_token
        self.params = { 'api_key' : self.api_key }
        self.get_data()

    def get_data(self):
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data', params={'api_key':API_KEY})
        self.data = json.loads(response.text)

    def get_exercises(self, muscle_group):
        exercises = []
        for group in self.data['musclegroups']:
            if muscle_group in group['group'].lower():
                exs = group['exercises']
        for exercise in exs:
            exercises.append(exercise['exercise'])
        return exercises

    def get_workout(self, muscle_group):
        exercises = self.get_exercises(muscle_group)
        random.shuffle(exercises)
        workout = []
        for i in range(4):
            workout.append(exercises[i])
        return workout

#######################################
# NUTRITION COMMAND HELPER METHOD
#######################################

def get_nutrient(i):
    if i == 3:
        return 'calories'
    if i == 4:
        return 'protein'
    if i == 5:
        return 'carbohydrates'
    if i == 6:
        return 'fiber'
    if i == 7:
        return 'fat'
    if i == 8:
        return 'saturated fat'

#######################################
# VOICE ASSISTANT METHODS
#######################################

def record_audio(ask=False):
    with sr.Microphone() as mic:
        if ask:
            speak(ask)
        audio = r.listen(mic)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Sorry, I did not get that')
        except sr.RequestError:
            speak('Sorry, my speech service is not working')
    return voice_data

def respond(voice_data):
    print('You said: ' + voice_data)
    if 'what time is it' in voice_data:
        speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        print('You said: ' + search)
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('Here is what I found for ' + search)
    if 'location' in voice_data:
        location = record_audio('What place are you looking for?')
        print('You said: ' + location)
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        speak('Goodbye')
        exit()
    if 'workout' in voice_data:
        muscle = record_audio('What do you want to work on today?')
        print('You said: ' + muscle)
        data = Workout(API_KEY, PROJECT_TOKEN)
        workout = data.get_workout(muscle)
        speak('Here is your ' + muscle + ' workout')
        for exercise in workout:
            speak(exercise)
            print(exercise)
        speak('Have a great workout!')
    if 'nutrition' in voice_data:
        food_group = record_audio('What type of food do you want nutritional information for?')
        if food_group == 'meet':
            food_group = 'meat'
        print('You said: ' + food_group)
        food = record_audio('What specific ' + food_group + ' product are you looking for?')
        print('You said: ' + food)
        query = "SELECT * FROM " + food_group + " WHERE food = '" + food + "'"
        mycursor.execute(query)
        speak('Here are the nutritional facts for ' + food)
        print('Here are the nutritional facts for ' + food)
        for x in mycursor:
            speak(x[1] + ' or ' + str(x[2]) + ' grams of ' + food + ' contains:')
            print(x[1] + ' or ' + str(x[2]) + ' grams of ' + food + ' contains:')
            for i in range(3, 9):
                nutrient = get_nutrient(i)
                if i == 3:
                    speak(str(x[i]) + nutrient)
                    print(str(x[i]) + nutrient)
                elif i == 8:
                    speak('and ' + str(x[i]) + ' grams of ' + nutrient) 
                    print('and ' + str(x[i]) + ' grams of ' + nutrient)
                else:   
                    speak(str(x[i]) + ' grams of ' + nutrient)
                    print(str(x[i]) + ' grams of ' + nutrient)

def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)

#######################################
# COMMAND LINE OUTPUT / LOOP
#######################################

print('Listening...')
time.sleep(1)
speak('Hi, what can I help you with?')
while 1:
    voice_data = record_audio()
    respond(voice_data)