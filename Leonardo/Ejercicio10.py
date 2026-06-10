def contar_seguidos(lista, num):
    if lista == []:
        return 0
    elif lista[0] != num:
        return 0
    else:
        return 1 + contar_seguidos(lista[1:], num)

def comprimir_repetidos(lista):
    if lista == []:
        return []
    else:
        return [[lista[0],contar_seguidos(lista, lista[0])]] + comprimir_repetidos(lista[contar_seguidos(lista, lista[0]):])
    
