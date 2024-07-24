"""
This Python script uses the playwright library to interact with web pages dynamically, 
suitable for extracting information from websites that load content asynchronously or 
have elements that appear only after certain user interactions or delays
"""

# Import the necessary modules
from playwright.async_api import async_playwright  # Playwright module for asynchronous browser control
import asyncio  # Module to handle asynchronous tasks in Python

async def get_article_details(url):

    # 1. Start a context manager with async_playwright() to handle setup and teardown of resources
    async with async_playwright() as p:
        
        # 2. Launch a browser instance (Chromium or Firefox) and create a new page
        browser = await p.chromium.launch(headless=False)
        # browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()

        # 3. Navigate to the specified URL and wait for the page to load
        # load is fired when the page and its resources (images, scripts, stylesheets, etc.) have finished loading. 
        await page.goto(url, wait_until='load')
        # Option2: Wait until network is idle after going to the page
        # await page.goto(url, wait_until='networkidle') # It considers the network to be idle when there are no more than 0 network connections for at least 500 ms (by default).

        # 4.1 Retrieve and print the full page title after it has loaded
        title = await page.title()
        print(f"The page title is: {title}")
        
        # 4.2 Retrieve and print the author of the article
        author = await page.inner_text('.wp-block-tc23-author-card-name a')
        print(f"The article author is: {author}")
        # author_name_selector = '.wp-block-tc23-author-card-name a'
        # author_name = await page.inner_text(author_name_selector)
        # print(f"Author Name: {author_name}")
        
        # 4.3 Retrieve and print the date of the article
        date = await page.inner_text('.wp-block-post-date time')
        print(f"The article publish date is: {date}")
        # time_selector = '.wp-block-post-date time'
        # date_time_text = await page.inner_text(time_selector)
        # print(f"The article publish date is: {date_time_text}")

        # Delay further actions by 5 seconds to ensure all dynamic content is loaded,
        # useful in pages with elements that load after the initial page load
        await asyncio.sleep(5)
        
        # Close the browser once the tasks are completed
        await browser.close()

async def main():
    # url = 'https://twitter.com/OldRowSwig/status/1732112446943269347?s=20'
    url = 'https://techcrunch.com/2024/04/20/boston-dynamics-unveils-a-new-robot-controversy-over-mkbhd-and-layoffs-at-tesla/'
    await get_article_details(url)

if __name__ == "__main__":
    asyncio.run(main())
