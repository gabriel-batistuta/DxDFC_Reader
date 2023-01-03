from modules import url, site, img, title, link, novel

def chamaModulos():
    _url = url.pedirUrl()
    _site = site.trataUrl(_url)
    _img = img.pegaImg(_site)
    _title = title.getTitle(_site)
    _routeImg = img.downloadImage(_img, _title)
    _links = link.pegaCapitulos(_site)
    _novel = novel.writeNovel(_links, _title)
    return _url, _site, _img, _title, _routeImg, _links, _novel

url, site, img, title, routeImg, links, novel = chamaModulos()

# site = BeautifulSoup(requests.get(input('Digite a URL com o volume a novel DxD: ')).content, 'html.parser')

print(f'\n\nSITE: {url}\n\nNOVEL: {title}\n\nLINK DA IMAGEM: {img}\n\nIMAGEM em: {routeImg}\n\nNOVEL em: {novel}')