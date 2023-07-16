"""
Introdução ao try/axecept
try -> tentar executar o código
exept -> ocorreu algum erro ao temtar execultar
"""

numero_str = input('Vou dobra o número que você digitar: ')
#sempre tratar o valor do input

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('float', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')
'''if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
else:
    print('Isso não é um número')'''