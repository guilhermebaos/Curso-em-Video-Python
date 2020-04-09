from termcolor import colored, cprint
n = str(input(colored('Como te chamas? ', 'blue'))).strip()
if n == 'Guilherme':
    cprint('Que nome lindo!', 'yellow')
elif n == 'Maria' or n == 'Miguel' or n == 'Catarina':
    cprint('O teu nome até é bonito!', 'yellow')
elif n == 'David' or n == 'Luís' or n == 'Tomás':
    cprint('Vieste aqui a casa?', 'yellow')
cprint('Bom dia, {}!'.format(n), 'green')
