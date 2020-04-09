from termcolor import colored, cprint
a = float(input(colored('Escreve um número: ', 'blue')))
b = float(input(colored('Escreve outro número: ', 'blue')))
c = float(input(colored('E agora mais um: ', 'blue')))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > c and b > a:
    maior = b
if c > a and c > b:
    maior = c
cprint('''O maior número é o {}
O menor número é o {}'''.format(maior, menor), 'green')
