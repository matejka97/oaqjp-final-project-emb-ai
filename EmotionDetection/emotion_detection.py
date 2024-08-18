import requests
import json

def emotion_detector(text_to_analyse):
    """Function to run emotion detection"""
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    obj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = obj, headers = header)

    formated_response = json.loads(response.text)
    emotions = formated_response['emotionPredictions'][0]['emotion']
    output_dict = {}
    score = 0

    for key, value in emotions.items():
        
        output_dict[key] = value

        if value > score:
            dominant_emotion = key
        
        score = value
    
    output_dict['dominant_emotion'] = dominant_emotion

    return output_dict