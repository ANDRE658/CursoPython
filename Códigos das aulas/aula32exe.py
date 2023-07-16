"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# input_numero_STR = input('Digite um número inteiro: ')

# try:
#     numero_INT = int(input_numero_STR)
# except:
#     print('Isso não é um número inteiro')
    
# verificar_numero_par_ou_ipmar = (int(input_numero_STR) % 2 == 0 )

# if verificar_numero_par_ou_ipmar:
#     print(f'O número {input_numero_STR} é um número PAR')
# else:
#     print(f'O número {input_numero_STR} é um número IMPAR')

# print(50 * '__')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# input_hora_atual = input('Digite a hora atual: ')
# horas = float(input_hora_atual)
# manhã = horas >= 0 and horas < 12
# tarde = horas >= 12 and horas < 18
# noite = horas >= 18 and horas < 24
# if manhã:
#     print(f'Bom dia!!')
# elif tarde:
#     print(f'Boa tarde!!')
# elif noite:
#     print(f'Boa noite!!')
# else:
#     print('Não conheço essa hora')
# print(50 * '__')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input('Digite seu primeiro nome: ')

nome_curto = len(primeiro_nome) > 1 and len(primeiro_nome) <= 4
nome_normal = len(primeiro_nome) >= 5 and  len(primeiro_nome) <= 6
nome_longo = len(primeiro_nome) > 6

if nome_curto:
    print("Seu nome é curto")
elif nome_normal:
    print("Seu nome é normal")
elif nome_longo:
    print("Seu nome é muito grande")
else:
    print("Digite mais de uma letra")