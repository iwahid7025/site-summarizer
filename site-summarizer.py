"""
site-summarizer.py - Interactive CLI for AI-powered website summarization

This is the main entry point for the website summarizer application.
It provides an interactive command-line interface that allows users to
enter website URLs and receive AI-generated summaries.

Usage:
    python site-summarizer.py

The script will prompt users to enter website URLs and display summaries
until they choose to quit by typing 'quit', 'exit', or 'q'.
"""

from resources.summarizer import check_api_key, display_summary


def main():
    """
    Main function that runs the interactive website summarizer.
    
    This function handles the entire user interaction flow:
    1. Displays welcome message
    2. Validates OpenAI API key
    3. Enters main loop to process user input
    4. Handles various exit conditions and errors gracefully
    
    The function continues running until the user chooses to quit
    or interrupts the program (Ctrl+C).
    """
    # Display welcome message and instructions
    print("=== Website Summarizer ===")
    print("Enter a website URL to get an AI-powered summary\n")
    
    # Validate API key before starting the main loop
    # If the API key is invalid, exit early to avoid API errors
    if not check_api_key():
        return
    
    # Main interaction loop
    while True:
        try:
            # Get URL input from user with prompt
            url = input("Enter website URL (or 'quit' to exit): ").strip()
            
            # Check for quit commands (case-insensitive)
            if url.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            # Validate that user entered something
            if not url:
                print("Please enter a valid URL.\n")
                continue
            
            # Validate URL format - must start with http:// or https://
            # This prevents common user input errors
            if not (url.startswith('http://') or url.startswith('https://')):
                print("Please enter a URL starting with http:// or https://\n")
                continue
            
            # Display what we're processing
            print(f"\nSummarizing: {url}")
            print("-" * 50)
            
            # Process the URL and display the AI-generated summary
            display_summary(url)
            
            # Add visual separation for better readability
            print("-" * 50)
            print()
            
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\nGoodbye!")
            break
        except EOFError:
            # Handle EOF (Ctrl+D on Unix, Ctrl+Z on Windows) gracefully
            print("\n\nGoodbye!")
            break
        except Exception as e:
            # Handle any other errors (network issues, invalid URLs, API errors)
            print(f"An error occurred: {str(e)}")
            print("Please try again with a different URL.\n")


if __name__ == "__main__":
    # Only run main() if this script is executed directly
    # (not when imported as a module)
    main()