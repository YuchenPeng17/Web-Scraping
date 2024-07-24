"""
BeautifulSoup is a Python library used for parsing HTML and XML documents. 
It helps in navigating, searching, and modifying the parse tree (i.e., the structure of the HTML or XML document). 
Essentially, it allows you to extract data from HTML pages, such as text or links, in a straightforward and efficient manner.

In this script, we use BeautifulSoup to extract information from static HTML pages.
"""

import requests
from bs4 import BeautifulSoup

# 1. Get HTML Content
url = "https://news.ycombinator.com"
response = requests.get(url)
html_content = response.text

# 2. Parse HTML Content
soup = BeautifulSoup(html_content, 'html.parser')
"""
Create a BeautifulSoup object from HTML content.

This function takes HTML content and parses it using Python's built-in HTML parser,
resulting in a BeautifulSoup object that can be used to navigate and search the parsed HTML tree.

Parameters:
    html_content (str): A string representing the HTML content to be parsed.
    'html.parser': A string specifying the parser to use; here, Python's built-in HTML parser.

Returns:
    BeautifulSoup object: An object that represents the parsed HTML document.
"""

# 3. Extract all span elements with class "titleline" from a BeautifulSoup object.
titlelines = soup.find_all('span', class_='titleline')
"""
Retrieve all <span> elements with the class 'titleline' from the parsed HTML.

This method searches the BeautifulSoup object, `soup`, for all <span> elements that have
a class attribute with the value 'titleline'. It returns a list of all matching elements,
allowing for further manipulation or data extraction.

Parameters:
    'span': The tag name to search for within the HTML document.
    class_='titleline': The class attribute to filter the <span> elements by.

Returns:
    list: A list of BeautifulSoup Tag objects that match the search criteria.
"""

# 4. Iterate through each BeautifulSoup Tag objects and extract title and link
for titleline in titlelines:
    hyperlink_tag = titleline.find('a')
    title = hyperlink_tag.text
    link = hyperlink_tag['href']
    print(f"Title: {title}\nLink: {link}\n")