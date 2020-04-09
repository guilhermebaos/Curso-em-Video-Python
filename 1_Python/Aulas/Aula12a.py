a = float(input('Escreve um número: '))
if a > 0:
    print('{} é um número positivo!'.format(a))
elif a < 0:
    print('{} é um número negativo!'.format(a))
else:
    print('{} não é negativo nem positivo!'.format(a))
