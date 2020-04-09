from datetime import date
from termcolor import colored, cprint
a = int(input(colored('Escreva um ano e descuba de ele é bissexto! (Escreva 0 para analisar o ano atual): ', 'blue')))
'''if a % 400 == 0:
    cprint('O ano {} é bissexto!'.format(a), 'green')
else:
    if a % 100 == 0:
        cprint('O ano não é bissexto.'.format(a), 'green')
    else:
        if a % 4 == 0:
            cprint('O ano {} é bissexto!'.format(a), 'green')
        else:
            cprint('O ano {} não é bissexto.'.format(a), 'green')'''
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    cprint('O ano {} é bissexto!'.format(a), 'green')
else:
    cprint('O ano {} não é bissexto'.format(a), 'red')
