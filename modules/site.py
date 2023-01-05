import requests
from bs4 import BeautifulSoup

def filterUrl(_url):
    _response = requests.get(_url)
    _content = _response.content
    _site = BeautifulSoup(_content, 'html.parser')

    return _site