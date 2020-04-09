import time
import sys


def contador(i, f, p):
    p = abs(p)
    if p == 0:
        p = 1
    if f < i:
        p = p * -1
    contagem = []
    contagem += [i]
    while True:
        i += p
        contagem += [i]
        if i >= f and p > 0:
            break
        elif i <= f and p < 0:
            break
    return contagem


def tit(string):
    t = int(len(string) / 2 + 2)
    return f'''{'-=' * t}
{str(string):^{t * 2}}
{'-=' * t}'''


print(tit('CONTADOR'))
print('')
for c1 in range(0, 2):
    if c1 == 0:
        a = 1
        b = 10
        c = 1
    else:
        a = 10
        b = 0
        c = 2
    print(f'''\nContagem de {a} até {b}, de {c} em {c}:''')
    tam = int(len(contador(a, b, c)))
    for c2 in range(0, tam):
        print(f'''{contador(a, b, c)[c2]}-> ''', end='')
        sys.stdout.flush()
        time.sleep(0.4)
    print('FIM')
print('-=' * 20)
print('\nContagem personalizada:')
ap = float(input('Começo da contagem: '))
bp = float(input('Fim da contagem: '))
cp = float(input('Tamanho do passo: '))
tam = int(len(contador(ap, bp, cp)))
for c3 in range(0, tam):
    print(f'''{contador(ap, bp, cp)[c3]}-> ''', end='')
    sys.stdout.flush()
    time.sleep(0.4)
