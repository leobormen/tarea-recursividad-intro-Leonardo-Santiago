import ejercicio5
from ejercicio5 import * 

#Separar segun paridad 

def separar_segun_paridad(num):
    return [eliminar_impares(num), eliminar_pares(num)]

def eliminar_pares(num):
    return eliminar_pares_aux(0, num)

def eliminar_pares_aux(exp, num):
    if num == 0:
        return 0
    else:
        if num % 10 % 2 != 0:
            return (num % 10)*(10**exp) + eliminar_pares_aux(exp +1, num //10)
        else :
            return 0 + eliminar_pares_aux(exp, num//10)
