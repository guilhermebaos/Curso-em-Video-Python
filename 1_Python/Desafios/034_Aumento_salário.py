s = float(input('Qual é o teu salário? '))
if s > 1000:
    print('Com o aumento de 10%, passarás a receber {:.2f}€'.format(s * 1.1))
else:
    print('Com o aumento de 15%, passarás a receber {:.2f}€'.format(s * 1.15))
