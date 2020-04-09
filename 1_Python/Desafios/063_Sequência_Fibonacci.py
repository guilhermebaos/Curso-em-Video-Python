from termcolor import cprint, colored
n = int(input(colored('Quantos termos queres ver da sequência de Fibonacci queres ver? ', 'blue')))
c = 0
f1 = 0
f2 = 1
t = 0
cprint('Os primeiros {} termos da sequência de Fibonacci são: '.format(n), 'cyan')
while c < n:
    c += 1
    cprint(t, 'green', end=' ')
    t = f1 + f2
    if c % 2 == 0:
        f1 = t
    else:
        f2 = t
