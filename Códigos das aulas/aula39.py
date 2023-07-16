'''
Interando string com while
'''

#       12345678901
nome = 'André lucas' #Iteráveis 

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += letra + '*'
    indice += 1

print(novo_nome)