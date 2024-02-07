import requests
from bs4 import BeautifulSoup

def scrape_reviews(url):
    """
    Scrape reviews from a product review website.
    
    Args:
    url (str): The URL of the product review page.
    
    Returns:
    list: A list of review texts.
    """
    # Send a GET request to the URL
    response = requests.get(url)
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract review elements
    review_elements = soup.find_all("div", class_="review")
    
    # Extract review texts
    reviews = []
    for review in review_elements:
        review_text = review.find("p", class_="review-text").get_text()
        reviews.append(review_text.strip())
    
    return reviews

# Example usage
if __name__ == "__main__":
    # Example URL of a product review page
    url = "https://example.com/product-reviews"
    
    # Scrape reviews from the URL
    reviews = scrape_reviews(url)
    
    # Print the scraped reviews
    for i, review in enumerate(reviews, start=1):
        print(f"Review {i}: {review}\n")
