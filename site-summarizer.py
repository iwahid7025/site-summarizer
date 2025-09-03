from resources.summarizer import check_api_key, display_summary

def main():
    """Main function to run the interactive site summarizer"""
    print("=== Website Summarizer ===")
    print("Enter a website URL to get an AI-powered summary\n")
    
    # Check API key first
    if not check_api_key():
        return
    
    while True:
        try:
            # Get URL from user
            url = input("Enter website URL (or 'quit' to exit): ").strip()
            
            # Check if user wants to quit
            if url.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            # Validate URL format
            if not url:
                print("Please enter a valid URL.\n")
                continue
                
            if not (url.startswith('http://') or url.startswith('https://')):
                print("Please enter a URL starting with http:// or https://\n")
                continue
            
            print(f"\nSummarizing: {url}")
            print("-" * 50)
            
            # Display the summary
            display_summary(url)
            print("-" * 50)
            print()
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except EOFError:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print("Please try again with a different URL.\n")

if __name__ == "__main__":
    main()