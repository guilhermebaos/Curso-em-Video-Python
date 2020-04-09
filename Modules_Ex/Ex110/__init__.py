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


def increase(price=0, num=0, euro=False):
    preco_aum = price * ((num + 100)/100)
    if euro:
        preco_aum = float(preco_aum)
        string = f'{preco_aum:.2f}€'
        string_org = string.replace('.', ',')
    else:
        string_org = preco_aum
    return string_org


def decrease(price=0, num=0, euro=False):
    preco_des = price * ((100 - num)/100)
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


def price_manipulation(num, increase_, decrease_):
    a = len('Manipulação do preço')
    p1 = f'Preço analisado: {format_euro(num)}'
    p2 = f'Dobro do preço: {format_euro(num * 2)}'
    p3 = f'Metade do preço: {format_euro(num / 2)}'
    p4 = f'Preço com aumento de {increase_}%: {format_euro(num * (100 + increase_) / 100)}'
    p5 = f'Preço com desconto de {decrease_}%: {format_euro(num *(100- decrease_) / 100)}'
    return f"{'-=' * a}\n{str('Manipulação do preço'):^{a * 2}}\n{'-=' * a}\n{p1}\n\n" \
        f"{p2}\n{p3}\n{p4}\n{p5}\n{'-=' * a}"
