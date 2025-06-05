import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=input_json)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response_json = response.json()
    emotions = response_json['text']['emotion']['document']['emotion']

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': emotions.get('anger'),
        'disgust': emotions.get('disgust'),
        'fear': emotions.get('fear'),
        'joy': emotions.get('joy'),
        'sadness': emotions.get('sadness'),
        'dominant_emotion': dominant_emotion
    }
