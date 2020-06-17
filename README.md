# Voice-Assistant
Voice assistant written in Python

## Current Voice Commands

### Basic Commands
* "What time is it?": Responds with the current time and date.
* "Search": Used for Google search. The response will be "What do you want to search for?".
* "Location": Used for Google Maps search. The response will be "What place are you looking for?".
* "Exit": Programs terminates. 

### "Workout" Command
Provides a random weight lifting workout specific to the provided muscle group. The response will be "What do you want to work on today?".
Simply respond with the desired muscle group. The program will list the workout, exercise by exercise (it will also print the exercises to 
the console), which consists of four randomly selected exercises from the specified muscle group. Muscle group commands include:
* Chest
* Back
* Shoulders
* Quadriceps
* Hamstrings
* Biceps
* Triceps

## Exercise Data
The exercises where obtained by web scraping the following website: https://www.aworkoutroutine.com/list-of-exercises-for-each-muscle-group/
The tool used for web scraping was [Parsehub](https://www.parsehub.com/)

## Dependencies
* pip install speechrecognition
* pip install pyaudio (http://people.csail.mit.edu/hubert/pyaudio/)
* pip install gTTS
* pip install playsound
* pip install PyObjC
* pip install requests
