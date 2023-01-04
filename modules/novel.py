import os

def writeNovel(_links, _title):
    if os.path.isdir('./novels'):
        pass
    else:
        os.mkdir('./novels')

    if os.path.isdir(f'./novels/{_title}'):
        pass
    else:
        os.mkdir(f'./novels/{_title}')

    file = open(f'novels/{_title}/{_title}.txt','a+')
    for i, _link in enumerate(_links):
        if i != 0:
            file.write(f'CAPÍTULO {i}: {_link.text}\n\n')
    file.close()

    currentDirectory = os. getcwd()

    _novel = f'{currentDirectory}/novels/{_title}.txt'
    return _novel