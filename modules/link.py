def pegaCapitulos(_site):
    _caps = _site.find('div', attrs={'class': 'post-body entry-content float-container'})

    _links = _caps.find_all('a')

    _links.pop()

    for i, _link in enumerate(_links):
        if i != 0:
            print(f'\n\nCAPÍTULO {i}: {_link.text}\n\n')

    return _links

    # for i, cap in enumerate(caps):
    #     print(f'{i}:\n {cap.text}\n\n')

    