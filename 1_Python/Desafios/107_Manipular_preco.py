from Modules_Ex import Ex107
from Modules import my_inputs

preco = my_inputs.inputint('Escreve o preço de um produto: ')

print(f'''
O produto custa {preco}.

Duas unidades custam {Ex107.double(preco)}.
Com 50% de desconto o preço passa a {Ex107.half(preco)}.
Com um imposto adidional de 10% o preco passa a {Ex107.aumentar(preco, 10)}.
Com uma promoção de 13% o preço passa a {Ex107.diminuir(preco, 13)}.
''')
