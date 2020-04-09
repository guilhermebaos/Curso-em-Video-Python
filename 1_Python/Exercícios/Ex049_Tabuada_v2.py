n = int(input('Digite um número para ver a sua tabuada: '))
for c1 in range(0,11):
    print('{} x {:>2} = {}'.format(n, c1, n * c1))
