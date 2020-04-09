from Modules_Ex import Ex109
from Modules import my_inputs

preco = my_inputs.inputint('Escreve o preço de um produto, em euros: ')

print(f'''
O produto custa {Ex109.format_euro(preco)} (Inserido: {preco}).

Duas unidades custam {Ex109.double(preco, True)}.
Com 50% de desconto o preço passa a {Ex109.half(preco, True)}.
Com um imposto adidional de 10% o preco passa a {Ex109.aumentar(preco, 10, True)}.
Com uma promoção de 13% o preço passa a {Ex109.diminuir(preco, 13, True)}.
''')
