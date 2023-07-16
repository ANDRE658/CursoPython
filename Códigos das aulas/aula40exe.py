#CALCULADORA COM WHILE
print("CALCULADORA")
print(10 *'--')


condicao = 's'
while condicao == 's':
    pri_numero = input('Digite um número: ')
    seg_numero = input('Digite outro número: ')
    operador = input('Qual operação deseja fazer? (+-/*)')
    
    numeros_válidos = None

    try :
        pri_numero_float = float(pri_numero)
        seg_numero_float = float(seg_numero)
        numeros_válidos = True
    except :
        numeros_válidos = None 

    if numeros_válidos == None:
        print('algum número digitado, está inválido.')
        continue

    opredores_valido = '+-*/'

    if operador not in opredores_valido:
        print('Operador inválido.')
        continue

    if len(operador) > 1 :
        print('Digite apenas um operador.')
        continue
    
    print(10 *'--')
    
    print('Confira o resultado abaixo:')

    if operador == '+':
        resutado = pri_numero_float + seg_numero_float
        print(f'{pri_numero} + {seg_numero} = {resutado}')
    elif operador == '-':
        resutado = pri_numero_float - seg_numero_float
        print(f'{pri_numero} + {seg_numero} = {resutado}')
    elif operador == '*':
        resutado = pri_numero_float * seg_numero_float
        print(f'{pri_numero} + {seg_numero} = {resutado}')
    elif operador == '/':
        resutado = pri_numero_float / seg_numero_float
        print(f'{pri_numero} + {seg_numero} = {resutado}')
    
    condicao = input('Deseja continuar? [s]sim/ [n]não ')
    condicao = condicao.lower()
print(10 *'--')
print('Ecerrado')
