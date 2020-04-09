n1 = int(input('Escreve um valor:'))
n2 = int(input('Escreve outro número:'))
s = n1 + n2
u = n1 - n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
print('O resultado da soma desses números é: {}, a subtração é: {}'.format(s, u), end=' ')
print('a divisão é: {:.3f}, a divisão inteira é: {} e o 1º elevado ao segundo é: {}'.format(d, di, p))
