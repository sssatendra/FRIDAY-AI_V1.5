# FRIDAY AI Virtual assistance by Satendra Kumar R, Feel free to use this code. If you have any inputs to add in this program, then please let me know @ sssatendra51@gmail.com
# my LinkedIn profile @  satendra-kumar-006795148
# 

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random
import requests
import pyjokes
import time
import wolframalpha
from googlesearch import search
from pygame import mixer
# from weather import Weather



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def searchOnGoogle(query, outputList): 
   speak("The top five search results from Google are listed below.")
   for output in search(query, tld="co.in", num=10, stop=5, pause=2):
      print(output) 
      outputList.append(output) 
   return outputList 

#opens the link in the google search results
def openLink(outputList): 
    speak("Here you go")
    if 'yes' in query or 'sure' in query:
        webbrowser.open(outputList[0])

    elif 'second' in query:
       webbrowser.open(outputList[1])

    elif 'third' in query:
       webbrowser.open(outputList[2])

    elif 'fourth' in query:
       webbrowser.open(outputList[3])

    elif 'fifth' in query:
       webbrowser.open(outputList[4])


# start with wishing the user
def wishMe():
    hour = int(datetime.datetime.now().hour)
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    if hour>=0 and hour<12:
        speak(f"Good Morning! its {strTime} and weather in Banaglore is 22 degree celcius")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon! its {strTime} and weather in Banaglore is 22 degree celcius")

    else:
        speak(f"Good Evening! its {strTime} and weather in Banaglore is 22 degree celcius")

    speak("Hi SAM, This is Friday. Version 1 point 5 loaded with wolfarm alpha.  How may i assist you today")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening to you dear...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Analyzing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        speak("Sorry, please say that again...")
        print("Sorry, please say that again...")
        return takeCommand()

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your Email', 'your password')
    server.sendmail('your email', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query or 'who is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'thank' in query:
            print('Glad to help you\n')
            speak("Glad to help you")
            exit()

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
    

        elif 'search' in query:            
            outputList = []
            #speak('What should I search for ?')
            #query = takeCommand() 
            query=query.replace("search", " ")           
            searchOnGoogle(query, outputList)
            speak("Should I open up the first link for you ?")
            query = takeCommand()
            if 'yes' or 'sure' in query:
                openLink(outputList)
            elif 'second' in query:
                openLink(outputList)
            elif 'Third' in query:
                openLink(outputList)
            elif 'fourth' in query:
                openLink(outputList)
            elif 'fifth' in query:
                openLink(outputList)
            if 'no' in query:
                speak('Alright.')

        elif 'play prime' in query  or 'amazon prime' in query:
            webbrowser.open('primevideo.com')

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack'  in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query or 'play songs' in query or 'play the music' in query or 'play the songs' in query:
            music_dir = 'G:\\Music\\'
            music = os.listdir(music_dir)
            random_music = music_dir + random.choice(music) 
            mixer.init() 
            mixer.music.load(random_music) 
            mixer.music.play()
            #while mixer.music.get_busy() == True:
                #continue
            # USE THE ABOVE LOOP IF YOU DONT WANT ANY INTERUPTIONS WHILE THE MUSIC IS RUNNING
            # AND IF YOU WANT THE FRIDAY TO WAIT FOR THE NEXT QUERY UNTIL THE MUSIC IS FINISHED
                

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
        
        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by Satendra.")

        elif 'stop the music' in query or 'stop music' in query or 'stop the song' in query or 'stop song' in query:
            mixer.music.stop() 
            speak('The music is stopped.')
            

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'news' in query:
             
            try: 
                jsonObj = urlopen('''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))

        elif "where is" in query:
            query = query.split(" ")
            location = query[2]
            speak("Hold on Sam, I will show you where " + location + " is.")
            webbrowser.open("https://www.google.nl/maps/place/" + location + "/&amp;")

        elif "will you be my gf" in query or "will you be my bf" in query:   
            speak("I love you too, as a friend")
 
        elif "how are you" in query:
            speak("I'm fine, glad you me that")
 
        elif "i love you" in query:
            speak("It's hard to understand")

        elif "calculate" in query or "what is"in query:
            client = wolframalpha.Client("YOUR API KEY HERE FROM WOLFRAMALPHA")
            res = client.query(query)
            if res['@success']=='true':
                pod0=res['pod'][0]['subpod']['plaintext']
                print(pod0)
                pod1=res['pod'][1]
                if (('definition' in pod1['@title'].lower()) or ('result' in  pod1['@title'].lower()) or (pod1.get('@primary','false') == 'true')):
                    result = pod1['subpod']['plaintext']
                    print(result)
                    speak(result)
                    
                else:
                    speak("No answer returned")
                    print("No answer returned")


        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
 
        elif "who are you" in query:
            speak("I am your virtual assistant created by Mr Kumar")
 
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mr Kumar ")
 

        elif 'stop' or "exit" in query:
            print('Thank you for your precious time')
            speak('Thank you for your precious time')
            exit()

        elif 'weather' in query:
            api_address='http://api.openweathermap.org/data/2.5/weather?appid=Your_API_KEY'
            city = query.replace("weather in", " ")
            url = api_address+city
            json_data = requests.get(url).json()
            format_add = json_data['base']
            print(format_add)
            speak(format_add)
        
        

        

        
        
