import random
import time
import sys
numeros = []


def juntar(lst, string):
    lst = str(string).join(str(x) for x in lst)
    return lst


def sortear(lista):
    print('A gerar valores para a lista: ', end='')
    for c1 in range(0, 5):
        n = random.randint(0, 100)
        lista += [n]
        sys.stdout.flush()
        time.sleep(1)
        if c1 < 4:
            print(n, end=', ')
        else:
            print(n)


def somapar(lista):
    s = 0
    np = []
    for i1 in lista:
        if i1 % 2 == 0:
            s += i1
            np += [i1]
    print(f'''Dos valores gerados, {len(np)} eram pares ({juntar(np, ', ')}) e a sua soma é {s}''')


sortear(numeros)
somapar(numeros)