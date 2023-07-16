# Operadores lógicos
# and (e) or (ou) no (não)
# or -> Qual quer expreção avaliada com verdadeira, avaliará toda expreção como verdadeira

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha')
senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e' ) and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito

print(False or False or 'abc')

senha = input('Senha: ') or 'Sem senha'
print(senha)
