def eliminar_impares(num):
    return eliminar_impares_aux(0, num)

def eliminar_impares_aux(exp, num):
    if num == 0:
        return 0
    else:
        if num % 10 % 2 == 0:
            return (num % 10)*(10**exp) + eliminar_impares_aux(exp +1, num //10)
        else :
            return 0 + eliminar_impares_aux(exp, num//10)
        
