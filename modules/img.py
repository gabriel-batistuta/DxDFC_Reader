def baixaImg(_site):
    _img = _site.find('img')
    if _img['border'] == '0':
        _imagem = _img['src']
        return _imagem
    else:
        print('\n\nNão foi possível achar uma imagem!\n\n')