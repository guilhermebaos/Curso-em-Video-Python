from termcolor import cprint, colored
cprint('Programa multifunções!', 'cyan')
cprint('-=' * 20, 'cyan')
r = 6
c = 0
while r != 5:
    c += 1
    n1 = float(input(colored('\nEscreva um número: ', 'blue')))
    n2 = float(input(colored('Escreva outro número: ', 'blue')))
    if c == 1:
        cprint('''Funções:
        [1] para somar
        [2] para multiplicar
        [3] para ver qual é o maior
        [4] para escrever outros dois números
        [5] para sair do programa''', 'cyan')
    r = int(input(colored('Que função quer executar? ', 'yellow')))
    if r == 1:
        cprint('{} + {} = {}'.format(n1, n2, n1 + n2), 'green')
    elif r == 2:
        cprint('{} x {} = {}'.format(n1, n2, n1 * n2), 'green')
    elif r == 3:
        if n1 > n2:
            cprint('{} é maior que {}'.format(n1, n2), 'green')
        elif n2 > n1:
            cprint('{} é maior que {}'.format(n2, n1), 'green')
        else:
            cprint('Os números são iguais!', 'green')
    if r > 5:
        cprint('Função inexistente!', 'red', attrs=['underline'])
