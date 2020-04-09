from termcolor import cprint, colored
f = str(input(colored('Escreve uma frase: ', 'blue'))).strip().lower()
f = f.replace(' ', '')
fi = ''
for a in range((len(f) - 1), -1, -1):
    fi += f[a]
if fi == f:
    cprint('A frase é palindrómica!', 'green')
else:
    cprint('A frase não é palíndrómica!', 'red')
