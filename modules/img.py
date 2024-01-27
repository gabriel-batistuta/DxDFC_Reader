import requests
from bs4 import BeautifulSoup
import sys

def getImageCover(site):
    div = site.find('div', class_='separator')
    link = div.find('a')
    
    imagem = link['href']
    
    return imagem

def downloadImageCover(img, title):
    try: 
        with open(f'novels/{title}/cover - {title}.jpg', 'wb') as file:
            data = requests.get(img)
            file.write(data.content)
            file.close()
    except:
        erro = sys.exc_info()
        print(f'{__name__} : {erro}')

def download_all_images(links_chapters, title):
    novel_ilustrations = []

    for link in links_chapters:
        html_content = BeautifulSoup(requests.get(link).content, 'html.parser')
        main_content = html_content.find('div', attrs={'class':'post-body-container'})
        divs = main_content.find_all('div', {'class': 'separator'})
        if len(divs) > 0:
            for div in divs:
                link = div.find('a')
                if link is not None and link.find('img'):        
                    link = div.find('a')
                    img_tag = link.find('img')
                    img_tag['src'] = link['href']
                    if img_tag['src'] not in novel_ilustrations:
                        novel_ilustrations.append(img_tag['src'])

    for i, ilustration in enumerate(novel_ilustrations):
        try:
            if 'png' in ilustration:
                with open(f'novels/{title}/ilustrations/image {i+1} - {title}.png', 'wb') as file:
                    data = requests.get(ilustration)
                    file.write(data.content)
                    file.close()
            elif 'jpeg' in ilustration:
                with open(f'novels/{title}/ilustrations/image {i+1} - {title}.jpeg', 'wb') as file:
                    data = requests.get(ilustration)
                    file.write(data.content)
                    file.close()
            else:
                with open(f'novels/{title}/ilustrations/image {i+1} - {title}.jpg', 'wb') as file:
                    data = requests.get(ilustration)
                    file.write(data.content)
                    file.close()
        except:
            erro = sys.exc_info()
            print(f'{__name__} : {erro}')