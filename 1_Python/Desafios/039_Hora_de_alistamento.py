from termcolor import cprint, colored
from datetime import date
a = date.today().year
n = int(input(colored('Em que ano nasceste? ', 'blue')))
i = a - n
if i < 18:
    cprint('Daqui a {} anos terás de te enlistar no exército'.format(18 - i), 'green')
elif i > 18:
    cprint('O tempo de alistamento passou há {} anos'.format(i - 18), 'green')
else:
    cprint('Tens de te enlistar este ano!', 'green')

