def writeHeader(_site, _title):
    div = _site.find('div', attrs={'class': 'header-widget'})
    _blog = div.find('a', attrs={'href': 'https://highschooldxdfc.blogspot.com/'})
    _blogLink = _blog['href']
    _blog = _blog.text
    _aboutBlog = div.find('p')
    _aboutBlog = _aboutBlog.text

    _folderBlog = open(f'novels/{_title}/README.txt','a+')
    _folderBlog.write(f'{_blog}\n{_aboutBlog}\n{_blogLink}')
