s = 0
for c1 in range(0, 6):
    n = int(input('Escreva um número: '))
    if n % 2 == 0:
        s += n
print('A soma dos números pares que escreveste é {}'.format(s))
