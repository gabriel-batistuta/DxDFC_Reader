def writeSumary(titleChapters, title):

    with open(f'novels/{title}/sumary - {title}.txt','a+') as file:
        for titleCap in titleChapters:
            if titleCap == titleChapters[-1]:
                file.write(f'{titleCap}')
            else:
                file.write(f'{titleCap}\n\n')
        file.close()