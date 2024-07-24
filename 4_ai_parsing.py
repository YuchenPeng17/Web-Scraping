"""
Unlike BeautifulSoup, for AI
We don't need to know about the HTML structure of target website
We only provide AI with the schema described in natural language
"""

import asyncio
from util import load_config
from langchain_openai import ChatOpenAI
from langchain.chains import create_extraction_chain
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

config = load_config('config.yml')
OPENAI_KEY = config['open_ai']['key']
GPT = 'gpt-4o-mini'
llm = ChatOpenAI(temperature=0, model=GPT, openai_api_key=OPENAI_KEY)

async def run_playwright(site):
    """
    2. Use Playwright to load a webpage, extracts its HTML content, cleans it by removing JavaScript and CSS, and then returns the visible text.
    """
    async with async_playwright() as p:
        # 2.1: Start a browser using playwright
        browser = await p.chromium.launch(headless=False) # if True, may get the error: This browser is no longer supported. Please switch to a supported browser to continue using twitter.com. You can see a list of supported browsers in our He....
        # Option2: firefox
        # browser = await p.firefox.launch(headless=False)

        # 2.2: Set conditions to wait until the page is fully loaded 
        page = await browser.new_page()
        # Set a timeout for navigating to the page
        try:
            # await page.goto(site, wait_until='load', timeout=20000) # 10 secs
            # await page.goto(site, wait_until='load')
            await page.goto(site, wait_until='networkidle')
        except TimeoutError:
            print("Timeout reached during page load, proceeding with available content.")

        # 2.3: Extract clean HTML content of the page
        # Retrieves the full HTML content of the loaded webpage as a string
        page_source = await page.content()
        
        # BeautifulSoup is initialized with page_source (the HTML content) and the parser "html.parser".
        # soup is now a BeautifulSoup object that represents the parsed HTML.
        soup = BeautifulSoup(page_source, "html.parser")
        
        # The soup(["script", "style"]) expression finds all <script> and <style> elements in the HTML.
        # script.extract() removes each <script> and <style> element from the soup object. Clean the HTML by removing JavaScript and CSS code, which are not needed for text extraction.
        for script in soup(["script", "style"]): # Remove all javascript and stylesheet code
            script.extract()
        
        # Extracts all the text from the HTML, excluding the HTML tags.
        text = soup.get_text()

        # Break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines()) 
        # Break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  ")) 
        data = '\n'.join(chunk for chunk in chunks if chunk) # Drop blank lines

        await browser.close()
    return data

async def main():
    """
    1. Define target urls, schemas and run the function
    """
    stock_website_info = {
        "url": "https://stockanalysis.com/stocks/googl/",
        "schema": {
            "properties": {
                "market_cap": {"type": "string"},
                "open": {"type": "string"},
                "eps": {"type": "string"},
                "finantial perfomanc": {"type": "string"},
            },
        }
    }
    youtube_website_info = {
        "url": "https://www.youtube.com/@turingplanet4052/videos",
        "schema": {
            "properties": {
                "title": {"type": "string"},
                "view": {"type": "string"},
                "date": {"type": "string"},
            },
        }
    }
    twitter_website_info = {
        "url": "https://twitter.com/elonmusk/status/1777659389568045424",
        "schema": {
            "properties": {
                "post_author": {"type": "string"},
                "post_content": {"type": "string"},
            },
        }
    }
    techcruch_website_info = {
        "url": "https://techcrunch.com/2024/04/12/meta-is-testing-an-ai-powered-search-bar-in-instagram/",
        "schema": {
            "properties": {
                "article_title": {"type": "string"},
                "article_content": {"type": "string"},
            },
        }
    }

    parsing_target = stock_website_info
    # parsing_target = youtube_website_info
    # parsing_target = twitter_website_info
    # parsing_target = techcruch_website_info

    output = await run_playwright(parsing_target['url'])

    """
    3. Creates a data extraction chain using a schema and a language model, processes the output data, and prints the extracted text.
    """
    json_result = create_extraction_chain(parsing_target['schema'], llm).invoke(output)
    # json_result = {'input': '...', 'text': '...'}
    print(json_result['text'])

if __name__ == "__main__":
    asyncio.run(main())
