from termcolor import cprint, colored
from time import sleep
cprint('Números pares de 1 a 50: ', 'blue')
for a in range(2, 50, 2):
    cprint(a, 'cyan', end=' ')
