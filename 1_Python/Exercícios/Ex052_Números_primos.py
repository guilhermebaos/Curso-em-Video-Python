from termcolor import cprint, colored
n = int(input(colored('Escreva um número: ', 'blue')))
nnp = 0
for c1 in range(1, n + 1):
    np = n % c1
    if np == 0:
        nnp += 1
        np = colored(c1, 'green')
        print(np, end=' ')
    else:
        np = colored(c1, 'red')
        print(np, end=' ')
if nnp == 2:
    p = 'é'
    q = ' apenas'
else:
    p = 'não é'
    q = ''
cprint('\nO número {} {} primo, porque é divisível{} por {} números'.format(n, p, q, nnp), 'green')
