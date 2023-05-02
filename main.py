import modules
import time

CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"

def callModules(resp):

    start_time = time.time()

    modules.cleanDiretory()
    url = modules.getUrl()
    site = modules.filterUrl(url)
    title = modules.getTitle(site)
    modules.makeFolder(title)
    modules.writeHeader(site, title)
    img = modules.getImg(site)
    modules.downloadImage(img, title)
    links = modules.getLinks(site)
    modules.writeSumary(links, title)
    novel = modules.writeChapter(links, title, resp)

    end_time = time.time()
    elapsed_time = int(end_time - start_time)
    print(f'Tempo decorrido: {CYAN}{elapsed_time}{RESET}s')

    return title, novel

if __name__ == '__main__':

    resp = modules.menu()
    title, novel = callModules(resp)
    if resp == 'pdf':
        modules.removeTemplates(title)
        modules.removeNoMainPdfs(title)
    print(f'\n\n{CYAN}{title}{RESET} em: {GREEN}{novel}')