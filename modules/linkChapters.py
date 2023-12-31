from requests import get
from bs4 import BeautifulSoup

def getLinks(site):

    def getAllVolumes(site):
        divAllContent = site.find('div', attrs={'class':'post-body-container'})
        allLinksTags = divAllContent.find_all('a')
        allLinksTags = list(filter(lambda x: 'https://highschooldxdfc.blogspot.com/p/' in x.get('href'), allLinksTags))        
        allVolumesObjects = []

        for i in range(len(allLinksTags)):
            volume = {
                'name':allLinksTags[i].text,
                'url':allLinksTags[i].get('href')
            }
            allVolumesObjects.append(volume)
        
        return allVolumesObjects

    def getLinksInVolume(url):
        site = BeautifulSoup(get(url).content, 'html.parser')
        caps = site.find('div', attrs={'class': 'post-body entry-content float-container'})
        links = caps.find_all('a')
        
        return links

    def filterLinksCaps(links):
        keys = ['DOWNLOAD', 'PDF', 'EPUB', 'JPG', 'MEGA', 'JPEG']
        links = list(filter(lambda x: x.get("href"), links))
        for key in keys:
            links = list(filter(lambda x: key.lower() not in x["href"].lower(), links))

        return links
    
    def getLinksInTags(linksTags):
        links = []
        for i in range(len(linksTags)):
            links.append(linksTags[i].get('href').strip())
            
        return links

    def removeRepeatedCaps(links):
        listNoReapeated = []
        for link in links:
            if link['href'] not in str(listNoReapeated):
                listNoReapeated.append(link)

        return listNoReapeated
        
    def getTitlesCaps(linkTags):
        titleChapters = []
        for i in range(len(linkTags)):
            titleChapters.append(linkTags[i].text)
        
        # print(titleChapters)
        # print('------------------')
        return titleChapters

    allVolumesObjects = getAllVolumes(site)
    
    listVolumes = []

    for volumeObject in allVolumesObjects:
        linksTags = getLinksInVolume(volumeObject['url'])
        linksTags = filterLinksCaps(linksTags)
        linksTags = removeRepeatedCaps(linksTags)
        titleChapters = getTitlesCaps(linksTags)
        linksChapters = getLinksInTags(linksTags)

        # verifica se o volume tem alguma capítulo pra ler
        if len(linksChapters) > 0:
            volume_obj = {
                'name' : volumeObject['name'],
                'url' : volumeObject['url'],
                'links_tags':linksTags,
                'links_chapters' : linksChapters,
                'title_chapters' : titleChapters
            }
            listVolumes.append(volume_obj)
            # print(volume_obj)
    
    # debuging ;)
    '''
    for i in links:
        print(f'\n\n{i["href"]}\n\n')               
    '''

    return listVolumes