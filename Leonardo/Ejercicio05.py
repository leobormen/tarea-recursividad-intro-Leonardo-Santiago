def contar_digitos(num):
    if num == 0:
        return 0
    else:
        return 1 + contar_digitos(num//10)

def invertir_numeros(num, inv=0):
    if num == 0:
        return inv
    else:
        return invertir_numeros(num//10, inv+(num%10)*10**(contar_digitos(num)-1)) 

def eliminar_impares(num, pares=0):
    if num == 0:
        return invertir_numeros(pares)
    elif num%10%2 == 0:
        return eliminar_impares(num//10, pares*10 + num%10)
    else:
        return eliminar_impares(num//10, pares)
    
print(eliminar_impares(12345))
print(eliminar_impares(223344))