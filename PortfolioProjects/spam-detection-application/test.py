import unittest
from model import predict_spam

class TestSpamDetection(unittest.TestCase):
    def test_spam(self):
        msg = "Congratulations! You have won a prize"
        self.assertIn("spam", predict_spam(msg).lower())
    
    def test_ham(self):
        msg = "Let's catch up tommorrow"
        self.assertIn("ham", predict_spam(msg).lower())
    
    def test_empty(self):
        msg = ""
        self.assertTrue(predict_spam(msg).lower())

if __name__ == "__main__":
    unittest.main()