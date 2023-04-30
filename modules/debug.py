import os
import shutil

def cleanDiretory():
    dirPath = './novels'
    if os.path.isdir(dirPath):
        if len(os.listdir(dirPath)) != 0:
            try:
                shutil.rmtree(dirPath)
            except OSError as e:
                print(f"Error:{ e.strerror}")
        else:
            os.rmdir('./novels')
    else:
        pass

if __name__ == '__main__':
    cleanDiretory()