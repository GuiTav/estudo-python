
def somar(n1, n2):
    return n1 + n2

def dividir(dividendo, divisor):
    return dividendo / divisor



# Chamada com argumentos posicionais
# O primeiro número passado para a função se torna n1 e o segundo se torna n2
print(somar(7, 8)) # n1: 7, n2: 8
print(somar(8, 7)) # n1: 8, n2: 7
print(dividir(10, 5)) # dividendo: 10, divisor: 5


# Chamada com argumentos nomeados
# Não importa a posição. O argumento n1 pode ser passado em terceiro lugar, caso seja nomeado
print(somar(n2=6, n1=9))
print(dividir(divisor=7, dividendo=14))


# Unpack list e tuple
# Permite selecionar os valores de uma lista ou tupla e passá-los de forma posicional à função
lista = [15, 3]
tupla = (18, 6)

print(somar(*lista))
print(dividir(*lista))
print(somar(*tupla))
print(dividir(*tupla))


# Unpack dict
# Como o unpack list mas pode passar os argumentos de forma nomeada
# Porém, com apenas um asterisco, o python seleciona apenas as keys do dicionário e com dois asteriscos
# ocorre a seleção dos values
dicionario = {
    "n1": 10,
    "n2": 15
}


print(somar(**dicionario))



# Default values
# É possível criar funções que possuem valores de argumentos padrão
# Caso o usuário não os passe, python faz com que aquele argumento deve assuma seu valor padrão

def saudacao(nome, saudacao="Olá"):
    return f"{saudacao} {nome}"


print(saudacao("Guilherme"))
print(saudacao("Guilherme", "Bom dia"))
print(saudacao(saudacao="Hey", nome="Guilherme"))