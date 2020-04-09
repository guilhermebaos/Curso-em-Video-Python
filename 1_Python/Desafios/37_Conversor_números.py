from termcolor import colored, cprint
n = int(input(colored('Escreve um número inteiro qualquer: ', 'blue')))
bn = str(bin(n))[2:]
on = str(oct(n))[2:]
hn = str(hex(n))[2:]
cprint('Escreve 1 para ver o número em binário, 2 para o veres em octal e 3 para o veres em hexadecimal', 'yellow')
e = str(input())
if e == '1':
    v = bn
    f = 'binário'
elif e == '2':
    v = on
    f = 'octal'
elif e == '3':
    v = hn
    f = 'hexadecimal'
else:
    cprint('ERRO, não foi escrito 1, 2 ou 3', 'red', attrs=['underline'])
cprint('O número {} escrito em {} passa a {}!'.format(n, f, v), 'green')
