from modules import linkChapters, sumary, url, site, img, title, debug, getChapter, folder, header
import os


def callModules():
    # debug.cleanDiretory()
    _url = url.getUrl()
    _site = site.filterUrl(_url)
    _title = title.getTitle(_site)
    folder.makeFolder(_title)
    header.writeHeader(_site, _title)
    _img = img.getImg(_site)
    _links = linkChapters.getLinks(_site)
    _sumary = sumary.writeSumary(_links, _title)
    _novel = getChapter.getText(_links , _title)
    _routeImg = img.downloadImage(_img, _title)
    return _url, _site, _img, _title, _links, _sumary, _novel, _routeImg

url, site, img, title, links, sumary, novel, routeImg = callModules()

# site = BeautifulSoup(requests.get(input('Digite a URL com o volume a novel DxD: ')).content, 'html.parser')

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

os.system('clear')

print(f'\n\n{RED}SITE:{RESET} {url}\n\n{CYAN}NOVEL:{RESET} {title}\n\n{RED}LINK DA IMAGEM:{RESET} {img}\n\n{CYAN}IMAGEM em:{RESET} {routeImg}\n\n{RED}SUMÁRIO em:{RESET} {sumary}\n\n{CYAN}NOVEL em:{RESET} {novel}\n')