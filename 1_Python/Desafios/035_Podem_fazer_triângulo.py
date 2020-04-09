r1 = float(input('Escrve o comprimento de uma reta: '))
r2 = float(input('Agora escreve o comprimento de outra: '))
r3 = float(input('Agora escreve o comprimento de uma terceira: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas podem formar um triângulo!')
else:
    print('Essas retas não podem formar um triângulo.')
