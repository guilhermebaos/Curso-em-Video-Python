dias = int(input('Durante quantos dias foi o carro alugado: '))
km = float(input('Kilómetros andados: '))
custo = dias * 60 + km * 0.15
print('O total a ser pago é R${}'.format(custo))
