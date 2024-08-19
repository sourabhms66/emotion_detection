import nlpcloud
from functools import reduce
class API:
    def __init__(self):
        self.client = nlpcloud.Client("distilbert-base-uncased-emotion", "your_api_key", gpu=False, lang="en")

    def sentiment_analysis(self,text):
        response = self.client.sentiment(text)
        l = []
        for i in response['scored_labels']:
            l.append(i['score'])
        max_score = reduce(lambda x,y:x if x>y else y,l)
        for i in response['scored_labels']:
            if i['score'] == max_score:
                return "The sentiment is: " + i['label']

    def ner(self,text):
        pass

    def emotion_detection(self,text):
        pass
