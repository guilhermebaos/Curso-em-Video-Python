from termcolor import cprint, colored
cprint('''Somador de números pares!
Dos números que escreveres apenas serão considerados para a soma os pares''', 'blue')
s = 0
for a in range(0, 6):
    b = int(input(colored('Escreve um número: ', 'cyan')))
    if (b % 2) != 0:
        b = 0
    s += b
cprint('A soma dos números pares que escreveste é: {}'.format(s), 'yellow')
