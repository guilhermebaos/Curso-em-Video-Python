from Modules import my_math

n = int(input('Escreve um número: ').strip())
fat = my_math.factorial(n)
print(f'O fatorial de {n} é {fat}')
print(f'O dobro de {n} é {my_math.double(n)}')
print(f'O dobro de {n} é {my_math.triple(n)}')
