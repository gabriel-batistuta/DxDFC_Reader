def getLinks(site):
    def getLinksInSite(site):
        caps = site.find('div', attrs={'class': 'post-body entry-content float-container'})
        links = caps.find_all('a')
        
        return links

    def filterLinksCaps(links):
        keys = ['DOWNLOAD', 'PDF', 'EPUB', 'JPG', 'MEGA', 'JPEG']
        links = list(filter(lambda x: x.get("href"), links))
        for key in keys:
            links = list(filter(lambda x: key.lower() not in x["href"].lower(), links))

        return links
    
    def removeRepeatedCaps(links):
        listNoReapeated = []
        for link in links:
            href = link["href"].strip()
            if href not in str(listNoReapeated):
                listNoReapeated.append(link)

        return listNoReapeated

    links = getLinksInSite(site)
    links = filterLinksCaps(links)
    links = removeRepeatedCaps(links)

    # debuging ;)
    '''
    for i in links:
        print(f'\n\n{i["href"]}\n\n')               
    '''
    
    return links