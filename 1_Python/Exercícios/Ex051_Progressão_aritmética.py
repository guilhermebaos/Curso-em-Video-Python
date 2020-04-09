from emoji import emojize
from termcolor import cprint, colored
from time import sleep
e = '=-' * 30
cprint('''{0}
Primeiros 10 termos de uma progressão aritmética
{0}'''.format(e), 'cyan')
pt = float(input(colored('Primerio termo da PA: ', 'blue')))
pa = float(input(colored('Razão da PA: ', 'blue')))
s = emojize(':arrow_forward:', use_aliases=True)
s = colored(s, 'yellow')
tp = pt
cprint('Os primeiros 10 termos da progressão são: ', 'green')
for c1 in range(0, 11):
    print(tp, s, end=' ')
    tp += pa
