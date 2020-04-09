from termcolor import colored, cprint
n = 0
cn = 0
while n != 999:
    cn += n
    n = int(input(colored('Escreve um número para o adicionar à soma (escreve 999 para parar e ver o resultado): ', 'blue')))
    if n != 999:
        cprint('{} + '.format(n), 'green', end='\n')
cprint('= {}'.format(cn), 'green')
