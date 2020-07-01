#

# sudo apt-get update
# sudo apt update
# sudo apt install python3-pip
# pip3 install pyttsx3
# pip3 install chatterbot
# pip3 install SpeechRecognition
# python3 -m spacy download en
# sudo apt-get update && sudo apt-get install espeak
# sudo apt install libespeak1
# sudo apt install python3-pyaudio
# sudo apt install jackd2
# sudo apt install qjackctl




import pyttsx3
import configparser
import speech_recognition as sr
from configparser import ConfigParser
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('MOVI')
trainer = ListTrainer(bot)

# #### Loading and Training the ChatBot
separator = "="
with open('ChatbotTraining.properties') as f:
    for line in f:
        if separator in line:
            name, value = line.split(separator, 1)
            trainer.train([name, value])

# #### Converting Speech To Text
r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Please say something")
    audio = r.listen(source)
    print("Recognizing Now .... ")
    # Using sphinx API
    #voiceheard = r.recognize_sphinx(audio);
    
    # Using Google API
    voiceheard = r.recognize_google(audio);
    try:
        print("You have said: " + voiceheard)
    except Exception as e:
        print("Error :  " + str(e))

# #### Returning answer [as text] from the question [as speech]
speechResponse= bot.get_response(voiceheard)


# #### Converting Text To Speech
engine = pyttsx3.init() # object creation
ttsconfig = configparser.ConfigParser()
ttsconfig.read('TTS.properties')

""" RATE"""
rate = engine.getProperty('rate')    # getting details of current speaking rate
#print (rate)                        # printing current voice rate
engine.setProperty('rate', ttsconfig.get("TTS", "rate"))     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')    # getting to know current volume level (min=0 and max=1)
#print (volume)                          # printing current volume level
engine.setProperty('volume', ttsconfig.get("TTS", "volume")) # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       # getting details of current voice
#engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
engine.setProperty('voice', ttsconfig.get("TTS", "voices")) # changing index, changes voices. 1 for female

engine.say(speechResponse)
engine.runAndWait()
engine.stop()

# """Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
# engine.save_to_file('Hello World', 'test.mp3')
# engine.runAndWait()

