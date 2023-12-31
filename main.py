import modules
import time
import os

CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"

def callModules(resp):

    start_time = time.time()

    url = modules.getUrl()
    os.system('clear || cls')
    all_volumes_site = modules.filterUrl(url)
    listVolumes = modules.getLinks(all_volumes_site)
    for volume in listVolumes:
        volumeSite = modules.filterUrl(volume['url'])
        title = modules.getTitle(volumeSite)
        modules.makeFolder(title)
        modules.writeHeader(volumeSite, title)
        img = modules.getImageCover(volumeSite)
        modules.downloadImageCover(img, title)
        modules.download_all_images(volume['links_chapters'], title)
        modules.writeSumary(volume['title_chapters'], title)
        modules.writeChapter(volume['links_tags'], title, img, resp)

    end_time = time.time()
    elapsed_time = int(end_time - start_time)
    print(f'Tempo decorrido: {CYAN}{elapsed_time}{RESET}s')

if __name__ == '__main__':

    resp = modules.menu()
    callModules(resp)
    print(f'\n\nAll Novels saved in: {GREEN}/novels')