import requests
import time
import cv2

URL = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
def get_fact():
    response = requests.get(URL)
    if response.status_code == 200:
        fact_json = response.json()
        print(f"Did you know that {fact_json['text']}?")
    else:
        print("Failed to retreive facts.")

while True:
    answer = input("Press Enter for a new fact. Press q to exit.")
    if answer.lower() == 'exit' or answer.lower() == 'q':
        break
    get_fact()