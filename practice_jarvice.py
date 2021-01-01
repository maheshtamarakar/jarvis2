import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(voices):
    engine.say(voices)
    engine.runAndWait()

def WishMe():
    time=int(datetime.datetime.now().hour)
    if time>=0 and time<12:
        speak('good morning!')
    if time>=12 and time<18:
        speak('good afternoon!')
    else:
        speak('good evening!')
    speak('this is shrishti sir.. how can i help you')

def TakeCommand():
    # to convert audio into query
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening......')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('recognizing.......')
        query=r.recognize_google(audio,language='en-in')
        print(f"you said {query}")
        
    except Exception as e:
        print('something wrong may happen sir please speak again')
        speak('something wrong may happen sir please speak again')
    return query



if __name__=='__main__':
    WishMe()
    if 1:
        query=TakeCommand().lower()
        if 'open youtube' in query:
            webbrowser.open('youtube.com')
        if 'open google' in query:
            webbrowser.open('google.com')
        if 'play music' in query:
            music_dir='E:\music'
            song_list=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, song_list[9]))
        if 'wikipedia' in query:
            query=query.replace('wikipedia', '')
            result=wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        if 'open code' in query:
            code_dir('C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe')
            os.startfile(code_dir)
        if 'the time' in query:
            Current_Time=datetime.datetime.now().strftime('%H:%M:%S')
            print(f'the current time is{Current_Time}')
            speak(f'the current time is{Current_Time}')
