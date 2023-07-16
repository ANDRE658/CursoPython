"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
'''nome_do_usuario =input('Digite seu nome: ')
idade_do_usuario = input('Digite sua idade: ')

if nome_do_usuario != "" and idade_do_usuario != '':
    print(f'Seu nome é {nome_do_usuario}')
    print(f'Seu nome invertido é', nome_do_usuario[::-1])
    if " " in nome_do_usuario:
        print(f'Seu nome contém espaços')
    else:
        print(f'Seu nome não contém espaços')
    print(f'Seu nome contém', len(nome_do_usuario),"letras")
    print(f'A primeira letra do seu nome é', nome_do_usuario[0])
    print(f'A ultima letra do seu nome é', nome_do_usuario[::len(nome_do_usuario)])
else:
    print(f"Desculpe, você deixou campos vazios.")'''


#correção
    
nome_do_usuario =input('Digite seu nome: ')
idade_do_usuario = input('Digite sua idade: ')

if nome_do_usuario and idade_do_usuario: # os campos sem valor em bool são false
    print(f'Seu nome é {nome_do_usuario}') # certo
    print(f'Seu nome invertido é {nome_do_usuario[::-1]}') #certo 

    if " " in nome_do_usuario: #certo
        print(f'Seu nome contém espaços')
    else:
        print(f'Seu nome não contém espaços')

    print(f'Seu nome contém {len(nome_do_usuario)} letras')
    print(f'A primeira letra do seu nome é {nome_do_usuario[0]}')
    print(f'A ultima letra do seu nome é {nome_do_usuario[-1]}')
else:
    print(f"Desculpe, você deixou campos vazios.")

