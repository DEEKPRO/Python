import cv2
import colorama
from textblob import TextBlob
from colorama import Fore,Style

colorama.init()
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error. Failed to capture image.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 50))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
    cv2.imshow('Face Detection - Press q to Quit', frame)
    emotion = TextBlob(str(face_cascade)).sentiment.polarity
    if emotion > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😁"
    elif emotion < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😢"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😕"

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()