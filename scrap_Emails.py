# The line `import requests` is importing the `requests` library in Python. This library allows you to
# send HTTP requests and handle the responses in your code. In this specific code snippet, it is used
# to send an HTTP GET request to a webpage and retrieve its content.
import requests
# The line `from bs4 import BeautifulSoup` is importing the `BeautifulSoup` class from the `bs4`
# module. `BeautifulSoup` is a Python library used for parsing HTML and XML documents. In this code
# snippet, it is used to parse the HTML content of the webpage retrieved from the HTTP GET request.
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = "https://www.analyticsvidhya.com/blog/2023/10/small-python-projects/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    # The line `soup = BeautifulSoup(response.text, 'html.parser')` is creating a BeautifulSoup object
    # called `soup` by parsing the HTML content of the webpage.
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract data from the webpage (for example, scraping all the links)
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))

    # Print the scraped data (in this case, the links)
    for link in links:
        print(link)
else:
    print("Failed to fetch the webpage. Status code:", response.status_code)