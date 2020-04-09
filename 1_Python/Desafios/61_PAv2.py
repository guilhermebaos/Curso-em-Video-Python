from termcolor import cprint, colored
c = 0
p = 10
ni = float(input(colored('Primeiro termo da progressão aritmética: ', 'blue')))
pa = float(input(colored('Razão da progressão aritmética: ', 'blue')))
np = ni
while c < p:
    c += 1
    cprint(np, 'green', end=' ')
    np += pa
