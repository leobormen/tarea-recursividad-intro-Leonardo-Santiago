def contar_pares(num):
    if num == 0:
        return 0
    elif num%10%2 == 0:
        return 1 + contar_pares(num//10)
    else:
        return contar_pares(num//10)
    