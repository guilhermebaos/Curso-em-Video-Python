import math
an = float(input('Digita um ângulo: '))
a = math.radians(an)
sa = math.sin(a)
ca = math.cos(a)
ta = math.tan(a)
print('O valor do seno de um ãngulo com {}º é: {:.2f}'.format(an, sa))
print('O valor do seu cosseno é: {:.2f}'.format(ca))
print('O valor da sua tangente é: {:.2f}'.format(ta))

# A função math.radians só vi na solução