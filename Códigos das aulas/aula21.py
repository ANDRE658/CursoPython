# Operadores lógicos
# and (e) or (ou) no (não)
# and -> qual quer expreção verdadeira avaliará a expreção como verdadeira
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha')
senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
# Dependento da sua condição ele retornará ela como valor falso
print(True and True and False)


