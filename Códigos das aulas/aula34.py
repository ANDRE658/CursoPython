'''
Repetições 
while == enquanto
Executa uma ação enquanto uma condição fo verdadeira
Loop infinito -> Quando um código não tem fim
'''

condicao = True

while condicao:
    nome = input('Qual o seu nome? ')
    print(f'Seu nome é {nome}')

    if nome == "Sair":
        break

print("Acabou")
