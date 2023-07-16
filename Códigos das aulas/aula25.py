'''
interpolação básca de string
s - string
d e i - int
f - float
x e X - Hexadecimal
'''

nome = 'André'
preco = 10000.00003
variaval = '%s, preço é R$%.2f'%(nome, preco)
print(variaval)
print('O hexadecimal de %d é %08X' % (1500, 1500))