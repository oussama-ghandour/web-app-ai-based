from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest


# Unit test class 
class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        sent_positive = sentiment_analyzer("I love working with Python")
        self.assertEqual(sent_positive['label'], 'SENT_POSITIVE')
        sent_negative = sentiment_analyzer("I dislike her unfriendly attitude")
        self.assertEqual(sent_negative['label'], 'SENT_NEGATIVE')
        sent_neutral = sentiment_analyzer("I am neutral on this")
        self.assertEqual(sent_neutral['label'], 'SENT_NEUTRAL')

unittest.main()
