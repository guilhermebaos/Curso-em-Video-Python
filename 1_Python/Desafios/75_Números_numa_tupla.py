from termcolor import cprint, colored
pares = []
while True:
    n1 = str(input(colored('Escreve um número inteiro: ', 'blue'))).strip()
    if n1.isnumeric():
        break
    else:
        cprint('Não escreveste um número inteiro!\n', 'red')
while True:
    n2 = str(input(colored('Escreve um número inteiro: ', 'blue'))).strip()
    if n2.isnumeric():
        break
    else:
        cprint('Não escreveste um número inteiro!\n', 'red')
while True:
    n3 = str(input(colored('Escreve um número inteiro: ', 'blue'))).strip()
    if n3.isnumeric():
        break
    else:
        cprint('Não escreveste um número inteiro!\n', 'red')
while True:
    n4 = str(input(colored('Escreve um número inteiro: ', 'blue'))).strip()
    if n4.isnumeric():
        break
    else:
        cprint('Não escreveste um número inteiro!\n', 'red')
tupla = (n1, n2, n3, n4)
if '3' in tupla:
    t3 = 'O valor "3" foi o {}º a ser digitado'.format(tupla.index('3') + 1)
else:
    t3 = 'O valor "3" não foi digitado'
if '9' in tupla:
    t9 = 'O valor "9" foi digitado {} vezes'.format(tupla.count('9'))
else:
    t9 = 'O valor 9 não foi digitado'
if int(tupla[0]) % 2 == 0:
    pares += [tupla[0]]
if int(tupla[1]) % 2 == 0:
    pares += [tupla[1]]
if int(tupla[2]) % 2 == 0:
    pares += [tupla[2]]
if int(tupla[3]) % 2 == 0:
    pares += [tupla[3]]
cprint(f'''\nO maior valor foi {max(tupla)} e o menor foi {min(tupla)}
{t3}
{t9}
Os números pares digitados foram: {', '.join(pares)}''', 'green')
