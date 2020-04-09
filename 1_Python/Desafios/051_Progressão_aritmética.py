from termcolor import colored, cprint
t1 = float(input(colored('Escreve o termo 1 da sequência: ', 'blue')))
g = float(input(colored('Lógica da progressão aritmética: ', 'blue')))
cprint('A ordem da sequência é: {}'.format(t1), 'cyan',  end=' ')
for a in range(0, 9):
    t1 += g
    cprint(t1, 'cyan', end=' ')
