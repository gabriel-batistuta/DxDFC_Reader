import requests
from bs4 import BeautifulSoup
import os
from jinja2 import Template
import pdfkit
import platform
from tqdm import tqdm
from requests_html import HTMLSession

def writeChapter(links:list, title:str, img:str, resp:str):

    def getSiteChapter(link):
        
        session = HTMLSession()
        r = session.get(link['href'])
        r.html.render()
        html = r.html.html

        # html = requests.get(link['href']).content
        site = BeautifulSoup(html, 'html.parser')

        return site

    def getDivChapter(site):
        divChapter = site.find('div', attrs={'class': 'post-body entry-content float-container'})

        def ajustImages(soup):
            divs = soup.find_all('div', {'class': 'separator'})
            if type(divs) == list and len(divs) > 0:
                for div in divs:
                    link = div.find('a')
                    if link is not None and link.find('img'):
                        img_tag = link.find('img')
                        img_tag2 = img_tag
                        img_tag2['src'] = link['href']
                        img_tag2['width'] = img_tag2['data-original-width']
                        img_tag2['height'] = img_tag2['data-original-height']
                        soup.find(lambda tag: tag.name == 'img' and str(img_tag) == str(tag)).replace_with(img_tag2)

            return soup

        divChapter = ajustImages(divChapter)

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

    def mountHtmlDiv(titleChapter, divChapter, date, chapterText):
        with open('./templates/template.html','r') as file:
            templateString = file.read()
            
            context = {
                'titleChapter':titleChapter,
                'date':date,
                'chapterText':chapterText,
                'divChapter':divChapter
            }

            templateDiv = Template(templateString)
            templateDiv = templateDiv.render(context)
        
        return templateDiv

    def writeChapterForFormat(resp, startHtml):
        if resp == 'txt':
            with open(f'./novels/{title}/{title}.txt', 'a+') as chapter:
                chapter.write(f'{titleChapter}\n\n')
                chapter.write(f'{date}\n\n')
                chapter.write(f'{chapterText}\n\n')

        elif resp == 'pdf':
            endHtml = '</body></html>'
            cssPath = './templates/template.css'
            
            if platform.system() == 'Windows':
                path_wkhtmltopdf = os.popen('where wkhtmltopdf').read() 
                config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
            else:
                path_wkhtmltopdf = os.popen('which wkhtmltopdf').read() 
                config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
            # config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
                    
            pdfkit.from_string(startHtml+endHtml, f'./novels/{title}/{title}.pdf', configuration=config, css=cssPath, options={
                'enable-local-file-access': None, 
                'encoding': 'UTF-8',
                '--image-quality': 100
            })

    startHtml = f'<html><head><meta http-equiv="Content-type" content="text/html; charset=utf-8"/></head><body><img src="{img}" alt="main-picture" class="cover">'
    with tqdm(total=len(links)) as progress_bar:
        progress_bar.desc=f'download {title}'
        progress_bar.colour='blue'

        for link in links:
            site = getSiteChapter(link)
            titleChapter = getTitleChapter(link)
            date = getPublicationDate(site)
            divChapter = getDivChapter(site)
            chapterText = getChapterText(divChapter)
            if resp == 'pdf':
                templateDiv = mountHtmlDiv(titleChapter, divChapter, date, chapterText)
                startHtml += templateDiv
                progress_bar.update(1)
            elif resp == 'txt':
                writeChapterForFormat(resp, startHtml)
                progress_bar.update(1)
        progress_bar.close()
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        
    writeChapterForFormat(resp, startHtml)