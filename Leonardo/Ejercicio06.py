def contar_bloques_iguales(lista, bloques=[], num=0):
    if lista == []:
        return len(bloques)
    elif lista[0] == num:
        bloques[len(bloques)-1].append(lista[0])
        return contar_bloques_iguales(lista[1:], bloques, lista[0])
    else:
        return contar_bloques_iguales(lista[1:], bloques+[[lista[0]]], lista[0])