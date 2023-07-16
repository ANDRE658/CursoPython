nome = 'André Lucas'
altura = 1.83
peso = 83
imc = peso / (altura**2)

#f-strings
linha1 = f'{nome} tem {altura:.2f} de altura'
linha2 = f'pesa {peso} e seu IMC é'
linha3 = f'{imc:.2f}'
print(linha1)
print(linha2)
print(linha3)