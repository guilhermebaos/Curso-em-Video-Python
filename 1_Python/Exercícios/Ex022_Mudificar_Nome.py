n = str(input('Escreve o teu nome: ')).strip()
n1 = n.split()[0]
n2 = len(n1)  # n.find(' ') # Isto encontra o 1º espaço, pois o nome termina nessa posição
n3 = len(n.replace(' ', ''))  # len(n) - n.count(' ') # Isto retira os espaços
n4 = n.upper()
n5 = n.lower()
print('''Analisando o teu nome...
...
...
O teu primeiro nome é {} e tem {} letras
O teu nome completo tem {} letras
O teu nome em maiúsculas é: {}
O teu nome em minúsculas é: {}'''.format(n1, n2, n3, n4, n5))
