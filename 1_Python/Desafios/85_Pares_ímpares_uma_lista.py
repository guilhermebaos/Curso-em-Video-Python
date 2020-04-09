pares = []
impares = []
numeros = [pares, impares]
for c1 in range(0, 7):
    while True:
        n = str(input('Escreve um número: ')).strip()
        if n.isnumeric():
            n = int(n)
            break
        else:
            print('Escreve só o número!\n')
    if n % 2 == 0:
        pares += [n]
    elif n % 2 == 1:
        impares += [n]
pares.sort()
impares.sort()
pares = ', '.join(str(x) for x in pares)
impares = ', '.join(str(x) for x in impares)
print(f'Os números pares são: {pares}')
print(f'Os números ímpares são: {impares}')
