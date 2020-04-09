from math import hypot
co = float(input('Medida do cateto oposto: '))
ca = float(input('Medida do cateto adjacente: '))
h = hypot(co, ca)
print('A hipotenusa de um triângulo retângulo de catetos {} e {} é {:.2f}'.format(co, ca, h))

'''cato = float(input('Medida do cateto oposto: '))
cata = float(input('Medida do cateto adjacente: '))
h2 = (ca**2 + ca**2)**1/2
print('A hipotenusa de um triângulo retânfulo de catetos {} e {} é {:.2f}'.format(co, ca, h))'''
