"""
This script is to show the main factors of requests and how to use it with an HTML Parser
HTML Parser to use is BeautifulSoup: One of the best xml and html parsers
"""

from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import sys , argparse


# to install Beautiful Soup: File ---> Settings --> Project Interpreter and "add package"

if __name__ == '__main__':
    for url in sys.argv[1:]:
        # Add https to urls without protocol with layer
        if not url.lower().startswith('http'):
            url = f"https://en.wikipedia.org/wiki/Turing_(disambiguation)?search?q=turing"
        else:
            url = f'https://en.wikipedia.org/wiki/Florida_Gulf_Coast_(disambiguation)'


        # Gets website url and provides response
        # If error - exists with exception
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as httperr:
            print(f'HTTP error: {httperr}')
            sys.exit(1)
        except Exception as err:
            print(f"Something went really wrong!: {err}")
            sys.exit(1)

        # Open our page with beautiful soup
        soup = BeautifulSoup(response.text,'html.parser')

        #
        for link in soup.findAll("a"):
            print(link.text)
