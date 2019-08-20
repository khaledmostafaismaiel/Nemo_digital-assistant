import creator_info
import digital_assistant_info
import speech_recognition as sr  # pip install speechRecognition
import datetime
import website
import os
import ctypes
import pyautogui
from playsound import playsound
import time
import digital_assistant_funcs
import command_line_database
import operating_system


#digital_assistant_funcs.digital_assistant_init()

remind_speech = 'still_version'



def welcome_message():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        digital_assistant_funcs.speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        digital_assistant_funcs.speak("Good Afternoon!")

    else:
        digital_assistant_funcs.speak("Good Evening!")

    digital_assistant_funcs.speak("My name is "+digital_assistant_info.DIGITAL_ASSISTANT_NAME+". How may I help you ?")



if __name__ == "__main__":
    
    
    welcome_message()
    
while True :
        
    while True:

        digital_assistant_funcs.say_my_name()
        
        # Logic for executing tasks based on query
        query = digital_assistant_funcs.take_command().lower()


        if (('open' in query)and('youtube' in query)):
            website.open_website(website.YOUTUBE_URL)

        elif (('open' in query)and('google' in query)):
            website.open_website(website.GOOGLE_URL)

        elif (('open' in query)and('stack over flow' in query)):
            website.open_website(website.STACK_OVERFLOW_URL)

        elif (('open' in query)and('linkedin' in query)):
            website.open_website(website.LINKED_IN_URL)

        elif (('open' in query)and('github' in query)):
            website.open_website(website.GIT_HUB_URL)

        elif (('open' in query)and('facebook' in query)):
            website.open_website(website.FACEBOOK_URL)

        elif (('open' in query)and('instagram' in query)):
            website.open_website(website.INSTAGRAM_URL)

        elif (('open' in query)and('whatsapp' in query)):
            website.open_website(website.WHATS_APP_URL)

        elif (('open' in query)and('gmail' in query)):
            website.open_website(website.G_MAIL_URL)

        elif (('open' in query)and('translate' in query)):
            website.open_website(website.GOOGLE_TRANSLATION_URL)

        elif (('open' in query)and('drive' in query)):
            website.open_website(website.GOOGLE_DRIVE_URL)

        elif (('open' in query)and('ever note' in query)):
            website.open_website(website.EVER_NOTE_URL)
        
        elif (('open' in query)and('programiz' in query)):
            website.open_website(website.PROGRAMIZE_URL)
    
        elif (('open' in query)and('songs' in query)) or (('open' in query)and('song' in query)):
            website.webbrowser.open('https://www.youtube.com/watch?v=hlznpxNGFGQ&list=RDhlznpxNGFGQ&start_radio=1', new=0, autoraise=False)
            digital_assistant_funcs.speak('Enjoy !')
        
        elif (('open' in query)and('quraan' in query)):
            website.webbrowser.open('https://www.youtube.com/watch?v=2rx0DYOex1c', new=0, autoraise=False)
        
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
            '''

        elif query == 'play music' or query == 'romantic bollywood music' or query == ' bollywood music':
            speak('Enjoy !')
            playsound('Main_Hoon_Saath_Tere.mp3')
            '''
            '''
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

            '''
        elif 'date' in query and 'today' in query:
            current_time = time.strftime("%d:%B:%Y:%A:%H:%M:%S")
            digital_assistant_funcs.speak(current_time)

        elif 'the time' in query:
            digital_assistant_funcs.speak('and time is' + time.strftime("%H %M %S"))

        elif 'day we are' in query:
            digital_assistant_funcs.speak(time.strftime("%A"))
            '''
        elif 'open code' in query:
            codePath = "bin/code"
            os.startfile(codePath)
            '''
            '''
        elif 'open pycharm' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            '''
        elif ((('abort' in query) and ('please' in query))or(('stop' in query) and ('please' in query)) \
             or (('shut down' in query) and ('please' in query))or(('turn off' in query) and ('please' in query))):
            digital_assistant_funcs.speak('Ok ,bye , see you later .')
            break

        elif ((('your' in query) and ('functions' in query))or(('your' in query) and ('functionality' in query)) \
            or(('your' in query) and ('function' in query))or(('your' in query) and ('functionalities' in query))):
            digital_assistant_funcs.speak('i can open youtube')
            digital_assistant_funcs.speak('i can open google')
            digital_assistant_funcs.speak('i can open whats app')
            digital_assistant_funcs.speak('i can open instagram')
            digital_assistant_funcs.speak('i can open gmail')
            digital_assistant_funcs.speak('i can open facebook')
            digital_assistant_funcs.speak('i can open github')
            digital_assistant_funcs.speak('i can open stack over flow')
            digital_assistant_funcs.speak('i can open ever note')
            digital_assistant_funcs.speak('i can open google drive')
            digital_assistant_funcs.speak('i can open songs on youtube')
            digital_assistant_funcs.speak('i can open programiz')
            digital_assistant_funcs.speak('i can open quraan on youtube')
            digital_assistant_funcs.speak('i can open google translation')            
            digital_assistant_funcs.speak('i can open music directory')            
            digital_assistant_funcs.speak('i can tell the time')            
            digital_assistant_funcs.speak('i can open visual code stdio directory')            
            digital_assistant_funcs.speak('i can open pycharme directory')            
            digital_assistant_funcs.speak('i can send e mails')            
            digital_assistant_funcs.speak('i can search about every thing')
            digital_assistant_funcs.speak('i can turn off my self')            
            digital_assistant_funcs.speak('my creator try to develop a way to make me do some short talks with humans')

        elif (('ok google' in query) or ('hi google' in query) or ('hello google' in query)):
            digital_assistant_funcs.speak('i am flatter, but google is not me. my name is '+digital_assistant_info.DIGITAL_ASSISTANT_NAME+' if you forget it')
            
        elif (('ok siri' in query) or ('hi siri' in query) or ('hello siri' in query)):
            digital_assistant_funcs.speak('i am flatter, but siri is not me. my name is rose if you forget it')

        elif (('ok alexa' in query) or ('hi alexa' in query) or ('hello alexa' in query)):
            digital_assistant_funcs.speak('i am flatter, but alexa is not me. my name is rose if you forget it')

        elif (('i like you' in query) or ('i love you' in query) or ('you are better than ' in query)):
            digital_assistant_funcs.speak('oh')
            digital_assistant_funcs.speak('you just made my day')

        elif (('your best friend' in query) or ('your friend' in query)):
            digital_assistant_funcs.speak(creator_info.CREATOR_FIRST_NAME+' is my best friend he is my creator.')

        elif (('you have boyfriend' in query) or ('you have a boyfriend' in query) \
            or ('you have boy friend' in query) or ('you in relationship' in query) or ('you in a relationship' in query)):
            digital_assistant_funcs.speak('i think its complicated')

        elif 'will you marry me' in query:
            digital_assistant_funcs.speak('i think its complicated , sorry i can\'t')

        elif 'who are you' in query or 'about yourself' in query:
            digital_assistant_funcs.speak('iam'+digital_assistant_info.DIGITAL_ASSISTANT_NAME+' and iam a digital assistant and i will be the smartest one as soon as posible,')
            digital_assistant_funcs.speak(creator_info.CREATOR_NAME+' is my creator and he start developing me at '+digital_assistant_info.DIGITAL_ASSISTANT_DATE_OF_BIRTH)

        elif 'how are you' in query:
            digital_assistant_funcs.speak('oh')
            digital_assistant_funcs.speak('iam fine and you ! , how have you been')
            '''
        elif 'logout' in query:
            digital_assistant_funcs.speak('ok')
            ctypes.windll.user32.LockWorkStation()
            '''
            '''
        elif 'take screenshot' in query or 'take screen shot' in query or 'snapshot' in query \
        or 'take a screenshot' in query or 'take a screen shot' in query:
            digital_assistant_funcs.speak('ok')
            pic = pyautogui.screenshot()
            pic.save('C:/home/robotics')
            digital_assistant_funcs.speak('check your desktop, i saved there')
            '''
        elif 'your born' in query or ' you born' in query or 'how old are you' in query or 'your birthday' in query:
            digital_assistant_funcs.speak('my creator starts coding me at '+digital_assistant_info.DIGITAL_ASSISTANT_DATE_OF_BIRTH)

        elif ('who' in query and 'creats you' in query) or ('who' in query and 'your creator' in query):
            digital_assistant_funcs.speak(creator_info.CREATOR_NAME+' is my creator')

        elif 'your favourite food' in query:
            digital_assistant_funcs.speak('a lot of zeros and ones')

        elif 'battery' in query  and 'percentage' in query:
            operating_system.battery_status()

        elif 'sing song' in query or 'sing a song' in query:
            digital_assistant_funcs.speak('la la la la la la la ')
            digital_assistant_funcs.speak('la la la la la la la ')
            digital_assistant_funcs.speak(' la!')
            digital_assistant_funcs.speak('la la la la la la la ')
            
            '''
        # Remind command
        elif 'add' in query and 'reminder' in query:
            digital_assistant_funcs.speak('what should i remind?')
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                digital_assistant_funcs.speak('say')
                audio = r.listen(source=source, timeout=10, phrase_time_limit=3)
                global remind_speech
                remind_speech = r.recognize_google(audio)
                digital_assistant_funcs.speak('alright, i will remind you' + remind_speech)
            '''
        # Ask Reminder
        elif 'reminder' in query:
            if remind_speech is 'still_version':
                digital_assistant_funcs.speak('you do not have any reminder for today')
            else:
                digital_assistant_funcs.speak('you have one reminder' + remind_speech)

        elif 'send email' in query:
            website.compose_e_mail()
        
        elif 'brightness' in query:
            operating_system.brightness(query)
        
        elif 'delete database' in query:
            os.remove(command_line_database.COMMAND_LINE_DATABASE_FILE_NAME)
            digital_assistant_funcs.speak("ok,its done.")

            '''
        elif 'list directory' in query:
            print(os.listdir("parent_dir"))
            digital_assistant_funcs.speak("ok,its done.")
            '''

        elif 'current directory' in query:
            digital_assistant_funcs.speak(os.getcwd())
        
        else:
            website.search_in_wiki(query)
