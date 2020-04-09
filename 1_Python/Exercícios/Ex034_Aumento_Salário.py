from termcolor import colored, cprint
s = float(input(colored('Qual é o teu salário? ', 'blue')))
a = 0.10 if s > 1250 else 0.15
sa = s + s * a
cprint('O salário de {:.2f}€ com o aumento de {}% passa a {:.2f}€'.format(s, a * 100, sa), 'green')
