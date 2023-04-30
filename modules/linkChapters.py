def getLinks(site):
    def getLinksInSite(site):
        caps = site.find('div', attrs={'class': 'post-body entry-content float-container'})
        links = caps.find_all('a')
        
        return links

    def filterLinksCaps(links):
        keys = ['DOWNLOAD', 'PDF', 'EPUB', 'JPG', 'MEGA', 'JPEG']
        for key in keys:
            links = list(filter(lambda x: key.lower() not in x["href"], links))

        return links
    
    def removeRepeatedCaps(capList):
        # return list(dict.fromkeys(capList))
        listNoReapeated = []
        for i in capList:
            link = i["href"].strip()
            if link not in str(listNoReapeated):
                listNoReapeated.append(i)

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