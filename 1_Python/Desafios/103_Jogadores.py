def ficha(nome='<desconhecido>', golos='0'):
    print('=' * 35, end='')
    print(f'\nJogador {" " * 20} Golos', end='')
    espaco = 32 - len(nome) - len(str(golos))
    print(f'\n{nome}{" " * espaco}{golos}')


n = str(input('Nome do jogador: ')).strip()
g = str(input('Número de Golos no campeonato: ')).strip()
if len(n) > 0:
    if len(g) > 0:
        ficha(n, g)
    else:
        ficha(n)
elif len(n) <= 0:
    if len(g) > 0:
        ficha(golos=g)
    else:
        ficha()
