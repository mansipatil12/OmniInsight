import unittest
from data_cleaning import clean_text, remove_stopwords

class TestDataPreprocessing(unittest.TestCase):
    def test_clean_text(self):
        # Test case 1: Test cleaning text with special characters and numbers
        dirty_text = "This is an example sentence with numbers 123 and special characters !@#."
        cleaned_text = clean_text(dirty_text)
        # Ensure that special characters and numbers are removed
        self.assertEqual(cleaned_text, "this is an example sentence with numbers and special characters")
    
    def test_remove_stopwords(self):
        # Test case 2: Test removing stopwords from text
        text = "this is a sample text with some stopwords"
        stopwords = ["is", "a", "with", "some"]
        text_without_stopwords = remove_stopwords(text, stopwords)
        # Ensure that stopwords are removed
        self.assertEqual(text_without_stopwords, "sample text stopwords")

if __name__ == "__main__":
    unittest.main()
