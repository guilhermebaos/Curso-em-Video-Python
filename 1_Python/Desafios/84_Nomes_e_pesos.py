dados = []
pessoa = []
lpma = []
lpme = []
c1 = c2 = 0


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


while True:
    qc = 0
    n = str(input('\nNome do indíviduo: ')).strip()
    while True:
        p = str(input('Peso do indivíduo (kg): ')).strip()
        if isfloat(p):
            break
        else:
            print('Escreva só o número!\n')
    pessoa.append(n)
    pessoa.append(p)
    dados.append(pessoa[:])
    pessoa.clear()
    if c2 == 0:
        pma = pme = p
    else:
        if pma < p:
            pma = p
        if pme > p:
            pme = p
    while qc not in ['S', 'N']:
        qc = str(input('Queres continuar [S/N]? ')).strip().upper()
    c2 += 1
    if qc == 'N':
        break
for p in range(0, len(dados)):
    if dados[p][1] == pma:
        lpma += [dados[p][0]]
    if dados[p][1] == pme:
        lpme += [dados[p][0]]
print(f'''\nForam registadas {c2} pessoas
As pessoas mais leves são: {', '.join(lpme)}
As pessoas mais pesadas são: {', '.join(lpma)}''')
