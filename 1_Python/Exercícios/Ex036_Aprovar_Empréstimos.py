from termcolor import cprint, colored
c = float(input(colored('Qual é o preço da casa que quer comprar? ', 'blue')))
s = float(input(colored('Qual é o seu salário? ', 'blue')))
a = float(input(colored('Em quantos anos pretende pagar? ', 'blue')))
m = a * 12
p = c / m
cprint('Segundo essas condições, terá de pagar uma prestação mensal de {:.2f}€ durante {} meses'.format(p, m), 'cyan')
if p > s * 0.3:
    cprint('Empréstimo negado', 'red')
else:
    cprint('Empréstimo aprovado!', 'green')
