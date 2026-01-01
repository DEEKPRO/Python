import requests

api_url = "https://router.huggingface.co/models/distilbert-base-uncased"

headers = {
    "Authorization":"Bearer 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"
}

text = input("Enter the text to be analyzed: \n")

response = requests.post(api_url, headers=headers, json={"inputs":text})
if response.status_code == 200:
    result = response.json()
    print(f"Sentiment: {result[0]['label']} with confidence score: {result[0]['score']}")
else:
    print(f"Error: {response.status_code}")