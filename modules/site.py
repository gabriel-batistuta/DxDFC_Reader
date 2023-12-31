import requests
from bs4 import BeautifulSoup

def filterUrl(url):
    headers = {
        'userAgent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0'
    }
    response = requests.get(url, headers=headers, stream=True)
    content = response.content
    site = BeautifulSoup(content, 'html.parser')
    
    return site