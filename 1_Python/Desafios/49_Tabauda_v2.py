from termcolor import cprint, colored
n = int(input(colored('Escreva um número para ver a sua tabauada: ', 'blue')))
cprint('A tabuada de {} é:'.format(n), 'yellow')
for a in range(1, 11):
    cprint('{} x {:<2} = {:<3}'.format(n, a, n*a), 'cyan')
