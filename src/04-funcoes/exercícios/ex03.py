breakpoint()

def soma(numeros):
    soma = 0
    for i in numeros:
        soma += i
    
    return soma


tupla = (9, 1, 8, 5, 2, 6)
resultado = soma(tupla)
print(resultado)