from nltk.sentiment.vader import SentimentIntensityAnalyzer

def perform_sentiment_analysis(texts):
    """
    Perform sentiment analysis on a list of preprocessed texts.
    
    Args:
    texts (list): A list of preprocessed texts.
    
    Returns:
    list: A list of sentiment scores for each text.
    """
    # Initialize the VADER sentiment analyzer
    sid = SentimentIntensityAnalyzer()
    
    # Perform sentiment analysis on each text
    sentiment_scores = []
    for text in texts:
        # Get sentiment scores for the text
        scores = sid.polarity_scores(text)
        # Normalize the compound score to a range of [-1, 1]
        compound_score = scores['compound']
        # Classify sentiment based on the compound score
        if compound_score >= 0.05:
            sentiment = 'Positive'
        elif compound_score <= -0.05:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
        sentiment_scores.append((text, compound_score, sentiment))
    
    return sentiment_scores

# Example usage
if __name__ == "__main__":
    # Example list of preprocessed texts
    preprocessed_texts = [
        "This movie is fantastic!",
        "I hated the customer service.",
        "The product quality is average.",
        "I'm not sure how I feel about this."
    ]
    
    # Perform sentiment analysis
    sentiment_results = perform_sentiment_analysis(preprocessed_texts)
    
    # Print sentiment results
    for text, score, sentiment in sentiment_results:
        print(f"Text: {text}")
        print(f"Sentiment Score: {score}")
        print(f"Sentiment: {sentiment}\n")
