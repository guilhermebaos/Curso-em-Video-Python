n = []
for c1 in range(0, 5):
    p = float(input('Quanto pesas? '))
    n += [str(p)]
n0 = float(n[0])
n1 = float(n[1])
n2 = float(n[2])
n3 = float(n[3])
n4 = float(n[4])
if n0 > n1 and n0 > n2 and n0 > n3 and n0 > n4:
    p = 'primeira'
elif n1 > n2 and n1 > n3 and n1 > n4:
    p = 'segunda'
elif n2 > n3 and n2 > n4:
    p = 'terceira'
elif n3 > n4:
    p = 'quarta'
else:
    p = 'quinta'
if n0 < n1 and n0 < n2 and n0 < n3 and n0 < n4:
    s = 'primeira'
elif n1 < n2 and n1 < n3 and n1 < n4:
    s = 'segunda'
elif n2 < n3 and n2 < n4:
    s = 'terceira'
elif n3 < n4:
    s = 'quarta'
else:
    s = 'quinta'
print('''A pessoa mais pesada é a {}
A mais leve é a {}'''.format(p, s),)
