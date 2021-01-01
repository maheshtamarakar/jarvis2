import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(voices):

    engine.say(voices)
    engine.runAndWait()
  
    
    
    
    


def larger(arr):
    max=arr[0]
    for item in range(1, len(arr)):
        if arr[item]>max:
            max=arr[item]
    return max



arr=[20,50,78,99,33]
print(f'the largest value is {larger(arr)}')
speak(f'the largest value is {larger(arr)}')