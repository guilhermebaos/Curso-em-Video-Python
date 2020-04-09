print('DIVISÃO EM PYTHON\n')

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError) as erro1:
    print(f'Ocorreu um erro com os valores que introduziu.')
except ZeroDivisionError as erro2:
    print('Não é possível dividir por 0.')
except KeyboardInterrupt as erro3:
    print('Não inseriu od dados!')
except Exception as erro:        # Catch-all exception
    print(f'O erro foi causado por {erro.__cause__}')
else:
    print(f'O resultado da divisão é {r:.2}')
finally:
    print('\nEspero que o preograma tenha sido útil!')