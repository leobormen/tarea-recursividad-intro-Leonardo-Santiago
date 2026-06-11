def comprimir_repetidos(lista):
    if lista == []:
        return []
    
    return comprimir_repetidos_aux([lista[0],1], lista[1:], [])

def comprimir_repetidos_aux(sub_res, lista, res):
    if lista == []:
        res.append(sub_res)
        return res
    
    else:
        if sub_res[0] == lista[0]:
            sub_res[1] += 1

            return comprimir_repetidos_aux(sub_res, lista[1:], res)
        else:
            res.append(sub_res)
            sub_res = [lista[0], 1]
            return comprimir_repetidos_aux(sub_res, lista[1:], res)
        

def sublistas_ascendentes(lista):
    if len(lista) == 0:
        return []
    
    if len(lista) == 1:
        return [[lista[0]]]

    resto = sublistas_ascendentes(lista[1:])

    if lista[0] < resto[0]:
        return [[lista[0]] + resto[0]] + resto[1:]
    else:
        return [[lista[0]]] + resto
print(sublistas_ascendentes([1, 2, 3, 1, 4, 5, 2]))
# [[1, 2, 3], [1, 4, 5], [2]]

print(sublistas_ascendentes([5, 4, 3, 2]))
# [[5], [4], [3], [2]]

print(sublistas_ascendentes([1, 3, 5, 7]))
# [[1, 3, 5, 7]]

print(sublistas_ascendentes([2, 2, 3, 1, 2]))
# [[2], [2, 3], [1, 2]]

print(sublistas_ascendentes([]))
# []