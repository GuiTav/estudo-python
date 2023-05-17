breakpoint()

def soma(*numeros):
    soma = 0
    for i in numeros:
        soma += i
    
    return soma


resultado = soma(2, 5, 4, 6, 3)
print(resultado)