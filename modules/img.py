import urllib.request
import sys
import os

def pegaImg(_site):
    _img = _site.find('img')
    if _img['border'] == '0':
        _imagem = _img['src']
        return _imagem
    else:
        print('\n\nNão foi possível achar uma imagem!\n\n')

def downloadImage(_img, _title):
    try: 
        urllib.request.urlretrieve(_img, f'novel/{_title}.jpg')
        currentDirectory = os. getcwd()
        _routeImg = f'{currentDirectory}/novel/{_title}.jpg'
        return _routeImg
    except:
        erro = sys.exc_info()
        print("Ocorreu um erro com o download da imagem: ", erro)