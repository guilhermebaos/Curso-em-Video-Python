def _notas(*notas, sit=False):
    info = dict()
    info['n_notas'] = len(notas)
    info['melhor_nota'] = max(notas)
    info['pior_nota'] = min(notas)
    s = sum(notas) # Soma todos os valores do dicionário
    average = s / len(notas)
    info['média'] = f'{average:.2f}'
    if sit:
        if average < 10:
            info['situação'] = 'A média é má'
        elif average > 16:
            info['situação'] = 'A média é excelente'
        else:
            info['situação'] = 'A média é boa'
    return info


print(_notas(11, 12, 13, 14, 15, 6, 7, 8, 9, 10, 12, 20, 20, 20, sit=True))
