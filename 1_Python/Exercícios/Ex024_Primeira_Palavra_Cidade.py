n = str(input('Em que cidade nasceste? ')).strip().lower()   #.split()
n1 = n[:5] == 'santo'   # Eu tinha feito assim: 'santo' in n[0]
print('A cidade em que nasceste começa com Santo? {}'.format(n1))
