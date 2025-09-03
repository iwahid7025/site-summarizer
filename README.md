# Website Summarizer

An interactive AI-powered tool that summarizes any website content using OpenAI's GPT model.

## Features

- Interactive command-line interface
- AI-powered website content summarization
- Support for multiple websites in one session
- Clean markdown-formatted summaries

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/iwahid7025/site-summarizer.git
   cd site-summarizer
   ```

2. **Install dependencies:**
   ```bash
   conda install openai python-dotenv requests beautifulsoup4 -y
   ```

3. **Create `.env` file:**
   ```bash
   echo "OPENAI_API_KEY=your_api_key_here" > .env
   ```
   Get your API key from: https://platform.openai.com/api-keys

## Usage

Run the interactive summarizer:
```bash
python site-summarizer.py
```

Enter website URLs when prompted, or type 'quit' to exit.

## Example

```
=== Website Summarizer ===
Enter a website URL to get an AI-powered summary

Enter website URL (or 'quit' to exit): https://example.com
Summarizing: https://example.com
--------------------------------------------------
[AI-generated summary appears here]
--------------------------------------------------
```
