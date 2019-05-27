import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('rate', 140)
#engine.setProperty('voice', voices[0].id)
engine.setProperty('voice', 'english+f1')
engine.setProperty('volume', 1)
engine.setProperty('female', voices[0].gender)
engine.setProperty(22, voices[0].age)

        


def speak(audio):
    print('Nemo: ' + audio)  # i add this line to print what bondo2 said
    engine.say(audio)
    engine.runAndWait()


def welcome_message():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("My name is Nemo. How may I help you ?")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"You : {query}\n")
    # except sr.UnknownValueError :
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('khaledmostafa297@gmail.com', '01143325016')
    server.sendmail('khaledmostafa297@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    welcome_message()
    while True:
        
        while True :
            query = takeCommand().lower()
            if (query != "None") :
                break
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)


        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                #speak("Who is the recipient ?")
                #to = takeCommand()
                to = "Khalidgad23@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent successfully !")
            except Exception as e:
                print(e)
                speak("Sorry ,I am not able to send this email")

        else:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak(results)
