import os

def writeNovel(_links, _title):
    file = open(f'novel/{_title}.txt','a+')
    for i, _link in enumerate(_links):
        if i != 0:
            file.write(f'CAPÍTULO {i}: {_link.text}\n\n')
    file.close()

    currentDirectory = os. getcwd()

    _novel = f'{currentDirectory}/novel/{_title}.txt'
    return _novel