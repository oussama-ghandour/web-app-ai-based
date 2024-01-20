import requests
import json


def sentiment_analyzer(text_to_analyse):
    '''
    The expected output from calling the sentiment analyzer should be label and score extracted
    from Watson NLP library
    '''
    # Accessing BERT based sentiment analysis function(url,headers,input json format)
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": {"text": text_to_analyse} }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json = myobj, headers=header)
    # Response of the Watson NLP function(label,score)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    # In case of invalid text entry
    elif response.status_code == 500:
        label = None
        score = None
    return {'label': label, 'score': score}