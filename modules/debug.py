import os
import shutil

# if os.path.isdir('novel'):
#     print('"/novel" existe!')
# else:
#     print('"/novel" não existe!')

# if os.path.isdir('novels'):
#     print('tudo ok')
#     pass
# else:
#     os.mkdir('./novels')
#     print('/novels criada')

# if os.path.isdir('./novels/dxd'):
#     print('diretório dxd existe!')
# else:
#     print('diretório dxd não existe')
#     os.mkdir('./novels/dxd')

def cleanDiretory():
    dirPath = './novels'
    if os.path.isdir(dirPath):
        if len(os.listdir(dirPath)) != 0:
            # print('tem arquivos no diretório')
            try:
                shutil.rmtree(dirPath)
            except OSError as e:
                print(f"Error:{ e.strerror}")
        else:
            # print('diretório vazio')
            os.rmdir('./novels')
    else:
        pass

if __name__ == '__main__':
    cleanDiretory()