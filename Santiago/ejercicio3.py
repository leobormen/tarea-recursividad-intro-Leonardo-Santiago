def mayor_lista(lista):
    return mayor_lista_aux(lista[0], lista[1:])

def mayor_lista_aux(res, lista):
    if lista == []:
        return res
    else: 
        if lista[0] > res:
            res = lista[0]
            return mayor_lista_aux(res, lista[1:])
        else:
            return mayor_lista_aux(res, lista[1:])
    
