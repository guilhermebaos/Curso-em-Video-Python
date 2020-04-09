def entrelin(var):
    print('-' * 20)
    print(f'{str(var):^20}')
    print('-' * 20)


entrelin('NOVO PROGRAMA')


def soma(a, b):
    s = a + b
    print(f'A soma dos números {a} e {b} é {s}')


soma(1, 2)
soma(10, 213)
soma(a=4, b=5)
soma(b=9, a=7)
# soma(a=9, 3) -> Erro


def contador(* num):
    print(f'''O conjunto: [{', '.join(str(x) for x in num)}] tem {len(num)} elementos''')


contador(1, 2, 3)
contador('r', 'y', 2, 1, 'ggg', '')


def dobro(lst):
    for c1 in range(0, len(lst)):
        lst[c1] *= 2


valores = [1, 2]
dobro(valores)
print(f'''O dobro dos valores é {', '.join(str(x) for x in valores)}''')
