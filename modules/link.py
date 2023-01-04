def pegaCapitulos(_site):
    _caps = _site.find('div', attrs={'class': 'post-body entry-content float-container'})

    _links = _caps.find_all('a')

    _keys = ['Download', 'PDF', 'pdf', 'ePub', 'EPUB', 'epub']

    _caps = []

    for _link in _links:
         _caps.append(_link.text)

    _count = 0

    for _key in _keys:
        for _cap in _caps:
            print(f'[{_key}] in [{_cap}] == ')
            if _key in _cap:
                print([_key in _cap],'\n\n')
                _count += 1
            else:
                print('pass\n\n')
                
    _count=_count/2
    # print(f'_count: {_count}')

    _links.pop(int(_count))

    # for i, _link in enumerate(_links):
    #     if i != 0:
    #         print(f'\n\nCAPÍTULO {i}: {_link.text}\n\n')

    return _links

    # for i, cap in enumerate(caps):
    #     print(f'{i}:\n {cap.text}\n\n')

    