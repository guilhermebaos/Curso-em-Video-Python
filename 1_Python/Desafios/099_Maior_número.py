import random
import time


def tit(string):
    t = int(len(string) / 2 + 2)
    return f'''{'-=' * t}
{str(string):^{t * 2}}
{'-=' * t}'''


def juntar(lst, string):
    lst = str(string).join(str(x) for x in lst)
    return lst


def maior(*num):
    if len(num) == 0:
        v1 = 'ERRO, NENHUM VALOR RECEBIDO'
        v2 = 0
        v3 = '-'
    else:
        v1 = juntar(num, ', ')
        v2 = len(num)
        v3 = max(num)
    print(f'''{'-=' * 20}
Foram recebidos os valores {v1} ({v2} valores ao todo)
O maior desses valores é {v3}''')
    return None


for c1 in range(0, 2):
    a = random.randint(0, 10)
    b = random.randint(1, 13)
    c = random.randint(2, 8)
    dt = random.choice([True, False])
    et = random.choice([True, False])
    if dt:
        d = random.randint(4, 12)
    else:
        d = -2
    if et:
        e = random.randint(1, 11)
    else:
        e = 0
    maior(a, b, c, d, e)
    time.sleep(0.5)
maior(1)
time.sleep(0.5)
maior()
time.sleep(0.5)
maior(1, 9, 4, 5, 6, 34, 5, 12, 34, 2, 34, 12, 3)
time.sleep(0.5)
print('-=' * 20)
ap = float(input('Escreve um número: '))
bp = float(input('Escreve um número: '))
cp = float(input('Escreve um número: '))
dp = float(input('Escreve um número: '))
ep = float(input('Escreve um número: '))
maior(ap, bp, cp, dp, ep)
