
import time
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib as s
from wikipedia import exceptions
import pyautogui
import requests
import json
import pyaudio
#  Apna voice assistant rakesh

os.chdir(r'C:\Users\kingd\OneDrive\Desktop\rakeshfiles')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    """These function wish with hour time"""
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
        engine.runAndWait()
    speak("I am rakesh sir. Please tell me how many I help you")

def takeCommand():
    """This function are take voice and give a string of your sentance"""
    r = sr.Recognizer()
    # my_mic = sr.Microphone(device_index=1) 
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 0.5
        r.energy_threshold = 300
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print(r.recognize_google(audio))
    try:
        print("Recognizing..")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say again please...")
        return "None"
    return query

def sendmail(subject,body,to):
    """"This funtion is send mail to other"""
    with open("C:\\boss\\New folder\\pass.txt","r") as e:
        emailpass = e.read()
    ob = s.SMTP("smtp.gmail.com",587)
    ob.starttls()
    ob.login("bsdkterabaaphuprashant@gmail.com",emailpass)
    message= f"Subject:{subject}\n\n{body}"
    ob.sendmail("bsdkterabaaphuprashant",to,message)
    ob.quit()

if __name__ =="__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if "rakesh open google" in query:
            webbrowser.open("www.google.com")


        elif "rakesh quit" in query:
            exit()


        elif "rakesh open youtube" in query:
            webbrowser.open("www.youtube.com")


        elif "rakesh time kya hua hai" in query or "rakesh what the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, time is {strtime}")


        elif "good job rakesh" in query or "rakesh very good" in query or "rakesh good job" in query or "bahut sahi rakesh" in query:
            speak("thank you sir")


        elif "tell yourself" in query or "what is your name voice assistant" in query:
            rakesh = ["Sir, I am rakesh your desktop assistant","I am rakesh sir"," i am your assistant sir"]
            import random
            choice = random.choice(rakesh)
            speak(choice)


        elif "on wikipedia" in query: 
            speak('Searching wikipedia...')
            query = query.replace("on wikipedia","")
            try:
                results = wikipedia.summary(query,sentences=2)
            except exceptions as e:
                speak("Something went worng try again")
            print(results)
            speak("According to wikipedia")
            speak(results)


        elif "open vs code" in query:
            codepath = "C:\\Users\\prash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)


        elif "send email to prashant" in query:
            try:
                speak("What the subject of your email")
                sub = takeCommand()
                speak("what should say sir")
                contant = takeCommand()
                to = "prashantsainiiftm@gmail.com"
                print(f"Your email subject are \n{sub}")
                print(f"Your email massage are \n{contant}")
                speak("Say confirm for send your email")
                confirm = takeCommand()

                if "confirm" in confirm:
                    sendmail(sub,contant,to)
                    speak("Email has been sent!")
                else:
                    speak("your email are cancel")
            except exceptions as e:
                speak("Soory sir, I am not able to send this email")


        elif "rakesh search on google" in query :
            try:
                from googlesearch import search
            except ImportError:
                print("No module named 'google' found")
 
            # to search
            speak("sir, tell something for search")
            query = takeCommand()
            for j in search(query, tld="co.in", num=10, stop=1, pause=1):
                query = j
                break
            webbrowser.open(query)


        elif "search on youtube" in query:
            query =  query.replace("search on youtube","")
            url = 'https://www.youtube.com/results?q=' + query
            webbrowser.open(url)


        elif "rakesh open whatsapp" in query or "rakesh open my whatsapp acount" in query:
            webbrowser.open("https://web.whatsapp.com/")


        elif "what your creator name" in query or "rakesh who made you" in query:
            with open("C:\\boss\\New folder\\owner_name.txt","r") as e:
                owner = e.read()

            speak(f"i created by {owner} sir")


        elif "rakesh shutdown computer" in query or "rakesh shutdown this computer" in query or "rakesh shutdown-computer" in query:
            speak("Say confirm for shutdown your computer")
            shut = takeCommand()
            if shut=='confirm':
                os.system("shutdown /s /t 1")
            else:
                speak("soory sir you can't say confirm for shutdown computer")


        elif "rakesh open hackerrank" in query or "rakesh open my hackerrank id" in query:
            def hackerrank():
                with open("C:\\boss\\New folder\\hacker.txt","r") as e:
                    usernameh = e.readline()
                    passh = e.readline()
                webbrowser.open("https://www.hackerrank.com/auth/login")
                time.sleep(5)
                for i in range(3):                  
                    pyautogui.press('tab')
                pyautogui.write(usernameh)
                time.sleep(1)
                pyautogui.press('tab')
                pyautogui.write(passh)
                time.sleep(1)
                pyautogui.press('enter')
            hackerrank()


        elif "rakesh restart-computer" in query or "rakesh restart this computer" in query or "rakesh restart computer" in query:
            speak("Say confirm for restart your computer")
            shut = takeCommand()
            if shut=='confirm':
                os.system("shutdown /r /t 1")
            else:
                speak("soory sir you can't say confirm for shutdown computer")


        elif "rakesh today news report" in query or "rakesh speak today news" in query:
            speak("News for today.. Lets begin")
            url = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=4616b60d62da49c2a64d1a9e300256d9"
            news = requests.get(url).text
            news_dict = json.loads(news)
            arts = news_dict['articles']
            for article in arts:
                speak(article['title'])
                speak(article['description'])
                print(article['title'])
                print(article['description'])
                speak("Moving on to the next news..Listen Carefully")

            speak("Thanks for listening...")

            


        elif "rakesh sleep" in query or "rakesh go offline" in query:
            speak("ok sir, say rakesh restart for restart me")
            while True:
                query = takeCommand().lower()
                if "rakesh restart" in query:
                    wishme()
                    break
                elif "rakesh quit" in query:
                    exit()
        
        # elif "rakesh open codewithharry python video" in query:
        #     speak("sir say no of video or can be play random")
        #     query = takeCommand()
        #     os.
        #     if query

        elif "change voice assistant owner name" in query or "rakesh i want change owner name" in query:
            speak("Sir say new owner name")
            query = takeCommand()
            speak("sir say conifrm for change owner name")
            con = takeCommand()
            if "confirm" in con:
                            with open("C:\\boss\\New folder\\owner_name.txt","w") as e:
                                owner = e.write(query)


        else:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            with open("feedback.txt","a") as ss:
                if "none" == query:
                    continue
                else:
                    ss.write(f"Time: {strtime} : This query are not avilable in your assistant : {query}\n")