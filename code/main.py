from email_ingestion import fetch_emails
from reviews_ingestion import scrape_reviews
from twitter_ingestion import fetch_tweets
from data_cleaning import clean_text, remove_stopwords
from sentiment_analysis import perform_sentiment_analysis
from topic_modelling import perform_topic_modeling
from visualization import visualize_sentiment_distribution

def main():
    # Step 1: Data Ingestion
    # Fetch emails
    email_texts = fetch_emails(username="your_email@example.com", password="your_password")
    # Scrape reviews
    review_texts = scrape_reviews(url="https://example.com/product-reviews")
    # Fetch tweets
    tweet_texts = fetch_tweets(api_key="your_api_key", api_secret_key="your_api_secret_key", 
                               access_token="your_access_token", access_token_secret="your_access_token_secret", 
                               query="data science")
    
    # Step 2: Data Cleaning
    # Clean text data
    cleaned_email_texts = [clean_text(text) for text in email_texts]
    cleaned_review_texts = [clean_text(text) for text in review_texts]
    cleaned_tweet_texts = [clean_text(text) for text in tweet_texts]
    
    # Step 3: Sentiment Analysis
    # Perform sentiment analysis on email texts
    email_sentiments = perform_sentiment_analysis(cleaned_email_texts)
    # Perform sentiment analysis on review texts
    review_sentiments = perform_sentiment_analysis(cleaned_review_texts)
    # Perform sentiment analysis on tweet texts
    tweet_sentiments = perform_sentiment_analysis(cleaned_tweet_texts)
    
    # Step 4: Topic Modeling
    # Perform topic modeling on review texts
    review_topics = perform_topic_modeling(cleaned_review_texts)
    
    # Step 5: Visualization
    # Visualize sentiment distribution of email sentiments
    visualize_sentiment_distribution(email_sentiments)
    # Visualize sentiment distribution of review sentiments
    visualize_sentiment_distribution(review_sentiments)
    # Visualize sentiment distribution of tweet sentiments
    visualize_sentiment_distribution(tweet_sentiments)

if __name__ == "__main__":
    main()
