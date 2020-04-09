def half(num=0, euro=False):
    num = num * 0.5
    if euro:
        num = float(num)
        string = f'{num:.2f}€'
        string_org = string.replace('.', ',')
    else:
        string_org = num
    return string_org


def double(num=0, euro=False):
    num = num * 2
    if euro:
        num = float(num)
        string = f'{num:.2f}€'
        string_org = string.replace('.', ',')
    else:
        string_org = num
    return string_org


def aumentar(preco=0, num=0, euro=False):
    preco_aum = preco * ((num + 100)/100)
    if euro:
        preco_aum = float(preco_aum)
        string = f'{preco_aum:.2f}€'
        string_org = string.replace('.', ',')
    else:
        string_org = preco_aum
    return string_org


def diminuir(preco=0, num=0, euro=False):
    preco_des = preco * ((100 - num)/100)
    if euro:
        preco_des = float(preco_des)
        string = f'{preco_des:.2f}€'
        string_org = string.replace('.', ',')
    else:
        string_org = preco_des
    return string_org


def format_euro(num=0):
    num = float(num)
    string = f'{num:.2f}€'
    string_org = string.replace('.', ',')
    return string_org
