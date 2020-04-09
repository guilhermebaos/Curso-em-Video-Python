from termcolor import cprint, colored
from datetime import date
a = date.today().year
a1 = str(a)
m1 = 0
m2 = 0
m3 = 0
y = 7
for b in range(0, y):
    n = int(input(colored('Em que ano nasceste? ', 'blue')))
    m = a - n
    if m >= 18:
        m1 += 1
    elif 0 <= m <= 18:
        m2 += 1
    else:
        cprint('ERRO, ano inválido!', 'red', attrs=['underline'])
cprint('Das pessoas que colocaram o seu ano de nascimento no programa, {} são maiores de idade ou sê-lo-ão no final do ano'.format(m1), 'cyan')
