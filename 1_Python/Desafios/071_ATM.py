from termcolor import cprint, colored
cprint('''--------------------
     ATM Local
--------------------''', 'cyan')
while True:
    n = input(colored('Quanto dinheiro queres levantar? ', 'blue'))
    if n.isnumeric():
        n = int(n)
        break
    else:
        cprint('Escreva apenas o número, por favor', 'red')
n50 = n // 50
sn = n - n50 * 50
n20 = sn // 20
sn = sn - n20 *20
n10 = sn // 10
sn = sn - n10 * 10
n1 = sn
cprint('Receberá: ', 'green')
if n50 != 0:
    cprint(f'{n50} notas de 50€', 'green')
if n20 != 0:
    cprint(f'{n20} notas de 20€', 'green')
if n10 != 0:
    cprint(f'{n10} notas de 10€', 'green')
if n1 != 0:
    cprint(f'{n1} moedas de 1€', 'green')
