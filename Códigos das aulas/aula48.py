"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipos
Conhecimentos reutilizaveis - índices e fatiamento
Métodos úteis:
         append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, Ler, alterar, apagar == lista[i] (CRUD)
"""

# lista = [ 1233, 'André lucas', 1.43]
# lista[2] = 'Rolim'
# print(lista)
# print(lista[2])

####### 48 segunda parte


lista2 = [10, 20, 30, 40]
# # lista2[2] = 300
# # del lista2[2]
# # print(lista2)
# # print(lista2[2])
# lista2.append(50)
# lista2.append(60)
# lista2.pop()
# lista2.append(70)
# lista2.append(80)
# lista2.append(90)
# utimo_valor = lista2.pop(3)
# print(lista2, 'removido', utimo_valor)

##########aula 48 terceira parte

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
# lista2.append('Andre')
# nome = lista2.pop()
# lista2.append(123)
# del lista2[-1]
# # lista2.clear()
# lista2.insert(780, 5)
# lista2.insert(740, 55)
# print(lista2)

########### aula 48 quarta parte

# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b
# lista_a.extend(lista_b)
# print(lista_a)

####### aula 48 quinta parte

"""Cuidado com tipos mutáveis
= - copiando o valor (imutáveis)
= - aponta o valor o mesmo valor na memória (mutável)
"""
lista_a = ['André', 'Arthur']
lista_b = lista_a.copy()

lista_a[0] = 'qualquer coisa' # Mesmo mexendo na lista a e imprimindo a lista b o valor é alterado
print(lista_b)                #Para isso é usado a função copy()
