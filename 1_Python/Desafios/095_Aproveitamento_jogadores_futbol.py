total, golos, = [], []
info = {}
mai = 0
c3 = 1
while True:
    info['número'] = c3
    c3 += 1
    total_golos = 0
    info['nome'] = str(input('Nome do jogador: ')).strip()
    while True:
        info['jogos'] = str(input('Número de partidas jogadas: ')).strip()
        if info['jogos'].isnumeric:
            info['jogos'] = int(info['jogos'])
            break
        else:
            print('Escreve só o número!\n')
    if info['jogos'] > mai:
        mai = info['jogos']
    for c1 in range(0, info['jogos']):
        while True:
            g = str(input(f'    >>> Número de golos no {c1 + 1}º jogo: ')).strip()
            if g.isnumeric:
                g = int(g)
                break
            else:
                print('Escreve só o número!\n')
        total_golos += g
        golos.append(g)
    info['golos'] = golos.copy()
    info['total'] = total_golos
    total.append(info.copy())
    golos.clear()
    while True:
        r = str(input('\nQueres inserir informação sobre outro jogador [S/N]? ')).strip().upper()
        if r in ['S', 'N']:
            break
        else:
            print('Escreve só "S" ou "N"!')
    print('-=' * 20)
    if r == 'N':
        break
mai = int(mai * 3)
print(f'''{'Número':8} {'Nome':10} {'Golos'.ljust(mai)} {'Total de golos'}''')
for c2 in total:
    print(f'''{c3:<8} {c2['nome']:10} {str(', '.join(str(x) for x in c2['golos'])).ljust(mai)} {c2['total']}''')
while True:
    while True:
        r2 = str(input('\nQueres saber mais informações sobre um jogador [S/N]? ')).strip().upper()
        if r2 in ['S', 'N']:
            break
        else:
            print('Escreve só "S" ou "N"!')
    if r2 == 'N':
        break
    else:
        r3 = str(input('\nEscreve o nome desse jogador: ')).strip()
        c5 = 1
        for c4 in total:
            c5 += 1
            if c4['nome'] == r3:
                print(f'''O jogador {c4['nome']} marcou no total {c4['total']} golos:''')
                for r3 in range(0, len(c4['golos'])):
                    print(f'''    >>> Marcou {c4['golos'][r3]} no {r3 + 1}º jogo''')
                print(f'''A média de golos por jogo é: {c4['total'] / c4['jogos']}!''')
                break
            if c3 == c5:
                print('Jogador inexistente!')
