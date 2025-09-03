"""
summarizer.py - AI-powered website summarization module

This module handles the core functionality of summarizing website content
using OpenAI's GPT model. It includes API key validation, prompt generation,
and interaction with the OpenAI API.
"""

from .Website import Website
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables from .env file
# override=True ensures .env values take precedence over existing environment variables
load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI client with the API key from environment
openai = OpenAI()

# System prompt that defines the AI assistant's behavior and output format
# This prompt instructs the AI to focus on main content and ignore navigation elements
system_prompt = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
Respond in markdown."


def user_prompt_for(website):
    """
    Generate a user prompt for the OpenAI API based on website content.
    
    This function creates a detailed prompt that includes the website title
    and full text content, asking the AI to summarize it in markdown format.
    
    Args:
        website (Website): A Website object containing title and text content
        
    Returns:
        str: A formatted prompt string for the OpenAI API
    """
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "\nThe contents of this website is as follows; \
please provide a short summary of this website in markdown. \
If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt


def messages_for(website):
    """
    Create a messages array formatted for the OpenAI Chat API.
    
    The OpenAI Chat API expects messages in a specific format with roles
    (system, user, assistant) and content. This function structures the
    system prompt and user prompt correctly.
    
    Args:
        website (Website): A Website object to generate messages for
        
    Returns:
        list: A list of message dictionaries for the OpenAI API
    """
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]


def summarize(url):
    """
    Summarize a website's content using OpenAI's GPT model.
    
    This is the main function that orchestrates the entire summarization process:
    1. Creates a Website object to scrape the content
    2. Generates appropriate prompts
    3. Calls the OpenAI API
    4. Returns the AI-generated summary
    
    Args:
        url (str): The URL of the website to summarize
        
    Returns:
        str: The AI-generated summary in markdown format
        
    Raises:
        requests.RequestException: If website scraping fails
        openai.OpenAIError: If the OpenAI API call fails
    """
    # Scrape the website content
    website = Website(url)
    
    # Call OpenAI API with the website content
    response = openai.chat.completions.create(
        model="gpt-4o-mini",  # Using the cost-effective mini model
        messages=messages_for(website)
    )
    
    # Extract and return the AI's response
    return response.choices[0].message.content


def display_summary(url):
    """
    Summarize a website and display the result to the console.
    
    This is a convenience function that combines summarization and display.
    It handles the summarization process and prints the result.
    
    Args:
        url (str): The URL of the website to summarize and display
    """
    summary = summarize(url)
    print(summary)


def check_api_key():
    """
    Validate the OpenAI API key and provide helpful error messages.
    
    This function performs several checks on the API key:
    1. Checks if the key exists
    2. Validates the key format (should start with 'sk-proj-')
    3. Checks for whitespace issues
    
    Returns:
        bool: True if the API key is valid, False otherwise
        
    Side Effects:
        Prints informative messages about the API key status
    """
    if not api_key:
        print("No API key was found - please create a .env file with your OpenAI API key!")
        print("Get your API key from: https://platform.openai.com/api-keys")
        return False
    elif not api_key.startswith("sk-proj-"):
        print("An API key was found, but it doesn't start with 'sk-proj-'")
        print("Please check you're using the correct OpenAI API key format")
        return False
    elif api_key.strip() != api_key:
        print("An API key was found, but it has whitespace at the beginning or end")
        print("Please remove any spaces or tabs from your API key in the .env file")
        return False
    else:
        print("API key found and looks good so far!")
        return True
