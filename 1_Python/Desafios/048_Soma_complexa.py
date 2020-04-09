from termcolor import colored, cprint
cprint('Soma de todos os números ímpares e múltiplos de 3 entre 1 e 500 é...: ', 'blue', end=' ')
s = 0
for a in range(1, 500, 2):
    if (a % 3) == 0:
        b = a
    else:
        b = 0
    s += b
cprint(s, 'cyan')
