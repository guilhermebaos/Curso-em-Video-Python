l1 = float(input('Comprimento do primeiro segmento de reta: '))
l2 = float(input('Comprimento do segundo segmento de reta: '))
l3 = float(input('Comprimento do terceiro segmento de reta: '))
if l1 >= l2 + l3 or l2 >= l1 + l3 or l3 >= l2 + l1:
    print('Os segmentos não podem formar um triângulo!')
else:
    if l1 == l2 == l3:
        t = 'Equilátero'
    elif l1 == l2 or l2 == l3 or l1 == l3:
        t = 'Isósceles'
    else:
        t = 'Escaleno'
    print('Os segmentos podem formar um triângulo {}!'.format(t))
