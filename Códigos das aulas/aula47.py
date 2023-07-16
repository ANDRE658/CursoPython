import os

palavra_secreta = 'perfume'
tentativas = 0
letra_certas = ''
while True:
    
    letra_digitada = input('Digite uma letra ')

    tentativas +=1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    palavra_formada = '' 
    if letra_digitada in palavra_secreta:
         letra_certas += letra_digitada 

    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_certas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(30 * '_')
        print('VOCÊ GANHOU!!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print(f'Tentativas realizadas: {tentativas}')
        tentativas = 0
        letra_certas = ''