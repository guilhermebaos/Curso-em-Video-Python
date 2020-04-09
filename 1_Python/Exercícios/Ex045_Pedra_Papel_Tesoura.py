from termcolor import cprint, colored
from time import sleep
from random import randint
e = colored('-=' * 20, 'cyan')
cprint('PEDRA PAPEL TESOURA!!', 'magenta')
print(e)
cprint('Prima [ 0 ] para Pedra \n'
       'Prima [ 1 ] para Papel \n'
       'Prima [ 2 ] para Tesoura', 'cyan')
j = int(input(colored('A tua jogada será: ', 'grey')))
pc = randint(0, 2)
r = j - pc
if r == 0:
    rf = colored('Empate', 'yellow')
elif r == -1 or r == 2:
    rf = colored('O PC ganhou!', 'red')
elif r == 1 or r == -2:
    rf = colored('O jogador ganhou!', 'green')
else:
    rf = 'ERRO'
    print('Jogada inválida, reeinicie o programa')
    sleep(1000)
sleep(0.8)
cprint('Pedra...', 'red')
sleep(0.8)
cprint('Papel...', 'yellow')
sleep(0.8)
cprint('Tesoura!!', 'green')
sleep(0.8)
if j == 0:
    je = 'Pedra'
elif j == 1:
    je = 'Papel'
elif j == 2:
    je = 'Tesoura'
else:
    je = 'ERRO'
if pc == 0:
    pe = 'Pedra'
elif pc == 1:
    pe = 'Papel'
elif pc == 2:
    pe = 'Tesoura'
else:
    pe = 'ERRO'
print(e)
cprint('O Computador jogou {}! \n'
       'O Jogador jogou {}!'.format(je, pe), 'blue')
print(e)
print(rf)
