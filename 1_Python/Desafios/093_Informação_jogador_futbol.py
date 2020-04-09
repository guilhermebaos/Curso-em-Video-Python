info = dict()
total = 0
info['nome'] = str(input('Nome do jogador: ')).strip()
while True:
    jogos = str(input('Número de jogos jogados: ')).strip()
    if jogos.isnumeric():
        jogos = int(jogos)
        break
    else:
        print('Escreve só o número!\n')
info['golos'] = []
for c1 in range(0, jogos):
    while True:
        g = str(input(f'Núemro de golos marcados pelo jogador no {c1 + 1}º jogo: ')).strip()
        if g.isnumeric():
            g = int(g)
            break
        else:
            print('Escreve só o número!\n')
    info['golos'].append(g)
    total += g
info['total'] = total
print(f'\nO jogador {info["nome"]} marcou no total {info["total"]} golos:')
for c2 in range(0, jogos):
    print(f'    >>> {info["golos"][c2]} golos no {c2 + 1}º jogo')
print(f'\nO que dá uma média de {total / jogos:3} golos por jogo!')
