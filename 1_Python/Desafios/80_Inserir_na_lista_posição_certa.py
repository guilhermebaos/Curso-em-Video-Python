r = 'a'
numeros = [1.1]
c2 = 0


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


while r != 'N':
    c2 += 1
    n = 'a'
    while not isfloat(n):
        n = str(input('\nEscreve um número: ')).strip()
        if not isfloat(n):
            print('Escrve só o número!')
        else:
            n = float(n)
    r = str(input('Queres inserir outro valor [S/N]? ')).strip().upper()
    for c1 in range(0, len(numeros)):
        if n < numeros[int(c1)]:
            numeros.insert(int(c1), n)
        if c1 + 1 == len(numeros):
            numeros.append(n)
        if c2 == 1:
            numeros.remove(1.1)
print(', '.join(str(x) for x in numeros))
