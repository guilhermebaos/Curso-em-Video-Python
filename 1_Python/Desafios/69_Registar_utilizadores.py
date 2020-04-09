from termcolor import cprint, colored
a = colored('''--------------------
Insira os dados de um utilizador:
--------------------''', 'cyan')
print(a)
mi = 0
h = 0
mm = 0
while True:
    i = ''
    while True:
        i = input(colored('Idade: ', 'blue'))
        if not i.isnumeric():
            cprint('Escreva apenas o número de anos!\n', 'red')
        else:
            break
    i = int(i)
    g = ''
    while True:
        g = input(colored('Género [M/F]: ', 'blue')).capitalize()
        if g != 'M' and g != 'F':
            cprint('Escreva apenas "M" ou "F"!\n', 'red')
        else:
            break
    c = ''
    while True:
        c = input(colored('Quer continuar? [S/N]: ', 'blue')).capitalize()
        if c != 'S' and c != 'N':
            cprint('Escreva apenas "S" ou "N"!\n', 'red')
        elif c == 'S':
            print('\n' + a)
            break
        else:
            break
    if i < 18:
        mi += 1
    if g == 'M':
        h += 1
    if g == 'F' and i < 20:
        mm += 1
    if c == 'N':
        break
cprint(f'''\nInformações:
Total de pessoas com menos de 18 anos registadas: {mi} 
Homens registados: {h}
Mulheres com menos de 20 anos registada: {mm}''', 'green')

