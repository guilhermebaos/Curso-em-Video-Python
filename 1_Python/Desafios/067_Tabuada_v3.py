d = '-' * 20
while True:
    n = int(input('Escreva um número para ver a sua tabuada, escreva um número negativo para terminar o programa: '))
    print(d)
    if n < 0:
        break
    for c1 in range(1, 11):
        print(f'{n} x {c1} = {n * c1}')
    print(d)
print('Programa terminado')
