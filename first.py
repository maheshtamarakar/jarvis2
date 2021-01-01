import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning!')

    elif hour>=12 and hour<18:
        speak('good afternoon!')

    else:
        speak('good evening')

    speak('i am jarvis sir how may i help you')

def TakeCommand():
    ''' will convert sound to string'''

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening......')
        r.pause_threshold=1
        r.energy_threshold = 400
        audio=r.listen(source)
    try:
        print('recognizing......')
        query=r.recognize_google(audio, language='en-in')
        print(f'you said: {query}')
    except Exception as e:
        print('plz say that again... something wrong may happened....')
    return query
def SendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.connect("smtp.gmail.com",465)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('approxgameplay@gmail.com', 'approx@786')
    server.sendmail('approxgameplay@gmail.com', to, content)
    server.quite()
    


if __name__=='__main__':
    WishMe()
    # if 1:
    while True:
        query=TakeCommand().lower()
        if 'wikipedia' in query:
            query=query.replace('wikipedia', '')
            result=wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir=  'E:\\music' 
            songs=os.listdir(music_dir) 
            # print(songs)  
            os.startfile(os.path.join(music_dir,songs[7]))
        elif 'the time'in query:
            strTime=datetime.datetime.now().strftime('%H:%M:%S')
            print(f'sir the time is {strTime}')
            speak(f'sir the time is {strTime}')
        elif 'open code' in query:
            code_path='C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(code_path)
        elif 'email to mahesh' in query:
            try:
                print('what should i say?')
                speak('what should i say?')
                content=TakeCommand()
                to='maheshtamarakar369@gmail.com'
                SendEmail(to, content)
                print('your email is successfully sent')
                speak('your email is successfully sent')
            except Exception as e:
                print(e)
                print('something wrong may happen so your msg didnt send please try again sir...')
                speak('something wrong may happen so your msg didnt send please try again sir...')
        elif 'exit' in query:
            break
