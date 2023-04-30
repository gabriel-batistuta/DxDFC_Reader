import modules

def callModules():
    modules.cleanDiretory()
    _url = modules.getUrl()
    _site = modules.filterUrl(_url)
    _title = modules.getTitle(_site)
    modules.makeFolder(_title)
    modules.writeHeader(_site, _title)
    _img = modules.getImg(_site)
    _links = modules.getLinks(_site)
    _sumary = modules.writeSumary(_links, _title)
    _novel = modules.getText(_links , _title)
    _routeImg = modules.downloadImage(_img, _title)
    return _url, _site, _img, _title, _links, _sumary, _novel, _routeImg

url, site, img, title, links, sumary, novel, routeImg = callModules()

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

print(f'\n\n{RED}SITE:{RESET} {url}\n\n{CYAN}NOVEL:{RESET} {title}\n\n{RED}LINK DA IMAGEM:{RESET} {img}\n\n{CYAN}IMAGEM em:{RESET} {routeImg}\n\n{RED}SUMÁRIO em:{RESET} {sumary}\n\n{CYAN}NOVEL em:{RESET} {novel}\n')