from random import randint
n1 = str(randint(1, 9))
n2 = str(randint(1, 9))
n3 = str(randint(1, 9))
n4 = str(randint(1, 9))
n5 = str(randint(1, 9))
n = (n1, n2, n3, n4, n5)
print(f'''A lista é: {' '.join(n)}
O maior número da lista é: {max(n)}
O menor número da lista é: {min(n)}''')

