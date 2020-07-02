#===================UBUNTU========================
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

#================WIN|ANACONDA=====================
# pip3 install pywin32
# pip3 install pyttsx3
# pip3 install chatterbot
# pip3 install SpeechRecognition
# python3 -m spacy download en
# pip3 install pyaudio
#=================================================
import pyttsx3
import configparser
import speech_recognition as sr
from configparser import ConfigParser
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#Initializing ChatBot
bot = ChatBot('MOVP')


#Loading and Training the ChatBot
def loadAndTrainChatBot():
    trainer = ListTrainer(bot)
    separator = "="
    with open('ChatbotTraining.properties') as f:
        for line in f:
            if separator in line:
                name, value = line.split(separator, 1)
                trainer.train([name, value])


                
                
#Converting Speech To Text
def convertSpeechToText(): 
    r = sr.Recognizer() 
    audio = ''  
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please Speak...") 
        audio = r.listen(source, phrase_time_limit = 5)  
    try: 
        text = r.recognize_google(audio, language ='en-US') 
        print("You said: ", text) 
        return text 
    except: 
        convertTextToSpeech("Time our or I counn't hear properly") 
        return 0                
                

        

#Drive Speech To Text
def executeSpeechToText():
    while(1): 
        text = convertSpeechToText() 
        if text == 0: 
            continue
        if "exit" in str(text) or "bye" in str(text): 
            convertTextToSpeech("Thank you for using the Application") 
            break
        botresponse= bot.get_response(text)
        convertTextToSpeech(botresponse) 




#Converting Text To Speech
def convertTextToSpeech(speechResponse):
    engine = pyttsx3.init()
    ttsconfig = configparser.ConfigParser()
    ttsconfig.read('TTS.properties')

    """ RATE"""
    rate = engine.getProperty('rate')    
    engine.setProperty('rate', ttsconfig.get("TTS", "rate"))     # setting up new voice rate

    """VOLUME"""
    volume = engine.getProperty('volume')
    engine.setProperty('volume', ttsconfig.get("TTS", "volume")) # setting up volume level  between 0 and 1

    """VOICE"""
    voices = engine.getProperty('voices')     
    #engine.setProperty('voice', voices[0].id)  # voices[0].id for male
    engine.setProperty('voice', voices[int(ttsconfig.get("TTS", "voices"))].id) # voices[1].id for female

    engine.say(speechResponse)
    engine.runAndWait()
    engine.stop()




#Driver
def main():
    loadAndTrainChatBot()
    executeSpeechToText()

if __name__ == "__main__":
    main()    

