import gensim
from gensim import corpora
from pprint import pprint

def perform_topic_modeling(texts, num_topics=5, num_words=10):
    """
    Perform topic modeling on a list of preprocessed texts using Latent Dirichlet Allocation (LDA).
    
    Args:
    texts (list): A list of preprocessed texts.
    num_topics (int): The number of topics to identify (default is 5).
    num_words (int): The number of words to display for each topic (default is 10).
    
    Returns:
    list: A list of tuples containing the top words for each topic.
    """
    # Create a dictionary representation of the texts
    dictionary = corpora.Dictionary(texts)
    
    # Create a bag-of-words representation of the texts
    corpus = [dictionary.doc2bow(text) for text in texts]
    
    # Perform LDA topic modeling
    lda_model = gensim.models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15)
    
    # Get the top words for each topic
    topic_words = lda_model.print_topics(num_topics=num_topics, num_words=num_words)
    
    return topic_words

# Example usage
if __name__ == "__main__":
    # Example list of preprocessed texts
    preprocessed_texts = [
        ["customer", "service", "experience", "satisfied", "issue", "resolved"],
        ["product", "quality", "excellent", "value", "money"],
        ["delivery", "time", "fast", "efficient", "shipping"],
        ["user", "interface", "easy", "navigate", "intuitive"]
    ]
    
    # Perform topic modeling
    topic_results = perform_topic_modeling(preprocessed_texts)
    
    # Print topic results
    for topic_id, topic_words in topic_results:
        print(f"Topic {topic_id}: {topic_words}\n")
