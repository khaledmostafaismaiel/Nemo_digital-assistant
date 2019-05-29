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

        
def say_my_name():

#this loop while break if you said nemo in query for called "Nemo assistant" and privent it from searching in every word lestining for it 
    while True:
        query = takeCommand().lower()
        if ('rose' in query):    
            speak('yes sir')
            break

def speak(audio):
    print('Rose: ' + audio)  # i add this line to print what bondo2 said
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

    speak("My name is Rose. How may I help you ?")


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

        say_my_name()
        
        # Logic for executing tasks based on query
        query = takeCommand().lower()

        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)


        elif (('open' in query)and('youtube' in query)):
            webbrowser.open('https://www.youtube.com', new=0, autoraise=False)

        elif (('open' in query)and('google' in query)):
            webbrowser.open('https://www.google.com', new=0, autoraise=False)

        elif (('open' in query)and('stack over flow' in query)):
            webbrowser.open('https://stackoverflow.com/', new=0, autoraise=False)

        elif (('open' in query)and('linkedin' in query)):
            webbrowser.open('https://www.linkedin.com/in/khaled-mostafa-414265bb/', new=0, autoraise=False)

        elif (('open' in query)and('github' in query)):
            webbrowser.open('https://github.com/khaledmostafaismaiel', new=0, autoraise=False)

        elif (('open' in query)and('facebook' in query)):
            webbrowser.open('https://www.facebook.com/khaled.asfora.7', new=0, autoraise=False)

        elif (('open' in query)and('instagram' in query)):
            webbrowser.open('https://www.instagram.com/', new=0, autoraise=False)

        elif (('open' in query)and('whatsapp' in query)):
            webbrowser.open('https://web.whatsapp.com/', new=0, autoraise=False)

        elif (('open' in query)and('gmail' in query)):
            webbrowser.open('https://mail.google.com', new=0, autoraise=False)

        elif (('open' in query)and('translate' in query)):
            webbrowser.open('https://translate.google.com', new=0, autoraise=False)

        elif (('open' in query)and('drive' in query)):
            webbrowser.open('https://drive.google.com/drive/my-drive', new=0, autoraise=False)

        elif (('open' in query)and('ever note' in query)):
            webbrowser.open('https://www.evernote.com/client/web#?an=true&n=a28be6fe-bd4b-41e6-84aa-e6fe500444e5&s=s669&/', new=0, autoraise=False)
        
        elif (('open' in query)and('quraan' in query)):
            webbrowser.open('https://www.youtube.com/watch?v=2rx0DYOex1c', new=0, autoraise=False)

        elif (('open' in query)and('programiz' in query)):
            webbrowser.open('https://www.programiz.com/', new=0, autoraise=False)
    
        elif (('open' in query)and('songs' in query)):
            webbrowser.open('https://www.youtube.com/watch?v=sG9mZWOqgFc&list=RDsG9mZWOqgFc&start_radio=1&pbjreload=10', new=0, autoraise=False)
            speak('Enjoy !')

        elif 'music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            speak('Enjoy !')
            os.startfile(os.path.join(music_dir, songs[0]))
            '''
            music_dir = 
            music = ['amr diab','asala']
            random_music = music + random.choice.(music)+ '.mp3' 
            speak('Enjoy !')
            os.system(random_music)
            '''
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath = "bin/code"
            os.startfile(codePath)

        elif 'open pycharm' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif ((('abort' in query) and ('please' in query))or(('stop' in query) and ('please' in query)) \
             or (('shut down' in query) and ('please' in query))or(('turn off' in query) and ('please' in query))):
            speak('Ok ,bye , see you later .')
            break

        elif ((('your' in query) and ('functions' in query))or(('your' in query) and ('functionality' in query)) \
            or(('your' in query) and ('function' in query))or(('your' in query) and ('functionalities' in query))):
            speak('i can open youtube')
            speak('i can open google')
            speak('i can open whats app')
            speak('i can open instagram')
            speak('i can open gmail')
            speak('i can open facebook')
            speak('i can open github')
            speak('i can open stack over flow')
            speak('i can open ever note')
            speak('i can open google drive')
            speak('i can open songs on youtube')
            speak('i can open programiz')
            speak('i can open quraan on youtube')
            speak('i can open google translation')            
            speak('i can open music directory')            
            speak('i can tell the time')            
            speak('i can open visual code stdio directory')            
            speak('i can open pycharme directory')            
            speak('i can send e mails')            
            speak('i can search about every thing')
            speak('i can turn off my self')            

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
