from Modules_Ex import Ex108
from Modules import my_inputs

preco = my_inputs.inputint('Escreve o preço de um produto, em euros: ')

print(f'''
O produto custa {Ex108.euro(preco)}.

Duas unidades custam {Ex108.euro(Ex108.double(preco))}.
Com 50% de desconto o preço passa a {Ex108.euro(Ex108.half(preco))}.
Com um imposto adidional de 10% o preco passa a {Ex108.euro(Ex108.aumentar(preco, 10))}.
Com uma promoção de 13% o preço passa a {Ex108.euro(Ex108.diminuir(preco, 13))}.
''')
