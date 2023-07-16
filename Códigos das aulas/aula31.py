"""
Flag (Bandeira) - Marcar um local
None = não valor 
is e is not = é ou não é (tipo, valor, identidade)
id = identidade

is faz uma pergunta ex.: "isso é um pão"
se for verdade o programa responde TRUE, caso contrário FALSE
Obs.: O not is nega a afirmação de is
"""
v1 = "a"
v2 = "b"
print(id(v1))
print(id(v2))

condição = False
passou_no_if = None 
if condição:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if, passou_no_if is not None)
print(passou_no_if, passou_no_if is  None)

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')