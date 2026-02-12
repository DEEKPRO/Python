import speech_recognition as sr
import datetime
import pyttsx3

eng=pyttsx3.init()
eng.setProperty("rate",150)
eng.setProperty('volume',1)

def speak(text):
    print(f"Assistant : {text}")
    eng.say(text)
    eng.runAndWait()
def process(query):
  query=query.lower()
  if "time" in query:
    time=datetime.datetime.now().strftime("%I:%M")
    return f"Current Time : {time}"
  elif "date" in query:
    date=datetime.datetime.now().strftime("%d/%m/%y")
    return f"Today's Date : {date}"
  else:
    return "Talk like a human"
recognizer = sr.Recognizer()
mic=sr.Microphone()
with mic as source:
  recognizer.adjust_for_ambient_noise(source)
  try:
    while True:
      print("Listening...")
      audio=recognizer.listen(source)
      try:
        a=recognizer.recognize_google(audio)
        print("You said :",a)
        b=process(a)
        speak(b)
      except sr.UnknownValueError:
        print("Could not understand audio")
      except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
  except KeyboardInterrupt:
    print("Program terminated by user")
    