import requests

API_URL1 = "https://api-inference.huggingface.co/models/cointegrated/rubert-tiny2-cedr-emotion-detection"

API_URL2 = "https://api-inference.huggingface.co/models/cointegrated/rubert-tiny-sentiment-balanced"

headers = {"Authorization": f"Bearer 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"}


def query1(payload):
    response = requests.post(API_URL1, headers=headers, json=payload)
    return response.json()


def query2(payload):
    response = requests.post(API_URL2, headers=headers, json=payload)
    return response.json()


def emotion(message: str):
    test = message.upper()
    if test == message:
        return "fear"
    message = message.lower()
    js1 = query1(message)
    js2 = query2(message)
    if abs(js1[0][0]['score'] - js1[0][1]['score']) >= abs(js2[0][0]['score'] - js2[0][1]['score']) * 3:
        return js1[0][0]['label']
    if abs(js2[0][0]['score'] - js2[0][1]['score']) <= 0.15:
        return js1[0][0]['label']
    if js2[0][0]['label'] == 'neutral':
        return 'neutral'
    if js2[0][0]['label'] == 'positive':
        for i in range(len(js1[0])):
            if js1[0][i]['label'] == 'joy' or js1[0][i]['label'] == 'surprise':
                return js1[0][i]['label']
    if js2[0][0]['label'] == 'negative':
        for i in range(len(js1[0])):
            if js1[0][i]['label'] == 'anger' or js1[0][i]['label'] == 'fear' or js1[0][i]['label'] == 'sadness':
                return js1[0][i]['label']


def color(text: str):
    if text == 'anger':
        return 'red'
    if text == 'sadness':
        return 'blue'
    if text == 'fear':
        return 'green'
    if text == 'surprise':
        return 'izumrud'
    if text == 'neutral' or text == 'no_emotion':
        return 'neutral'
    if text == 'joy':
        return 'yellow'

