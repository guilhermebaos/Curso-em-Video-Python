def somar(a=0, b=0, c=0):
    """
        -> Uma função que permite somar três números
    :param a: 1º valor
    :param b: 2º valor
    :param c: 3º valor
    :return: None
    """
    s = a + b + c
    print(f'A soma dos valores {a}, {b}, {c} é {s}')


somar(1, 2, 3)
somar(1, 2)
somar(1)
somar()
print(somar.__doc__)
help(somar)
