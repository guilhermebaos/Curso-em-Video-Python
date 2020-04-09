from termcolor import colored, cprint
n = int(input(colored('Escreve um número inteiro: ', 'blue')))
if n % 2 == 0:
    cprint('O número {} é par!'.format(n), 'green')
else:
    cprint('O número {} é ímpar!'.format(n), 'green')
