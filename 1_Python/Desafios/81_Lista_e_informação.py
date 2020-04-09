import random
r = ''
numeros = []


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


while r != 'N':
    r = n = ''
    while not isfloat(n):
        n = str(input('\nEscreve um número: ')).strip()
        if not isfloat(n):
            print('Escreve só o número!')
    numeros += n
    while r not in ['S', 'N']:
        r = str(input('Queres escrever outro número [S/N]? ')).strip().upper()
        if r not in 'SN':
            print('Escreve só "S" ou "N"\n')
    print('-=' * 20)
rn = random.randint(0, 10)
ln = len(numeros)
numeros = sorted(numeros, reverse=True)
numeros = ', '.join(str(x) for x in numeros)
print(f'''Escreveste {ln} números!
Os números por ordem decrescente são: {numeros}''')
if str(rn) in numeros:
    print(f'O número {rn} está na lista!')
else:
    print(f'O número {rn} não está na lista!')
