#Se define una funcion para contar digitos, cuestion de facilitarnos la vida

def contar_digitos(num):
    if num == 0:
        return 0
    else :
        return 1 + contar_digitos(num // 10)
    
def invertir_numero(num):
    return invertir_numero_aux(contar_digitos(num) -1, num)

def invertir_numero_aux(exp, num):
    if exp == -1:
        return 0
    else:
        return (num % 10)*(10**exp) + invertir_numero_aux(exp -1, num//10)
    
