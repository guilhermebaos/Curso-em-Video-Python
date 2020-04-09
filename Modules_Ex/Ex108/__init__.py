def half(num=0):
    return num * 0.5


def double(num=0):
    return num * 2


def aumentar(preco=0, num=0):
    return preco * ((num + 100)/100)


def diminuir(preco=0, num=0):
    return preco * ((100 - num)/100)


def euro(num=0):
    num = float(num)
    string = f'{num:.2f}€'
    string_org = string.replace('.', ',')
    return string_org
