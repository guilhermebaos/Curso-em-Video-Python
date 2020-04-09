def fatorial(n, show=False):
    """
    Calcula o fatorial de n
    :param n: Número cujo fatorial vai ser calculado
    :param show: Se True, irá mostrar o processo através do qual n foi calculado
    :return: Retornará apenas o fatorial de n
    Definido recursivamente
    """
    if n == 1:
        if show:
            print(n, end=' = ')
        return 1
    if n != 1:
        if show:
            print(n, end=' x ')
        m = fatorial(n-1, show)
        return n * m


print(fatorial(6, show=False))
