# Web Scraping Project

This project is designed to demonstrate web scraping techniques using different tools and libraries such as Playwright, BeautifulSoup, and AI. The aim is to collect and parse data from the web.

## Project Structure

```
web_scraping/
├── __pycache__/
├── .gitignore
├── 1_api_call.py
├── 2_bsoup_parsing.py
├── 3.1_playwright_synchronous.py
├── 3.2_playwright_search.py
├── 4_ai_parsing.py
├── 5.1_crawling_parsing.py
├── 5.2_web_crawler.py
├── 5.3_web_parsing.py
├── all_book_urls.txt
├── github_sample_data.csv
├── set_up.txt
├── util.py
```

### Files and Directories

- **1_api_call.py**: Script for making API calls and simple request to scrap data.
- **2_bsoup_parsing.py**: Script using BeautifulSoup for HTML parsing.
- **3.1_playwright_synchronous.py**: Synchronous script using Playwright for web scraping.
- **3.2_playwright_search.py**: Playwright script focusing on searching and extracting specific data.
- **4_ai_parsing.py**: Script utilizing AI-based techniques for parsing and extracting data.
- **5.1_crawling_parsing.py**: Script for web crawling and data parsing.
- **5.2_web_crawler.py**: Web crawling example1.
- **5.3_web_parsing.py**: Web crawling example2.
- **config.yml**: You need to set up your own Configuration file for your `OpenAI API Key` used in `4_ai_parsing.py`.
- **set_up.txt**: Setup instructions or requirements.
- **util.py**: Utility functions used across different scripts.

## Getting Started

### Prerequisites

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/YuchenPeng17/Web-Scraping.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Web-Scraping
   ```
3. Install the required packages in `set_up.txt`

### Usage

1. **API Call**:
   
   - Run `1_api_call.py` to make API requests and handle responses.
   ```sh
   python 1_api_call.py
   ```
   
2. **BeautifulSoup Parsing**:
   - Run `2_bsoup_parsing.py` to parse HTML content using BeautifulSoup.
   ```sh
   python 2_bsoup_parsing.py
   ```

3. **Playwright Synchronous**:
   - Run `3.1_playwright_synchronous.py` for synchronous web scraping using Playwright.
   ```sh
   python 3.1_playwright_synchronous.py
   ```

4. **Playwright Search**:
   - Run `3.2_playwright_search.py` to perform search operations and extract specific data using Playwright.
   ```sh
   python 3.2_playwright_search.py
   ```

5. **AI Parsing**:
   - Run `4_ai_parsing.py` to parse and extract data using AI-based methods.
   ```sh
   python 4_ai_parsing.py
   ```

6. **Crawling and Parsing**:
   - Run `5.1_crawling_parsing.py` for crawling websites and parsing data.
   ```sh
   python 5.1_crawling_parsing.py
   ```

7. **Web crawling example1**:
   
   ```sh
   python 5.2_web_crawler.py
   ```
   
8. **Web crawling example2**:
   
   ```sh
   python 5.3_web_parsing.py
   ```

## Configuration

You can configure various parameters in the `config.yml` file.
