p = float(input('Preço do produto (€): '))
print('''Formas de pagamento: 
[ 1 ] À vista em dinheiro / cheque
[ 2 ] À vista em cartão
[ 3 ] Duas vezes no cartão
[ 4 ] Três ou mais vezes no cartão''')
o = int(input('Forma de pagamento pretendida: '))
if o == 1:
    pf = p * 0.9
elif o == 2:
    pf = p * 0.95
elif o == 3:
    pf = p
    print('O preço de cada pagamento (2 parcelas) será de {}€'.format(pf / 2))
elif o == 4:
    pf = p * 1.2
    c = int(input('Quantidade de vezes que vai pagar com o cartão: '))
    print('O preço de cada pagamento ({} parcelas) será de {}€'.format(c, pf / c))
else:
    pf = 'ERRO'
    print('Essa função não existe!')
print('O preço final do produto é {}€'.format(pf))
