from termcolor import colored, cprint
n1 = str(input(colored('Escreve um número: ', 'blue'))).strip().lower()
n2 = str(input(colored('Escreve outro número: ', 'blue'))).strip().lower()
if n1.isnumeric() == True or n1.find('.') > 0 and n2.isnumeric() == True or n2.find('.') > 0:
    if n1 > n2:
        cprint('O primeiro número é maior que o segundo', 'green')
    elif n1 == n2:
        cprint('Os dois números são iguais', 'green')
    elif n1 < n2:
        cprint('O segundo número é maior que o primeiro', 'green')
else:
    cprint('Uma das entradas não é um número!', 'red', attrs=['underline'])
