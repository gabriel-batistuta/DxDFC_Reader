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