def contar_pares(numero):
    return contar_pares_aux(0, numero)

def contar_pares_aux(res, numero):
    if numero == 0:
        return res
    
    elif numero % 10 % 2 == 0:
        return contar_pares_aux(res + 1, numero//10)
    else : 
        return contar_pares_aux(res, numero//10)

