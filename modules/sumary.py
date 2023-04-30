import os

def writeSumary(_links, _title):
    _file = open(f'novels/{_title}/sumary - {_title}.txt','a+')
    for _link in _links:
            _file.write(f'{_link.text}\n\n')
    _file.close()

    _currentDirectory = os. getcwd()

    _sumary = f'{_currentDirectory}/novels/{_title}/sumary - {_title}.txt'
    return _sumary