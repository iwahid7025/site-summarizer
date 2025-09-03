"""
Website.py - Web scraping module for extracting content from websites

This module provides the Website class for fetching and parsing web content
using requests and BeautifulSoup libraries.
"""

import requests
from bs4 import BeautifulSoup

# HTTP headers to mimic a real browser request and avoid being blocked
# Many websites block requests that don't have proper user-agent headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


class Website:
    """
    A class to represent and parse a webpage's content.
    
    This class fetches a webpage, extracts its title and main text content,
    and removes irrelevant elements like scripts, styles, and images.
    """
    
    def __init__(self, url):
        """
        Initialize a Website object by fetching and parsing the given URL.
        
        Args:
            url (str): The URL of the website to scrape
            
        Attributes:
            url (str): The original URL
            title (str): The webpage's title
            text (str): The main text content of the webpage
        """
        self.url = url
        
        # Fetch the webpage content using requests
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the page title
        self.title = soup.title.string if soup.title else "No title found"
        
        # Remove irrelevant HTML elements that don't contain useful text
        # This includes scripts, stylesheets, images, and form inputs
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        
        # Extract clean text content from the remaining HTML
        # separator="\n" preserves line breaks, strip=True removes extra whitespace
        self.text = soup.body.get_text(separator="\n", strip=True)