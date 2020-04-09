ic = 0
mi = 0
for c1 in range(0, 4):
    print('{}ª pessoa '.format(c1 + 1))
    n = str(input('Teu nome- '))
    i = int(input('Sua idade- '))
    g = str(input('Seu género (M / F)- '))
    if i > ic and g == 'M':
        ic = i
        ni = n
    elif ic == 0:
        ni = 'Não há homens no grupo'
    if i < 20 and g == 'F':
        mi += 1
print('''O nome do homem mais velho é: {}
Há {} mulheres com menos de 20 anos'''.format(ni, mi))
