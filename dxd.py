from modules import url, site, img, title, link, novel, debug

def callModules():
    # debug.cleanDiretory()
    _url = url.getUrl()
    _site = site.trataUrl(_url)
    _img = img.pegaImg(_site)
    _title = title.getTitle(_site)
    _links = link.pegaCapitulos(_site)
    _novel = novel.writeNovel(_links, _title)
    _routeImg = img.downloadImage(_img, _title)
    return _url, _site, _img, _title, _links, _novel, _routeImg

url, site, img, title, links, novel, routeImg = callModules()

# site = BeautifulSoup(requests.get(input('Digite a URL com o volume a novel DxD: ')).content, 'html.parser')

print(f'\n\nSITE: {url}\n\nNOVEL: {title}\n\nLINK DA IMAGEM: {img}\n\nIMAGEM em: {routeImg}\n\nNOVEL em: {novel}')