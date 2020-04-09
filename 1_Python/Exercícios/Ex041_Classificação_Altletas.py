from termcolor import cprint, colored
from datetime import date
from time import sleep
cprint('PROGRAMA DE CLASSIFICAÇÃO DE ATLETAS', 'yellow')
cprint('-=-' * 20, 'cyan')
n = int(input(colored('Ano de nascimento: ', 'blue')))
a = date.today().year
i = a - n
if i <= 9:
    c = 'Mirim'
elif i <= 14:
    c = 'Infantil'
elif i <= 19:
    c = 'Júnior'
elif i <= 25:
    c = 'Sénior'
else:
    c = 'Master'
cprint('CLASSIFICAÇÃO: {}'.format(c), 'green')
