import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
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
		speak('good evening!')
	speak('i am jarvis sir. please tell me how can i help you')
def TakeCommand():

	r=sr.Recognizer()
	with sr.Microphone() as source:
		print('listening.......')
		r.pause_threshold=1
		audio=r.listen(source)

	try:
		print('Recognizing.......')
		query=r.recognize_google(audio,language='en-in')
		print(f'you said: {query}')

	except Exception as e:
		print('Say that again please.........')
		return 'None'
	return query

if __name__=="__main__":

   WishMe()
   if 1:
	   
	   query=TakeCommand().lower()

	   if 'open youtube' in query:

		   webbrowser.open('youtube.com')
	   elif 'wikipedia' in query:


		   query=query.replace('wikipedia', '')
		   result=wikipedia.summary(query,sentences=2)
		   print(result)
		   speak(result)
	   elif :
	       pass
