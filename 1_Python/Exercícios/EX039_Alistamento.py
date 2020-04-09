from termcolor import colored, cprint
from time import sleep
from datetime import date
cprint('É hora de te alistares?', 'yellow')
n = int(input(colored('Em que ano nasceste? ', 'blue')))
a = date.today().year
i = a - n
sleep(1.5)
cprint('Quem nasceu em {} tem {} anos em {}'.format(n, a - n, a), 'magenta')
if i < 18:
    cprint('Ainda faltam {} ano(s) para o teu alistamento'.format(18 - i), 'green')
    cprint('O seu alistamento será em {}'.format(a + (18 - i)), 'green')
elif i > 18:
    cprint('Deve-se ter alistado há {} ano(s)'.format(i - 18), 'green')
    cprint('O seu alistamento deve ter sido em {}'.format(a - (i - 18)), 'green')
else:
    cprint('Irá ter de se alistar este ano!', 'green')
