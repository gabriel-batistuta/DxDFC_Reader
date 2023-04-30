def getLinks(_site):
    _caps = _site.find('div', attrs={'class': 'post-body entry-content float-container'})

    _links = _caps.find_all('a')
    _keys = ['Download', 'PDF', 'pdf', 'ePub', 'EPUB', 'epub']
    
    for _key in _keys:
        for _link in _links:
            if (_key.lower() in _link.text.lower()) == True:
                try:
                    _links.remove(_link)
                except:
                    pass

    return _links