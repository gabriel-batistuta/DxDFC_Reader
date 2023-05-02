def writeSumary(links, title):

    with open(f'novels/{title}/sumary - {title}.txt','a+') as file:
        for link in links:
            file.write(f'{link.text}\n\n')
        file.close()