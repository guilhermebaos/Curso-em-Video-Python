from termcolor import cprint, colored
it = 0
im = 0
mn = 0
ms = ''
nm = colored('ERRO', 'red', attrs=['underline'])
for c1 in range(0, 4):
    cprint('----- {}ª Pessoa -----'.format(c1 + 1), 'blue')
    n = str(input(colored('Nome: ', 'cyan')))
    i = int(input(colored('Idade: ', 'cyan')))
    s = str(input(colored('Sexo [M/F]: ', 'cyan')))
    it += i
    if i > im and s == 'M':
        im = i
        nm = n
    if i < 20 and s == 'F':
        mn += 1
        if mn > 1:
            ms = 'es'
cprint('A média de idade do grupo é: {}'.format(it / 4), 'green')
cprint('O homem mais velho chama-se {} e tem {} anos de idade.'.format(nm, im), 'green')
cprint('Há {} mulher{} com menos de 20 anos de idade.'.format(mn, ms), 'green')
