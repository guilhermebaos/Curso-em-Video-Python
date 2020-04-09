f = str(input('Escreve uma expressão: '))
x1 = x2 = len(f)
y1 = y2 = 0
ff1 = f.find('(', y1, x1)
while ff1 != -1:
    ff2 = f.find(')', y2, x2)
    y2 = ff2 + 1
    if ff2 <= ff1:
        r = 'A expresssão está errada'
        break
    else:
        r = 'A expressão está correta'
    y1 = ff1 + 1
    ff1 = f.find('(', y1, x1)
print(r)
