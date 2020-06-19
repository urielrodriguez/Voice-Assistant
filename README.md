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

### "Nutrition" Command
Provides nutritional information on specific types of food. The first response will be "What type of food do you want nutritional information for?". Simply respond with the desired food group. The current food groups available are:
* Dairy 
* Meat
* Seafood
The second response will be "What specific *food group provided* product are you looking for?". Simply respond the the desired food. 
The current food products available are:
* Dairy: Whole cow milk
* Meat: Roasted Turkey
* Seafood: Canned Salmon

## Exercise Data
* The exercises where obtained by web scraping the following website: https://www.aworkoutroutine.com/list-of-exercises-for-each-muscle-group/
* The tool used for web scraping was [Parsehub](https://www.parsehub.com/)

## Nutrition Data
I created a small database using MySQL that contains all the nutrition data and decided to host is locally given its small size. Therefore, to use the 'nutrition' command, it is necessary to download MySQL. After, simply uncomment all the code related to the 
database, as well as the code pertaining to the actual command. The data for this function was obtained on the following website: 
https://en.wikipedia.org/wiki/Table_of_food_nutrients

## Dependencies
* pip install speechrecognition
* pip install pyaudio (http://people.csail.mit.edu/hubert/pyaudio/)
* pip install gTTS
* pip install playsound
* pip install PyObjC
* pip install requests
