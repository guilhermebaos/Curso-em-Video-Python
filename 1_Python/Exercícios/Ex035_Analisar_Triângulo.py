from termcolor import colored, cprint
cprint('-=-' * 20, 'cyan')
cprint('Será que três segmentos de reta podem formar um triângulo?', 'magenta')
cprint('-=-' * 20, 'cyan')
s1 = float(input(colored('Comprimento do primeiro segmento: ', 'blue')))
s2 = float(input(colored('Comprimento do segundo segmento: ', 'blue')))
s3 = float(input(colored('Comprimento do terceiro segmento: ', 'blue')))
if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
    t = 'podem'
    c = 'green'
else:
    t = 'não podem'
    c = 'red'
cprint('Os segmentos de reta {} formar um triângulo'.format(t), c)
