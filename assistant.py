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

API_KEY = 'tOAT_LJ153Wb'
PROJECT_TOKEN = 'tc1GAbc7iYbD'

r = sr.Recognizer()

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

def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)

print('Listening...')
time.sleep(1)
speak('Hi, what can I help you with?')
while 1:
    voice_data = record_audio()
    respond(voice_data)