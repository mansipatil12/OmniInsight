import unittest
from email_ingestion import fetch_emails
from reviews_ingestion import scrape_reviews
from twitter_ingestion import fetch_tweets

class TestDataIngestion(unittest.TestCase):
    def test_fetch_emails(self):
        # Test case 1: Test fetching emails with valid credentials
        email_texts = fetch_emails(username="your_email@example.com", password="your_password")
        # Ensure that emails are fetched successfully
        self.assertIsNotNone(email_texts)
        # Ensure that fetched emails are of the expected data type
        self.assertIsInstance(email_texts, list)
    
    def test_scrape_reviews(self):
        # Test case 2: Test scraping reviews from a valid URL
        review_texts = scrape_reviews(url="https://example.com/product-reviews")
        # Ensure that reviews are scraped successfully
        self.assertIsNotNone(review_texts)
        # Ensure that scraped reviews are of the expected data type
        self.assertIsInstance(review_texts, list)
    
    def test_fetch_tweets(self):
        # Test case 3: Test fetching tweets with valid API credentials
        tweet_texts = fetch_tweets(api_key="your_api_key", api_secret_key="your_api_secret_key", 
                                   access_token="your_access_token", access_token_secret="your_access_token_secret", 
                                   query="data science")
        # Ensure that tweets are fetched successfully
        self.assertIsNotNone(tweet_texts)
        # Ensure that fetched tweets are of the expected data type
        self.assertIsInstance(tweet_texts, list)

if __name__ == "__main__":
    unittest.main()
