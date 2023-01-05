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

    _links.pop(0)

    _file = open(f'novels/{_title}/sumary - {_title}.txt','a+')
    for _link in _links:
        _file.write(f'{_link.text}\n\n')
    _file.close()

    _currentDirectory = os. getcwd()

    _novel = f'{_currentDirectory}/novels/{_title}.txt'
    return _novel