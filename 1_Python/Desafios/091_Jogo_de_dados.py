from random import randint
from time import sleep
pontos = {}
print(f'''{'-=' * 10}
{'Jogo de dados!':^20}
{'-=' * 10}''')
for c1 in range(1, 5):
    p = str(input(f'Jogador {c1}, pressione Enter para lançar o dado!'))
    pl = 'Jogador ' + str(c1)
    pc = randint(1, 6)
    print('O dado foi lançado...')
    sleep(1)
    print(f'Saiu {pc}!\n')
    pontos[pl] = pc
pontos = sorted(pontos, key=pontos.get, reverse=True)
sleep(1)
print('Aqui estão os resultados!')
for c2 in range(0, 4):
    print(f'O {pontos[c2]} ficou na {c2 + 1}ª posição!')
    sleep(0.5)
