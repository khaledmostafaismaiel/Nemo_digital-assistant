import webbrowser
import wikipedia  # pip install wikipedia
import smtplib
import digital_assistant_funcs


YOUTUBE_URL = 'https://www.youtube.com'

GOOGLE_URL = 'https://www.google.com'

STACK_OVERFLOW_URL = 'https://stackoverflow.com/'

LINKED_IN_URL = 'https://www.linkedin.com/in/khaled-mostafa-414265bb/'

GIT_HUB_URL = 'https://github.com/khaledmostafaismaiel'

INSTAGRAM_URL = 'https://www.instagram.com/'

FACEBOOK_URL = 'https://www.facebook.com/khaled.asfora.7'

WHATS_APP_URL = 'https://web.whatsapp.com/'

GOOGLE_TRANSLATION_URL = 'https://translate.google.com'

G_MAIL_URL = 'https://mail.google.com'

EVER_NOTE_URL = 'https://www.evernote.com/client/web#?an=true&n=a28be6fe-bd4b-41e6-84aa-e6fe500444e5&s=s669&/'

GOOGLE_DRIVE_URL = 'https://drive.google.com/drive/my-drive'

PROGRAMIZE_URL = 'https://www.programiz.com/'


def open_website(website_url):
    webbrowser.open(website_url, new=0, autoraise=False)

def search_in_wiki(query):
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=1)
    digital_assistant_funcs.speak(results)


def send_e_mail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('khaledmostafa297@gmail.com', '01143325016')
    server.sendmail('khaledmostafa297@gmail.com', to, content)
    server.close()


def compose_e_mail():
    try:
        digital_assistant_funcs.speak("What should I say?")
        content = digital_assistant_funcs.take_command()
        #speak("Who is the recipient ?")
        #to = takeCommand()
        to = "Khalidgad23@gmail.com"
        send_e_mail(to, content)
        digital_assistant_funcs.speak("Email has been sent successfully !")
    except Exception as e:
        print(e)
        digital_assistant_funcs.speak("Sorry ,I am not able to send this email")
