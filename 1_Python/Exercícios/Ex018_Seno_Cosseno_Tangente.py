import math
an = float(input('Escreve um ângulo: '))
a = math.radians(an)
s = math.sin(a)
c = math.cos(a)
t = math.tan(a)
print('O seno do ângulo {}º é {:.2f}'.format(an, s))
print('O seu cosseno é {:.2f}'.format(c))
print('A sua tangente é {:.2f}'.format(t))
