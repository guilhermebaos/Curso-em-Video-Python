n = str(input('Como te chamas? ')).strip()
n1 = n.split()
print('''Gosto em conhecer-te!
O teu primeiro nome é {}
O teu último nome é {}'''.format(n1[0], n1[len(n1) - 1]))
