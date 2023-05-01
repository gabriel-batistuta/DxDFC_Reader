import requests
import sys
import os

def getImg(site):
    imgs = site.find_all('img')
    
    imagem = imgs[0]['src']

    def log():
        print(imagem)

        return imagem
    
    return log()

def downloadImage(img, title):
    try: 
        with open(f'novels/{title}/cover - {title}.jpg', 'wb') as file:
            data = requests.get(img)
            file.write(data.content)
            file.close()

        currentDirectory = os. getcwd()
        routeImg = f'{currentDirectory}/novels/{title}/cover - {title}.jpg'

        return routeImg
    
    except:
        erro = sys.exc_info()
        print(f'{__name__} : {erro}')