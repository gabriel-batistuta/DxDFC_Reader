import requests
from bs4 import BeautifulSoup
import os
import ssl
from urllib import request, parse, error

def getText(_links, _title):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False 
    ctx.verify_mode = ssl.CERT_NONE

    for _link in _links:
        _href = _link['href']
        html = request.urlopen(_href, context=ctx).read()
        _site_cap = BeautifulSoup(html, 'html.parser')
        print(html)
        print(_site_cap)
        _divPost = _site_cap.find('div', attrs={'class': 'post-content container'})
        _title_cap = _divPost.find('h3', attrs={'class': 'post-title entry-title'})
        _title_cap = _title_cap.text
        _cap = open(f'novels/{_title}/{_title}.txt','a+')
        _cap.write(f'{_title_cap}\n')
        _time = _divPost.find('time', attrs={'class': 'published'})
        _time = _time.text
        _cap.write(f'{_time}\n\n')
        _text = _divPost.find('div', attrs={'class': 'post-body entry-content float-container'})
        _text = _text.text
        _cap.write(f'{_text}\n\n')
        _cap.close()

    _currentDirectory = os. getcwd()
    _novel = f'{_currentDirectory}/novels/{_title}.txt'
    return _novel