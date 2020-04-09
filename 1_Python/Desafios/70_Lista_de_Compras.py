from termcolor import cprint, colored
d = colored('-' * 20, 'cyan')
ct = pm = c1 = p100 = 0
cprint(d)
cprint('Lista de compras!', 'cyan')
while True:
    c1 += 1
    cprint(d)
    n = str(input(colored('Nome do produto: ', 'blue'))).strip()
    while True:
        p = input(colored('Preço: ', 'blue'))
        if p.replace('.', '').isnumeric():
            p = float(p)
            break
        else:
            cprint('Escreva o preço outra vez! (Use "." em vez de ",")', 'red')
    while True:
        cprint(f'Produto: {n}, {p}€', 'green')
        c = str(input(colored('Quer adicionar um produto à lista? [S/N]: ', 'blue')))
        if c == 'S' or c == 'N':
            break
        else:
            cprint('Escrva apenas "S" ou "N"!', 'red')
    ct += p
    if p < pm or c1 == 1:
        pm = n
    if p > 100:
        p100 += 1
    if c == 'N':
        break
cprint(f'''Custo total da compra: {ct}
Produto mais barato: {pm}
Nº de produtos que cutam mais de 100€: {p100}''', 'green')
