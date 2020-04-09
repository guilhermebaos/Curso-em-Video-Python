from termcolor import cprint, colored
n1 = float(input(colored('Escreve um número: ', 'blue')))
n2 = float(input(colored('Escreve outro número: ', 'blue')))
if n1 > n2:
    cprint('o 1º número é maior que o segundo!', 'green')
elif n2 > n1:
    cprint('O 2º número é maior que o 1º!', 'green')
else:
    cprint('Os números são iguais!', 'green')
