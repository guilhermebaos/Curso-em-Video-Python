from termcolor import cprint, colored
r = 'y'
while r != 'M' and r != 'F':
    r = str(input(colored('Escreva o seu sexo (M/F): ', 'blue'))).upper()
    if r != 'M'and r != 'F':
        cprint('Por favor, escreva apenas "M" ou "F"', 'red', attrs=['underline'])
if r == 'M':
    s = 'masculino'
elif r == 'F':
    s = 'femenino'
cprint('Sexo registado: {}'.format(s), 'green')
