n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('A sua média é de {}'.format(m))
if m < 5:
    print('Está reprovado!')
elif m > 7:
    print('Foi aprovado!')
else:
    print('Tem de ir para recuperação!')
