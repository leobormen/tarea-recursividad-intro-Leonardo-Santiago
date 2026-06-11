def sublistas_ascendentes(lista):
    if len(lista) == 0:
        return []
    
    if len(lista) == 1:
        return [[lista[0]]]

    resto = sublistas_ascendentes(lista[1:])

    if lista[0] < resto[0][0]:
        return [[lista[0]] + resto[0]] + resto[1:]
    else:
        return [[lista[0]]] + resto
