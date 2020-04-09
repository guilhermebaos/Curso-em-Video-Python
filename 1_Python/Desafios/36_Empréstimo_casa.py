from termcolor import colored, cprint
cprint('Sistema de aprovamento de empréstinmos automático', 'yellow')
c = float(input(colored('Qual é o valor da casa que quer comprar?(€) ', 'blue')))
s = float(input(colored('Qual é o seu salário?(€) ', 'blue')))
a = float(input(colored('Em quantos anos pretende pagar a casa? ', 'blue')))
m = a * 12
men = c / m
sd = s * 0.3
if sd > men:
    cprint('O seu empréstimo foi aprovado!', 'green')
    cprint('A sua prestação mensal será de {:.2f}€'.format(men), 'green')
else:
    cprint('O seu empréstimo foi negado.', 'red')
