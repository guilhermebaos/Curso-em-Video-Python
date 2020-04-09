from termcolor import cprint, colored
n = int(input(colored('Escreve um número para ver o seu fatorial: ', 'blue')))
c = 0
f = 1
while c < n:
    c += 1
    f *= c
cprint('{}! = {}'.format(n, f), 'green')

# OU:
# from math import factorial
# factorial(n)
