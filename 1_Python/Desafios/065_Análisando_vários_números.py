from termcolor import cprint, colored
r = ''
mn = 0
c = 0
n = float(input(colored('Escreva um número: ', 'blue')))
maior = menor = n
while r != 'N':
    mn += n
    c += 1
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    r = ''
    while r != 'S' and r != 'N':
        r = str(input(colored('Quer escrever mais números [S/N]: ', 'blue'))).upper()
        if r != 'S' and r != 'N':
            cprint('Escreva apenas "S" ou "N"!', 'red')
        if r == 'S':
            n = float(input(colored('\nEscreva um número: ', 'blue')))
cprint('A média dos números que escreveu é: {}'.format(mn / c), 'green')
cprint('O maior número é {} e o menor é {}'.format(maior, menor), 'green')
