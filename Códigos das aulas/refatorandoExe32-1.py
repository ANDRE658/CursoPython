"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
input_número = input('Digite um número: ')

if input_número.isdigit()  :
    numero_int = int(input_número)
    par_ou_impar = numero_int % 2 == 0
    texto = 'impar'
    if par_ou_impar:
        texto = 'par'
        print(f'número {numero_int} é um número {texto}')
    else:
        print(f'número {numero_int} é um número {texto}')
else:
    print('O valor digitado não é inteiro')