from datetime import date
from termcolor import colored, cprint
n = int(input(colored('Em que ano nasceste? ', 'blue')))
a = date.today().year
i = a - n
if i <= 9:
    c = 'Mirim'
elif i <= 14:
    c = 'Infantil'
elif i <= 19:
    c = 'Junior'
elif i <= 20:
    c = 'Sénior'
else:
    c = 'Master'
cprint('A tua categoria é : {}'.format(c), 'green')
