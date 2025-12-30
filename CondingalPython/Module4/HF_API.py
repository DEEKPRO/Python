import requests
from config import api
# Label 0 is Negative
# Label 1 is Neutral
# Label 2 is Positive
def classify_text(text):
    api_url = 'https://router.huggingface.co/hf-inference/models/cardiffnlp/twitter-roberta-base-sentiment'
    header = {"Authorization":f"Bearer {api}"}
    payload = {"inputs":text}
    response = requests.post(api_url, headers=header, json=payload)
    return response.json()

if __name__ == "__main__":
    sam_text = input("Enter some text to identify the sentiment: \n")
    result = classify_text(sam_text)
    print(result)