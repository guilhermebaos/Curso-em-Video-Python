d = float(input('Número de dias pelos quais o carro foi alugado: '))
km = float(input('Número de kilómetros percorridos pelo carro: '))
p = d * 20 + km * 0.05
print('Sabendo que por dia o aluguer custa 30€ e por kilómetro 5 centimos extra, o preço do aluguer é {}€'.format(p))
