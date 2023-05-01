import os

def writeSumary(links, title):
    
    def writeInSumary(links, title):
        with open(f'novels/{title}/sumary - {title}.txt','a+') as file:
            for link in links:
                file.write(f'{link.text}\n\n')
            file.close()

    def log():
        currentDirectory = os. getcwd()
        sumary = f'{currentDirectory}/novels/{title}/sumary - {title}.txt'

        return sumary
    
    writeInSumary(links, title)

    return log()