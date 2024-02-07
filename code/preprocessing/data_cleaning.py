import re

def clean_text(text):
    """
    Clean and preprocess text data.
    
    Args:
    text (str): The input text to be cleaned.
    
    Returns:
    str: The cleaned text.
    """
    # Convert text to lowercase
    text = text.lower()
    # Remove special characters, punctuation, and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Strip leading and trailing whitespace
    text = text.strip()
    
    return text

def remove_stopwords(text, stopwords):
    """
    Remove stopwords from text data.
    
    Args:
    text (str): The input text.
    stopwords (list): A list of stopwords to be removed.
    
    Returns:
    str: The text with stopwords removed.
    """
    # Tokenize the text
    tokens = text.split()
    # Remove stopwords
    filtered_tokens = [token for token in tokens if token not in stopwords]
    # Join the tokens back into a single string
    filtered_text = ' '.join(filtered_tokens)
    
    return filtered_text

# Example usage
if __name__ == "__main__":
    # Example text data
    text = "This is an example sentence with numbers 123 and special characters !@#."
    
    # Clean the text
    cleaned_text = clean_text(text)
    print("Cleaned Text:", cleaned_text)
    
    # Example stopwords
    stopwords = ["is", "an", "with", "and"]
    
    # Remove stopwords
    text_without_stopwords = remove_stopwords(cleaned_text, stopwords)
    print("Text without stopwords:", text_without_stopwords)
