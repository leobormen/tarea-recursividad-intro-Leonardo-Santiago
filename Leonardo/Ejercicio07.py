def separar_por_paridad(num, impares=[], pares=[]):
    if num == 0:
        return [impares,pares]
    elif num%10%2 == 0:
        return separar_por_paridad(num//10, impares, pares+[num%10])
    else:
        return separar_por_paridad(num//10, impares+[num%10], pares)
    
print(separar_por_paridad(123456))