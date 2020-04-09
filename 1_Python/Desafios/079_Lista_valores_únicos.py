n = 'b'
numeros = []
print('Os números que escrever serão registados, a menos que já tenham sido escritos')
print('Escreva "a" quando já não quiser adicionar mais números\n')
while n != 'a':
    n = str(input('Escreva um número inteiro: '))
    if n.isnumeric():
        if int(n) in numeros:
            print('Valor duplicado! Não será adicionado à lista!\n')
        if int(n) not in numeros and n != 'a':
            numeros.append(int(n))
    else:
        print('Escreve apenas números inteiros!\n')
numeros = sorted(numeros)
print(f'Os números escritos, por ordem crescente ficam: {", ".join(str(x) for x in numeros)}')
