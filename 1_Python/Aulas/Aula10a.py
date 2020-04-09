n1 = float(input('Escreve a tua primeira nota:'))
n2 = float(input('Escreve outra nota: '))
m = (n1 + n2) / 2
print('A tua média foi {:.2f}'.format(m))
if m >= 15.0:
    print('A tua média foi boa!')
else:
    print('A tua média foi má. ESTUDA MAIS!')

# print('Parabéns pelas notas' if m >11.0 else 'ESTUDA MAIS1')
