from termcolor import cprint, colored
n = int(input(colored('Escreve um número inteiro: ', 'blue')))
if n == 1:
    cprint('O número 1 não é primo nem é não-primo, pois apenas tem um divisor, 1', 'green')
for a in range(2, (n+1)):
    if (n % a) == 0:
        if a == n:
            cprint('O número {} é primo!'.format(n), 'green')
        else:
            cprint('O número {} não é primo!'.format(n), 'red')
            n = -1
