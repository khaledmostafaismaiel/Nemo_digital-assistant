import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
#import wmi
import ctypes
import pyautogui
import random
from playsound import playsound
import time
import psutil



engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('rate', 140)
#engine.setProperty('voice', voices[0].id)
engine.setProperty('voice', 'english+f2')
engine.setProperty('volume', 1)
engine.setProperty('female', voices[0].gender)
engine.setProperty(22, voices[0].age)


remind_speech = 'global'





database_file_name = 'database.txt'
def write_in_database(speaker,sentence):
    fw=open(database_file_name,'a')
    fw.write(speaker + "...")
    fw.write(sentence + "\n")
    fw.close()



# Power Time Convert
def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%dhour, %02d minute, %02s seconds" % (hh, mm, ss)

def brightness(voice_note):
	if 'decrease ' in voice_note:
		print('ok listen.......')
		dec = wmi.WMI(namespace='wmi')
		methods = dec.WmiMonitorBrightnessMethods()[0]
		methods.WmiSetBrightness(30, 0)
	elif 'increase ' in voice_note:
		print('ok listen.......')
		ins = wmi.WMI(namespace='wmi')
		methods = ins.WmiMonitorBrightnessMethods()[0]
		methods.WmiSetBrightness(100, 0)

def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)



def say_my_name():

#this loop while break if you said nemo in query for called "Nemo assistant" and privent it from searching in every word lestining for it 
    while True:
        query = takeCommand().lower()
        if ('rosa' in query):    
            speak('yes sir')
            break

def speak(audio):
    print('Rosa: ' + audio)  # i add this line to print what bondo2 said
    engine.say(audio)
    engine.runAndWait()
    write_in_database("rosa",audio)

def welcome_message():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("My name is Rosa. How may I help you ?")


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
        print("You :" ,query)
    # except sr.UnknownValueError :
    except Exception as e:
        print("You :" ,e)
        print("Say that again please...")
        return "None"
    
    write_in_database("you",query)
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
    
while True :
        
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
    
        elif (('open' in query)and('songs' in query)) or (('open' in query)and('song' in query)):
            webbrowser.open('https://www.youtube.com/watch?v=hlznpxNGFGQ&list=RDhlznpxNGFGQ&start_radio=1', new=0, autoraise=False)
            speak('Enjoy !')
            '''

        elif 'music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            speak('Enjoy !')
            os.startfile(os.path.join(music_dir, songs[0]))
            '''
            '''

            music_dir = 
            music = ['amr diab','asala']
            random_music = music + random.choice.(music)+ '.mp3' 
            speak('Enjoy !')
            os.system(random_music)
            '''

        elif query == 'play music' or query == 'romantic bollywood music' or query == ' bollywood music':
            speak('Enjoy !')
            playsound('Main_Hoon_Saath_Tere.mp3')
            '''
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

            '''
        elif 'date' in query and 'today' in query:
            current_time = time.strftime("%d:%B:%Y:%A:%H:%M:%S")
            speak(current_time)

        elif 'the time' in query:
            speak('and time is' + time.strftime("%H %M %S"))

        elif 'day we are' in query:
            speak(time.strftime("%A"))

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
            speak('my creator try to develop a way to make me do some short talks with humans')

        elif (('ok google' in query) or ('hi google' in query) or ('hello google' in query)):
            speak('i am flatter, but google is not me. my name is rose if you forget it')
            
        elif (('ok siri' in query) or ('hi siri' in query) or ('hello siri' in query)):
            speak('i am flatter, but siri is not me. my name is rose if you forget it')

        elif (('ok alexa' in query) or ('hi alexa' in query) or ('hello alexa' in query)):
            speak('i am flatter, but alexa is not me. my name is rose if you forget it')

        elif (('i like you' in query) or ('i love you' in query) or ('you are better than ' in query)):
            speak('oh')
            speak('you just made my day')

        elif (('your best friend' in query) or ('your friend' in query)):
            speak('khaled is my best friend he is my creator.')

        elif (('you have boyfriend' in query) or ('you have a boyfriend' in query) \
            or ('you have boy friend' in query) or ('you in relationship' in query) or ('you in a relationship' in query)):
            speak('i think its complicated')

        elif 'will you marry me' in query:
            speak('i think its complicated , sorry i can\'t')

        elif 'who are you' in query or 'about yourself' in query:
            speak('iam rose and iam a digital assistant and i will be the smartest one as soon as posible,')
            speak('khaled mostafa is my creator and he start developing me at 15 5 2019')

        elif 'how are you' in query:
            speak('oh')
            speak('iam fine and you ! , how have you been')

        elif 'logout' in query:
            speak('ok')
            ctypes.windll.user32.LockWorkStation()

        elif 'take screenshot' in query or 'take screen shot' in query or 'snapshot' in query \
        or 'take a screenshot' in query or 'take a screen shot' in query:
            speak('ok,let me take a screenshot ')
            speak('check your desktop, i saved there')
            pic = pyautogui.screenshot()
            pic.save('C:/home/robotics')

        elif 'your born' in query or ' you born' in query or 'how old are you' in query or 'your birthday' in query:
            speak('my creator starts coding me at 15,5,2019')

        elif ('who' in query and 'creats you' in query) or ('who' in query and 'your creator' in query):
            speak('khaled mostafa is my creator')

        elif 'your favourite food' in query:
            speak('a lot of zeros and ones')

        elif 'battery' in query  and 'percentage' in query:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = int(battery.percent)
            time_left = secs2hours(battery.secsleft)
            speak(str(percent))
            if percent < 40 and plugged == False:
                speak('sir, please connect charger because i can survive only ' + time_left)
            if percent < 40 and plugged == True:
                speak("don't worry,charger is connected")
            else:
                speak('no need to connect the charger because i can survive ' + time_left)

        elif 'sing song' in query or 'sing a song' in query:
            speak('la la la la la la la ')
            speak('la la la la la la la ')
            speak(' la!')
            speak('la la la la la la la ')
            
            '''
        # Remind command
        elif 'add' in query and 'reminder' in query:
            speak('what should i remind?')
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                speak('say')
                audio = r.listen(source=source, timeout=10, phrase_time_limit=3)
                global remind_speech
                remind_speech = r.recognize_google(audio)
                speak('alright, i will remind you' + remind_speech)
            '''
        # Ask Reminder
        elif 'reminder' in query:
            if remind_speech is 'global':
                speak('you do not have any reminder for today')
            else:
                speak('you have one reminder' + remind_speech)

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
        
        elif 'brightness' in query:
            brightness(query)
        
        elif 'delete database' in query:
            os.remove(database_file_name)
            speak("ok,its done.")

            '''
        elif 'list directory' in query:
            print(os.listdir("parent_dir"))
            speak("ok,its done.")
            '''

        elif 'current directory' in query:
            speak(os.getcwd())
        
        else:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak(results)
