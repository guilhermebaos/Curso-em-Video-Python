from termcolor import cprint, colored
from random import randint
from time import sleep
a = '-='
cprint('''Jogo da adivinhação
{}
Tenta adivinhar o número que o computador pensou (de 1 a 10)
{}'''.format(a * 20, a * 20), 'cyan')
pc = randint(1, 10)
j = 11
c1 = 0
while j != pc:
    j = int(input(colored('Tenta a tua sorte! ', 'blue')))
    if j != pc:
        cprint('Enganaste-te, tenta outra vez!', 'yellow')
    c1 += 1
cprint('Parabéns! Ganhaste! Apenas precisaste de {} tentativas!'.format(c1), 'green')
