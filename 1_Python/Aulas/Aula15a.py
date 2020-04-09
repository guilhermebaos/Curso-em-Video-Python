n = s = 0
while True:
    n = int(input('Escreve um número: '))
    if n == 999:
        break
    s += n
# print('A soma é {}'.format(s))
print(f'A soma é {s}')
