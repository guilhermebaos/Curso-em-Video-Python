from termcolor import cprint, colored
from random import randint
from time import sleep
cprint('Printo para jogar Pedra Papel Tesoura com o computador?', 'yellow')
a = colored('-=-' * 20, 'cyan')
print(a)
p1 = str(input(colored('Pedra, Papel... Tesoura! (escreve o que queres jogar) ', 'magenta',))).strip().lower()
print(a)
sleep(1.5)
pc = randint(1, 3)   # 1 = pedra   2 = papel   3 = tesoura
if pc == 1:
    jpc = 'pedra'
elif pc == 2:
    jpc = 'papel'
elif pc == 3:
    jpc = 'tesoura'
cprint('(Tu fizeste {} e o computador fez {})'.format(p1, jpc), 'grey', attrs=['concealed'])
d = colored('O computador ganhou!', 'green')
v = colored('Ganhaste ao computador, parabéns!', 'green')
e = colored('Empate', 'yellow')
if p1 == 'tesoura':
    if pc == 1:
        r = d
    elif pc == 2:
        r = v
    elif pc == 3:
        r = e
if p1 == 'pedra':
    if pc == 2:
        r = d
    elif pc == 3:
        r = v
    elif pc == 1:
        r = e
if p1 == 'papel':
    if pc == 3:
        r = d
    elif pc == 1:
        r = v
    elif pc == 2:
        r = e
if p1 != 'tesoura' and p1 != 'pedra' and p1 != 'papel':
    cprint('ERRO', 'red', attrs=['underline'])
else:
    print(r)
