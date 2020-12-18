from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
class Senti:
    def __init__(self, text):
        self.text = text

    def sentiment(self):
        x = analyzer.polarity_scores(self.text)
        return list(x.values())[-1]
