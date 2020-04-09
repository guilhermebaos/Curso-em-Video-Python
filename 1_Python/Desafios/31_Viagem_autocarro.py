km = float(input('De quantos kilómetros será a viagem? '))
if km <= 200:
    print('A viagem custará {:.2f}€ (0.1€/km)'.format(km * 0.1))
else:
    print('A visgem custará {:.2f} € (0.09€/km)'.format(km * 0.09))
