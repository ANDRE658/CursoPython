'''
Repetições 
while == enquanto
Executa uma ação enquanto uma condição fo verdadeira
Loop infinito -> Quando um código não tem fim
'''
contador = 0

while contador <= 100:
    contador += 1

    if contador == 3:
        print('Essa expreção faz o código voltar ao início')
        continue # 

    if contador >= 10 and contador <= 27:
        print('Pulei o número', contador)
        continue

    print(contador)

    if contador == 40:
        break

    
print('Acabou')