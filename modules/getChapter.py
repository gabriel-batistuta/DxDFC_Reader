import requests
from bs4 import BeautifulSoup
import os
import jinja2
import pdfkit
import platform
import PyPDF2

def writeChapter(links, title, resp):

    def getSiteChapter(link):
        href = link['href']
        html = requests.get(href)
        site = BeautifulSoup(html.content, 'html.parser')

        return site

    def getDivChapter(site):
        divChapter = site.find('div', attrs={'class': 'post-content container'})
        divChapter = site.find('div', attrs={'class': 'post-body entry-content float-container'})

        return divChapter
    
    def getTitleChapter(link):
        titleChapter = link.text.strip()

        return titleChapter

    def getPublicationDate(site):
        date = site.find('time', attrs={'class': 'published'})
        date = date.text.strip()

        return date

    def getChapterText(divChapter):
        chapterText = divChapter.text

        return chapterText

    def writeChapterForFormat(resp):
        if resp == 'txt':
            with open(f'./novels/{title}/{title}.txt', 'a+') as chapter:
                chapter.write(f'{titleChapter}\n\n')
                chapter.write(f'{date}\n\n')
                chapter.write(f'{chapterText}\n\n')

        elif resp == 'pdf':
            with open('./template/template.html','r') as file:
                data = file.read()
                with open(f'./novels/{title}/{titleChapter}.html', 'x') as file:
                    file.write(f'{data}')
            
            context = {
                'titleChapter':titleChapter,
                'date':date,
                'chapterText':chapterText,
                'divChapter':divChapter
            }

            template_loader = jinja2.FileSystemLoader(f'./novels/{title}')
            template_env = jinja2.Environment(loader=template_loader)
            templ = template_env.get_template(f'{titleChapter}.html')
            output_text = templ.render(context)

            try:
                if platform.system() == 'Linux':
                    path_wkhtmltopdf = os.popen('which wkhtmltopdf').read() 
                    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
                else:
                    path_wkhtmltopdf = os.popen('where wkhtmltopdf').read() 
                    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
            except:
                config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
        
            pdfkit.from_string(output_text, f'./novels/{title}/{titleChapter}.pdf', configuration=config, css=f'./templates/template.css', options={ 'enable-local-file-access': None })

    def joinPdfs():
        
        def getIndexChapters(path=f'./novels/{title}/sumary - {title}.txt'):
            indexChapters = []

            with open(path, 'r') as file:
                for chapter in file.readlines():
                    if chapter != '\n':
                        if '\n' in chapter:
                            chapter = chapter.replace('\n','')
                            indexChapters.append(chapter)
                        elif '\n' not in chapter:
                            indexChapters.append(chapter)

            return indexChapters

        def joinPdfsByIndex(indexChapters):
            pathPdfFolder = f'./novels/{title}'
            merger = PyPDF2.PdfMerger()
            fileList = os.listdir(pathPdfFolder)

            concluid = []

            for index in indexChapters:
                for file in fileList:
                    if '.pdf' in file:
                        if index + '.pdf' == file:
                            concluid.append(file)
                            merger.append(f'{pathPdfFolder}/{file}')

            merger.write(f'{pathPdfFolder}/{title}.pdf')

        indexChapters = getIndexChapters()
        joinPdfsByIndex(indexChapters)

    for link in links:
        site = getSiteChapter(link)
        titleChapter = getTitleChapter(link)
        divChapter = getDivChapter(site)
        date = getPublicationDate(site)
        chapterText = getChapterText(divChapter)
        writeChapterForFormat(resp)
        if resp == 'pdf':
            joinPdfs()

    def log():
        currentDirectory = os. getcwd()
        novel = f'{currentDirectory}/novels/{title}'
        return novel
    
    return log()