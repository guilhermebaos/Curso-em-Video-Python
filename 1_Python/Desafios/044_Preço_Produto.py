from termcolor import colored, cprint
p = float(input(colored('Custo do produto (€): ', 'blue')))
cprint('Para pagar com dinheiro/ cheque, escreva 0', 'cyan')
cprint('Para pagar à vista com o cartão, escreva 1', 'cyan')
cprint('Para pagar até duas vezes com o cartão, escreva 2', 'cyan')
cprint('Para pagar três ou mais vezes com o cartão, escreva 3', 'cyan')
f = int(input(colored('Como deseja pagar? ', 'yellow')))
if f == 0:
    c = 0.9 * p
elif f == 1:
    c = 0.95 * p
elif f == 2:
    c = p
else:
    c = 1.2 * p
cprint('O preço final do produto é {}€'.format(c), 'green')
