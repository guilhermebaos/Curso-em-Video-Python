from termcolor import cprint, colored
cprint('CONVERSOR DE NÚMEROS', 'yellow')
n = int(input(colored('Escreve um número: ', 'blue')))
cprint('''Escolha uma das opções abaixo:
Prima [ 1 ] para converter para binário
Prima [ 2 ] para converter para octal
Prima [ 3 ] para converter para hexadecimal''', 'cyan')
c = int(input(colored('Opção: ', 'blue')))
if c == 1:
    c = colored(str(bin(n)[2:]), 'green')
    b = 'binário'
elif c == 2:
    c = colored(str(oct(n)[2:]), 'green')
    b = 'octal'
elif c == 3:
    c = colored(str(hex(n)[2:]), 'green')
    b = 'hexadecimal'
else:
    c = colored('OPCÂO INVÀLIDA, tente de novo', 'red', attrs=['underline'])
    b = colored('ERRO', 'red', attrs=['underline'])
cprint('O número {} convertido para {} é {}'.format(n, b, c), 'green')
