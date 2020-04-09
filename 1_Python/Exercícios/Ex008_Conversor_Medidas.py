m = float(input('Escreve um comprimento (em metros):'))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m / 0.1
cm = m / 0.01
mm = m / 0.001
print('{} metros correspondem a:'.format(m), end='')
print('\n {} km; \n {} hm; \n {} dam; \n {} dm; \n {} cm e \n {} mm'.format(km, hm, dam, dm, cm, mm))
