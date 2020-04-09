r = ''
numeros = []
pares = []
impares = []
while r != 'N':
    r = n = ''
    while not n.isnumeric():
        n = str(input('\nEscreve um número inteiro: ')).strip()
        if not n.isnumeric():
            print('Escreve só o número!')
    numeros += str(n)
    while r not in ['S', 'N']:
        r = str(input('Queres escrever outro número? ')).strip().upper()
        if r not in ['S', 'N']:
            print('Escreve só "S" ou "N"!\n')
    print('-=' * 20)
for x in numeros:
    if int(x) % 2 == 0:
        pares += x
    else:
        impares += x
print(f'''Os números que tu escrevste: {', '.join(str(y1) for y1 in numeros)}
Os pares: {', '.join(str(y2) for y2 in pares)}
Os ímpares: {', '.join(str(y3) for y3 in impares)}''')
