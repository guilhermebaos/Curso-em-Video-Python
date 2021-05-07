from termcolor import cprint, colored
from time import sleep
from random import randint
cprint('Pensei num número entre 1 e 10. Tenta adininhá-lo!', 'green')
pc = randint(0, 10)
j = -1
c1 = 0
while j != pc:
    m = 0
    while m != 1:
        j = input(colored('\nQual é o teu palpite? ', 'blue'))
        if j.isnumeric() == False:
            cprint('Escreva um número de 1 a 10!', 'red', attrs=['underline'])
            m = 0
        else:
            j = int(j)
            if j < 0 or j > 10:
                cprint('Escreva um número de 1 a 10!', 'red', attrs=['underline'])
            else:
                m = 1
    if pc > j:
        cprint('Pensei num número maior que esse...', 'cyan')
    if pc < j:
        cprint('Pensei num número menor que esse...', 'cyan')
    c1 += 1
cprint('\nParabéns, ganhaste! Só precisaste de tentar {} vezes'.format(c1), 'green')
