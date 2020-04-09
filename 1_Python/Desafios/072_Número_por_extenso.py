d = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'catorze', 'quinze', 'dezasseis', 'dezassete', 'dezoito', 'dezanove', 'vinte')
while True:
    n = str(input('Escreve um número de 0 a 20: '))
    if n.isnumeric():
        n = int(n)
        if 0 <= n <= 21:
            break
print(f'Tu escreveste o número {d[n]}')
