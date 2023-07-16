frase = '#Essa condição fará com que a letra que apareceu mais vezes fique armazenada na váriavel' \
        'qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual #a condição faz a checagem da utima letra com a penultima a maior é armazenada'

i = 0
qtd_apareceu_mais_vezes = 0 #Aqui será armazenado a qtd de vezes em que a letra apareceu
letra_apareceu_mais_vezes = '' #Aqui será armazenado a letra que aparece mais vezes 

while i < len(frase):
    letra_atual = frase[i] #Aqui fará a passagen da letra de acordo com o indice

    if letra_atual == ' ':
        i += 1
        continue

    repeticao_letra_atual = frase.count(letra_atual)#Atribuirá a letra o número de veses em que a letra atual repetiu

    if qtd_apareceu_mais_vezes < repeticao_letra_atual: #Essa condição fará com que a letra que apareceu mais vezes fique armazenada na váriavel 
        qtd_apareceu_mais_vezes = repeticao_letra_atual #a condição faz a checagem da utima letra com a penultima a maior é armazenada
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)

# De uma olhada no código acima
#
