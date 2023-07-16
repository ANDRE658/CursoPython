# Operadores in e no in
# Strings são iteráveis
# 0 1 2 3 4 5
# A n d r é
#-5-4-3-2-1
'''nome = 'André'
print(nome[1])
print(nome[-4])
print('é' in nome)
print('g' in nome)
print(10* '-')
print('é' not in nome)
print('g' not in nome)'''

nome_1 = input('Ditige seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome_1:
    print(f'{encontrar} está em {nome_1}')
else:
    print(f'{encontrar} não está em {nome_1}')
