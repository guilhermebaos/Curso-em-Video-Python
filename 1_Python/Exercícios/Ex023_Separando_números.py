n = int(input('Escreve um número de 0 a 9999: '))
n1 = n // 1000 % 10
n2 = n // 100 % 10
n3 = n // 10 % 10
n4 = n //1 % 10
print('''Analise do número {}:
Tem {} milhares
    {} centenas
    {} dezenas
    {} unidades'''.format(n, n1, n2, n3, n4))

# OU

n = int(input('Escreve um número: '))
n5 = n / 1000
num = str(n5)
print('''Analise do número {}:
Tem {} milhares
    {} centenas
    {} dezenas
    {} unidades'''.format(n, num[0], num[2], num[3], num[4]))
