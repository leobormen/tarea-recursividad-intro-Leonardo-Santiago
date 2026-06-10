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
    
print(invertir_numeros(1234))