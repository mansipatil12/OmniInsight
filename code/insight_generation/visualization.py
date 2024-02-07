import matplotlib.pyplot as plt

def visualize_sentiment_distribution(sentiments):
    """
    Visualize the sentiment distribution of a list of sentiment labels.
    
    Args:
    sentiments (list): A list of sentiment labels (e.g., 'Positive', 'Negative', 'Neutral').
    """
    # Count the occurrences of each sentiment label
    sentiment_counts = {sentiment: sentiments.count(sentiment) for sentiment in set(sentiments)}
    
    # Plot the sentiment distribution
    plt.bar(sentiment_counts.keys(), sentiment_counts.values())
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.title('Sentiment Distribution')
    plt.show()

# Example usage
if __name__ == "__main__":
    # Example list of sentiment labels
    sentiments = ['Positive', 'Negative', 'Neutral', 'Positive', 'Positive', 'Negative', 'Neutral']
    
    # Visualize the sentiment distribution
    visualize_sentiment_distribution(sentiments)
