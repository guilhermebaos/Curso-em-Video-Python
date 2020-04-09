import random
n1 = random.uniform(1, 5)
n2 = int(n1)
print('Vou pensar num número entre 0 e 5')
print('''...
...
...''')
a = int(input('Agora tenta adivinhar: '))
if a == n2:
    print('Adivinhaste, parabéns, tinha pensado no {}!'.format(n2))
else:
    print('Não adivinhaste, tenta outra vez! Tinha pensado no número {}'.format(n2))
