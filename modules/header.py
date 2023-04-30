def writeHeader(site, title):
    div = site.find('div', attrs={'class': 'header-widget'})
    blog = div.find('a', attrs={'href': 'https://highschooldxdfc.blogspot.com/'})
    blogLink = blog['href']
    blog = blog.text.strip()
    aboutBlog = div.find('p')
    aboutBlog = aboutBlog.text.strip()

    folderBlog = open(f'novels/{title}/README.txt','a+')
    folderBlog.write(f'{blog}\n{aboutBlog}\n{blogLink}')
