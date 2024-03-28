import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    """
    Scrapes headlines from the given URL of a news website.

    Parameters:
        url (str): The URL of the website to scrape.

    Returns:
        None
    """
    # Send a GET request to the URL
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all('span', class_='tease-card__headline')
        
        # Print each headline
        for headline in headlines:
            headline_text = headline.get_text(strip=True)
            print(headline_text)
    else:
        print("Failed to retrieve the webpage")

if __name__ == "__main__":
    # The URL of the news website to scrape
    url = 'https://www.msnbc.com'
    scrape_headlines(url)
