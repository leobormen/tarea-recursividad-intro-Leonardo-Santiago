def detectar_valles(lista):
    return [] + detectar_valles_aux(lista)

def detectar_valles_aux(lista):
    if len(lista) < 2:
        return []
    elif  lista[1] < lista[0] and lista[1] < lista[2]:
        return [[lista[0], lista[1], lista[2]]] + detectar_valles_aux(lista[2:])
    else:
        return detectar_valles_aux(lista[1:])

