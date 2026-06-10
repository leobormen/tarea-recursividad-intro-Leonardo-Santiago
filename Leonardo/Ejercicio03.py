def mayor_lista(lista, num = 0):
    if lista == []:
        return num
    elif lista[0] > num:
        return mayor_lista(lista[1:], num=lista[0])
    else:
        return mayor_lista(lista[1:], num)
    

