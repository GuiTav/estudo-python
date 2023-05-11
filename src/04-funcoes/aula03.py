
# É possível criar funções com um número indefinido de argumentos

def media(aluno, *notas):
    soma = 0
    for i in notas:
        soma += i
    return f"A média do(a) aluno(a) {aluno} é {soma / len(notas)}"


print(media("Afonso", 2, 4, 6, 8, 10))


# É possível criar também uma função com argumentos opcionais passados de forma nomeada

def calculo_preco(valor, **kwargs):
    imposto = kwargs.get("imposto")
    desconto = kwargs.get("desconto")

    if imposto:
        valor += valor * (imposto / 100)
    
    if desconto:
        valor -= desconto

    return valor


print("Valor:", calculo_preco(20))
print("Valor:", calculo_preco(20, imposto=10))
print("Valor:", calculo_preco(20, imposto=10, desconto=4))
print("Valor:", calculo_preco(20, desconto=4))