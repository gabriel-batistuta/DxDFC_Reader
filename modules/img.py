import requests
import sys

def getImg(site):
    imgs = site.find_all('img')
    
    imagem = imgs[0]['src']
    
    return imagem

def downloadImage(img, title):
    try: 
        with open(f'novels/{title}/cover - {title}.jpg', 'wb') as file:
            data = requests.get(img)
            file.write(data.content)
            file.close()
    except:
        erro = sys.exc_info()
        print(f'{__name__} : {erro}')