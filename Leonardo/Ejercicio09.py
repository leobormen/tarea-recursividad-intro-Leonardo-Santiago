def sublistas_ascendentes(lista):
    if lista == []:
        return lista
    res = [[lista[0]]]
    return sublistas_ascendentes_aux(lista[1:], res)

def sublistas_ascendentes_aux(lista, res):
    numero_en_lista = res[len(res)-1][len(res[len(res)-1])-1]
    if lista == []:
        return res
    elif lista[0] > numero_en_lista:
        res[len(res)-1].append(lista[0])
        return sublistas_ascendentes_aux(lista[1:], res)
    else:
        return sublistas_ascendentes_aux(lista[1:], res+[[lista[0]]])
        
