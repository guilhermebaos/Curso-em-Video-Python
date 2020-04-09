import urllib.request


def test_site(site='https://www.google.com/'):
    try:
        urllib.request.urlopen(site)
        print('O site está acessível!')
    except:
        print('Não conseguimos chegar ao site :(')


test_site()
