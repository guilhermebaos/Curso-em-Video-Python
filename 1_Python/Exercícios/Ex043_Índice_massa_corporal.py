p = float(input('Quanto pesa? '))
a = float(input('Quanto mede? '))
IMC = p / a ** 2
p1 = 18.5 * a**2
p2 = 25 * a**2
print('O seu ìndice de massa corporal é {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Está abaixo do seu peso ideal')
elif IMC < 25:
    print('Parabéns, está com um peso ideal')
elif IMC < 30:
    print('Está um pouco acima do seu peso ideal (Staus: Sobrepeso)')
elif IMC < 40:
    print('Está um bocado acima do seu ideal (Status: Obesidade)')
else:
    print('Está muito acima do seu peso ideal, cuidado! (Status: Obesidade mórbida)')
print('O seu peso ideal é entre {} e {}'.format(p1, p2))