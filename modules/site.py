import requests
from bs4 import BeautifulSoup

def filterUrl(url):
    response = requests.get(url)
    content = response.content
    site = BeautifulSoup(content, 'html.parser')

    return site