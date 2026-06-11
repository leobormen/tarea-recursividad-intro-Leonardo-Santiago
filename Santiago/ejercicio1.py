#Suma de digitos

def sumar_digitos(numero):
    return sumar_digitos_aux(0, numero)

def sumar_digitos_aux(res, num):
    if num == 0:
        return res
    else:
        res += num % 10 
        return sumar_digitos_aux(res, num // 10)
    
