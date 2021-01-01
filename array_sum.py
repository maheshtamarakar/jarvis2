import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def _sum(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum

def speak(voices):
    engine.say(voices)
    engine.runAndWait()



arr = [3,5,6,4,2]
print(f'sum of the array is {_sum(arr)}')
speak(f'sum of the array is {_sum(arr)}')