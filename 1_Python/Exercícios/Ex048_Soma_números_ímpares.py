s = 0
c2 = 0
for c1 in range(0, 501, 3):
    if c1 % 2 == 0:
        s += 0
    elif c1 % 2 == 1:
        s += c1
        c2 += 1
print('A soma de todos os números ímpares múltiplos de 3 entre 1 e 500 ({} valores) é: {}'.format(c2, s))
