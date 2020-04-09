import math
c1 = float(input('Digita o comprimento de um dos catetos do triângulo: '))
c2 = float(input('Agora escreve o comprimento do outro cateto: '))
h = math.sqrt(math.pow(c1, 2) + math.pow(c2, 2))
print('O comprimento da hipotenusa desse triângulo é {:.3f}'.format(h))
