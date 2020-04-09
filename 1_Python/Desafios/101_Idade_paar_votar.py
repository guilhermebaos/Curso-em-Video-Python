import datetime


def votar(anonascimento=0):
    anonascimento = int(anonascimento)
    if anonascimento > ano:
        return 'ERRO'
    idade = ano - anonascimento
    if idade >= 18:
        return f'Com {idade} anos podes votar!'
    else:
        return f'Com {idade} anos não podes votar!'


ano = datetime.datetime.now().year
an = int(input('Ano de nascimento: '))
print(votar(an))
