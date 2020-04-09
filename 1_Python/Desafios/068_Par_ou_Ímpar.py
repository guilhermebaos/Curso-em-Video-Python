from termcolor import cprint, colored
from random import randint
d1 = '-=' * 15
d2 = '-' * 30
cprint(d1)
cprint('Jogo: Par ou ímpar!', 'cyan')
cprint(d1)
j = ''
while True:
    n = int(input(colored('Diz um número: ', 'blue')))
    while j != 'P' and j != 'I':
        j = str(input(colored('Par ou Ímpar (P/I): ', 'blue'))).capitalize()
        if j != 'P' and j != 'I':
            cprint('Escreva apenas "P" oi "I"', 'red', attrs=['underline'])
    if j == 'P':
        j = 0
        j1 = 'par'
    elif j == 'I':
        j = 1
        j1 = 'ímpar'
    pc = randint(n - 5, n + 5)
    r = n + pc
    cprint(d2)
    cprint(f'Tu jogaste {n} e o computador jogou {pc}. A soma é {n + pc}', 'cyan')
    cprint(f'Tu disseste que a soma seria {j1}', 'cyan')
    cprint(d2)
    if (r % 2) == j:
        cprint('Parabéns! Ganhaste!', 'green')
        cprint('Vamos jogar de novo!', 'green')
    else:
        cprint('GAME OVER!', 'red')
        break
