from termcolor import colored, cprint
n1 = float(input(colored('Escreve ma das tuas notas: ', 'blue')))
n2 = float(input(colored('Escreve outra nota: ', 'blue')))
m = (n1 + n2) / 2
cprint('A tua média é: {:.2f}'.format(m), 'magenta')
if m > 7:
    cprint('Passaste de ano!', 'green')
elif m < 5:
    cprint('Reprovaste o ano!', 'red')
else:
    cprint('Tens de recuperar!', 'yellow')
