#Contar Bloques

def contar_bloques_iguales(lista):
    if lista == []:
        return 0
    return contar_bloques_aux(lista[0], lista[1:])

def contar_bloques_aux(elem, lista):
    if lista == []:
        return 1 #Retorna el ultimo elemento
    elif elem == lista[0]:
        return 0 + contar_bloques_aux(lista[0], lista[1:])
    else:
        return 1 + contar_bloques_aux(lista[0], lista[1:])
