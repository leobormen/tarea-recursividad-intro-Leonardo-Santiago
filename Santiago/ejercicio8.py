def detectar_valles(lista):

    if len(lista) < 3:
        return []
    
    if lista[1] < lista [0] and lista [1] < lista[2]:
        return [[lista[0], lista[1], lista[2]]] + detectar_valles(lista[1:])
    
    else :
        return detectar_valles(lista[1:])

