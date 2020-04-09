from termcolor import cprint, colored
l1 = float(input(colored('Escreve o comprimento de um segmento de reta: ', 'blue')))
l2 = float(input(colored('Escreve o comprimento de outro segmento de reta. ', 'blue')))
l3 = float(input(colored('Escreve o comprimento de mais um segmento de reta: ', 'blue')))
if l1 + l2 <= l3 or l2 + l3 <= l1 or l3 + l1 <= l2:
    cprint('Os segmentos de reta não podem formar um triângulo!', 'red')
else:
    if l1 == l2 == l3:
        t = 'equilátero'
    elif l1 == l2 or l2 == l3 or l3 == l1:
        t = 'isósceles'
    else:
        t = 'escaleno'
    cprint('Os segmentos de reta formam um triãngulo {}!'.format(t), 'green')
