f = input('Escreve o teu nome completo: ')

f = f.strip()
f1 = f.count(' ')
f2 = f.split()
print('''
O teu primeiro nome é: {}
O teu último nome é: {}'''.format(f2[0], f2[f1]))
