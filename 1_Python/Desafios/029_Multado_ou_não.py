v = float(input('A que velocidade estás a viajar (em km/h)? '))
if v >= 80:
    print('Estás em excesso de velocidade!')
    print('Terás de pagar uma multa de {}€'.format((v - 80) * 2))
else:
    print('OK')
