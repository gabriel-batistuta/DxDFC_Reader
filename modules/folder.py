import os

def makeFolder(_title):
    if os.path.isdir('./novels'):
        pass
    else:
        os.mkdir('./novels')

    if os.path.isdir(f'./novels/{_title}'):
        pass
    else:
        os.mkdir(f'./novels/{_title}')

    if os.path.isdir(f'./novels/{_title}/ilustrations'):
        pass
    else:
        os.mkdir(f'./novels/{_title}/ilustrations')

def removeTemplates(title):
    path=f'./novels/{title}'
    for file in os.listdir(path):
        if '.html' in file:
            os.remove(os.path.join(path, file))

def removeNoMainPdfs(title):
    path=f'./novels/{title}'
    for file in os.listdir(path):
        if '.pdf' in file and file != f'{title}.pdf':
            os.remove(os.path.join(path, file))