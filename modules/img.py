import requests
import sys
import os

def getImg(_site):
    _imgs = _site.find_all('img')
    
    _imagem = _imgs[0]['src']
    print(_imagem)
    return _imagem

def downloadImage(_img, _title):
    try: 
        with open(f'novels/{_title}/cover - {_title}.jpg', 'wb') as file:
            data = requests.get(_img)
            file.write(data.content)
            file.close()

        currentDirectory = os. getcwd()
        _routeImg = f'{currentDirectory}/novels/{_title}/cover - {_title}.jpg'

        return _routeImg
    
    except:
        erro = sys.exc_info()
        print("Ocorreu um erro com o download da imagem: ", erro)