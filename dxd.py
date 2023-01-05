from modules import url, site, img, title, link, novel, debug
import os


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

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

os.system('clear')

print(f'\n\n{RED}SITE:{RESET} {url}\n\n{CYAN}NOVEL:{RESET} {title}\n\n{RED}LINK DA IMAGEM:{RESET} {img}\n\n{CYAN}IMAGEM em:{RESET} {routeImg}\n\n{RED}NOVEL em:{RESET} {novel}')