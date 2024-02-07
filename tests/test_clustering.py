import unittest
from topic_modelling import perform_topic_modeling

class TestClustering(unittest.TestCase):
    def test_perform_topic_modeling(self):
        # Test case 1: Test topic modeling with sample data
        sample_texts = [
            ["customer", "service", "experience", "satisfied", "issue", "resolved"],
            ["product", "quality", "excellent", "value", "money"],
            ["delivery", "time", "fast", "efficient", "shipping"],
            ["user", "interface", "easy", "navigate", "intuitive"]
        ]
        # Perform topic modeling
        topic_results = perform_topic_modeling(sample_texts)
        # Ensure the correct number of topics is returned
        self.assertEqual(len(topic_results), 5)
        # Ensure each topic contains the correct number of words
        for topic_id, topic_words in topic_results:
            self.assertEqual(len(topic_words.split()), 10)

if __name__ == "__main__":
    unittest.main()
