a = int(input('Escreve um ano: '))
a1 = a // 4
a2 = a1 * 4
a3 = a // 100
a4 = a3 * 100
if a2 == a:
    if a4 == a:
        print('O ano não é bissexto.')
    else:
        print('O ano {} é bissexto!'.format(a))
else:
    print('O ano {} não é bissexto.'.format(a))
