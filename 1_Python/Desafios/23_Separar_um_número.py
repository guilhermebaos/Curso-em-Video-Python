n = input('Digita um número entre 0 e 9999: ')

print('''O número é : {}

Tem {} milhare(s)
    {} centena(s)
    {} dezena(s)
    {} unidade(s)'''.format(n, n[0], n[1], n[2], n[3]))

n = (int(input('Escreve um número entre 0 e 9999: ')))

n1 = n // 1000
n2 = n//100 - n1 * 10
n3 = n//10 - n1 * 100 - n2 * 10
n4 = n - n1 * 1000 - n2 * 100- n3 * 10

print('''O número é {}

Tem {} milhare(s)
    {} centena(s)
    {} dezena(s)
    {} unidade()'''.format(n, n1, n2, n3, n4))
