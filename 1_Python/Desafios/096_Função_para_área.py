def area(c, l):
    a = c * l
    print(f'A área de um terreno com medida de {c}m x {l}m tem área de {a}m²')


def enterelinha(a):
    print(f'''{'-=' * 20}
{a:^40}
{'-=' * 20}''')


enterelinha('Dimensão de um terreno')
c1 = float(input('Comprimento do terreno (em metros): '))
l1 = float(input('Largura do terreno (em metros): '))
area(c1, l1)
