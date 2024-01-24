#Programa hecho en curso de aprendizaje en python
#Los comentarios son por que los prints no son necesarios para que las funciones actuen
#

# crear lista

import random

#Pide un numero para ser la cantidad y rango
def crea_desordenados(n):
    lista =[]

    while len(lista) < n:
        ale=random.randint(0,n)
        if not(ale in lista):
            lista.append(ale)

    #print(lista)
    return lista


#Pide una lista ya hecha
def ordena(lista):

# ordenar lista
# print("parte de ordenar uwu")
    n = len(lista)
    for c in range (n):
        ordenados = False 

        if ordenados == False:
            
            for c2 in range (n-1):
                if lista[c2] > lista[c2+1]:
                    tempo = lista[c2]
                    lista[c2] = lista [c2+1]
                    lista[c2+1] = tempo
                else:
                    ordenados= True
            #print(lista)
    return lista

#Esto es para visualizar lo creado si es necesario
#a= crea_desordenados(10)
#print("La lista:",a)
#b= ordena(a)
#print("La lista ordenada:", b)
