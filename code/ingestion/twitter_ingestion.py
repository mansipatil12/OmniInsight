import tweepy

def fetch_tweets(api_key, api_secret_key, access_token, access_token_secret, query, count=10):
    """
    Fetch tweets based on a search query.
    
    Args:
    api_key (str): Twitter API key.
    api_secret_key (str): Twitter API secret key.
    access_token (str): Twitter access token.
    access_token_secret (str): Twitter access token secret.
    query (str): The search query to fetch tweets.
    count (int): Number of tweets to fetch (default is 10).
    
    Returns:
    list: A list of tweet texts.
    """
    # Authenticate with Twitter API
    auth = tweepy.OAuth1(api_key, api_secret_key, access_token, access_token_secret)
    api = tweepy.API(auth)
    
    # Fetch tweets based on the query
    tweets = []
    for tweet in tweepy.Cursor(api.search_tweets, q=query, tweet_mode='extended').items(count):
        tweets.append(tweet.full_text)
    
    return tweets

# Example usage
if __name__ == "__main__":
    # Example Twitter API credentials
    api_key = "your_api_key"
    api_secret_key = "your_api_secret_key"
    access_token = "your_access_token"
    access_token_secret = "your_access_token_secret"
    
    # Example search query
    query = "data science"
    
    # Fetch tweets based on the query
    tweets = fetch_tweets(api_key, api_secret_key, access_token, access_token_secret, query)
    
    # Print the fetched tweets
    for i, tweet in enumerate(tweets, start=1):
        print(f"Tweet {i}: {tweet}\n")
