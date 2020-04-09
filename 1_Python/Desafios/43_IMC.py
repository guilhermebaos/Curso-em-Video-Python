from termcolor import colored, cprint
p = float(input(colored('Quanto pesas (em kg)? ', 'blue')))
a = float(input(colored('Qual é a tua altura (em m)? ', 'blue')))
IMC = p / a**2
if IMC < 18.5:
    s = colored('Abaixo do peso Ideal', 'red')
elif IMC < 25:
    s = colored('Peso Ideal', 'green')
elif IMC < 30:
    s = colored('Acima do Peso Ideal', 'magenta')
elif IMC < 40:
    s = colored('Obeso', 'red')
else:
    s = colored('Obeso mórbido', 'red', attrs=['underline'])
cprint('O seu Índice de massa corporal é {:.2f} \nStatus: {}'.format(IMC, s), 'yellow')
cprint('O seu Peso Ideal é entre {}kg e {}kg'.format(18.5 * a**2, 25 * a**2), 'green')
