from termcolor import cprint, colored
cprint('Escreva vários números para os somar, escreva "parar" para parar', 'cyan')
c = s = 0
while True:
    n = input(colored('Escreve um número: ', 'blue'))
    if n.isnumeric():
        n = float(n)
        s += n
    if n == 'parar':
        break
    c += 1
cprint(f'A soma dos {c} que escreveste é: {s}', 'green')
