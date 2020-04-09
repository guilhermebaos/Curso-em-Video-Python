from termcolor import colored, cprint
n = float(input(colored('Qual é a distância da viagem, em km? ', 'blue')))
'''if n > 200:
    p = n * 0.045
else:
    p = n * 0.050'''
p = n * 0.045 if n > 200 else n * 0.050
cprint('A sua viagem de {}km custará {}€'.format(n, p), 'green')
