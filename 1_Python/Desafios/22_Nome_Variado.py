nome = input('Escreve o teu nome completo: ')

print(nome.upper())
print(nome.lower())

nome1 = nome.replace(' ', '')
print('O teu nome tem {} letras'.format(len(nome1)))

nome2 = nome.split()
print('O teu primeiro nome tem {} letras'.format(len(nome2[0])))
