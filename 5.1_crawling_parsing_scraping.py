from bs4 import BeautifulSoup

"""
1. Crawling: Fetching the HTML content
A simple example of a crawled HTML content (in real scenario, this would be fetched from the web)
"""
html_content = """
<html>
    <head><title>Example Web Page</title></head>
    <body>
        <h1>Welcome to Example Web Page</h1>
        <p>This is a sample web page for demonstration.</p>
        <div id="products">
            <h2>Products</h2>
            <ul>
                <li data-price="10">Product 1 - $10</li>
                <li data-price="20">Product 2 - $20</li>
                <li data-price="30">Product 3 - $30</li>
            </ul>
        </div>
    </body>
</html>
"""

"""
2. Parsing
Using BeautifulSoup to parse the HTML content to make it understandable and navigable
"""
soup = BeautifulSoup(html_content, 'html.parser')
print(soup)

"""
3. Scraping
Scraping specific data: Extracting product names and prices based on the understanding of HTML structure
"""
products = soup.select('#products ul li')
for product in products:
    name = product.text
    price = product.attrs['data-price']
    print(f'{name}: {price}')