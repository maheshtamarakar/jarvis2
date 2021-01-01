import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(voices):
    engine.say(voices)
    engine.runAndWait()
def WishMe():
    time = int(datetime.datetime.now().hour)
    if time>=0 and time<12:
        speak('good morning mahesh this is shrishti')
    elif time>=12 and time<18:
        speak('good afternoon mahesh this is shrishti')
    else:
        speak('good evening mahesh this is shrishti')
    speak('how can i help you dear')

def TakeCommand():
    #convert audio into query
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening..........')
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print('recognizing.........')
        query = r.recognize_google(audio, language='en-in') 
        print(f"you said {query}")
    
    except Exception as e:
        speak('something may wrong happend please try again......')
    return query

def SendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 889)
    server.connect('smtp.gmail.com', 997)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('approxgameplay@gmail.com', 'approx@786')
    server.sendmail('approxgameplay@gmail.com', to, content)
    server.quite()

        

if __name__ == "__main__":
    # speak('i am shrishti love you mahesh')
    WishMe()
    query=TakeCommand().lower()
    if 1:
        if 'wikipedia' in query:
            print('searching.........')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'play music' in query:
            song_dir='E:\\music'
            lst_song = os.listdir(song_dir)
            os.startfile(os.path.join(song_dir, lst_song[8]))
        elif 'open code' in query:
            code_dir='C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe'
            os.startfile(code_dir)
        elif 'send email to mahesh' in query:
            try:
                print('what should i say')
                speak('what should i say')
                to='maheshtamarakar369@gmail.com'
                content=TakeCommand()
                SendEmail(to, content)
                print('your email sent successfully....')
                speak('your email sent successfully....')
            except Exception as e:
                print(e)
                print('something may wrong happened please try again')
                speak('something may wrong happened please try again')
