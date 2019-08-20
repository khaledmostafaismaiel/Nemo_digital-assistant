import creator_info
import digital_assistant_info
import pyttsx3  # pip install pyttsx3
import digital_assistant_info
import command_line_database
import speech_recognition as sr  # pip install speechRecognition
'''
def digital_assistant_init():
    engine = pyttsx3.init('espeak')
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 140)
    #engine.setProperty('voice', voices[0].id)
    engine.setProperty('voice', 'english+f2')
    engine.setProperty('volume', 1)
    engine.setProperty('female', voices[0].gender)
    engine.setProperty(22, voices[0].age)
'''
def take_command():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(creator_info.CREATOR_FIRST_NAME,':',query)
    # except sr.UnknownValueError :
    except Exception as e:
        print(creator_info.CREATOR_FIRST_NAME,':',e)
        print("Say that again please...")
        return "None"
    
    command_line_database.write_in_database(creator_info.CREATOR_FIRST_NAME,query)
    return query


def say_my_name(): 
    while True:
        query = take_command().lower()
        name = digital_assistant_info.DIGITAL_ASSISTANT_NAME.lower()
        if (name in query):    
            speak('yes sir')
            break


def speak(audio):

    engine = pyttsx3.init('espeak')
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 140)
    #engine.setProperty('voice', voices[0].id)
    engine.setProperty('voice', 'english+f2')
    engine.setProperty('volume', 1)
    engine.setProperty('female', voices[0].gender)
    engine.setProperty(22, voices[0].age)


    print(digital_assistant_info.DIGITAL_ASSISTANT_NAME,':',audio)  # i add this line to print what bondo2 said
    engine.say(audio)
    engine.runAndWait()
    command_line_database.write_in_database(digital_assistant_info.DIGITAL_ASSISTANT_NAME,audio)