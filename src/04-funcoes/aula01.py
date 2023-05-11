
# Funções são blocos de código que podem ser executados para cumprir uma determinada tarefa
# Pode ser usado para evitar duplicação de código

# Existem funções que já vêm prontas no python
# Standard Library Functions - built-in functions
# Ex: print, len

print(len("Nome"))


# Existem também funções definidas pelo próprio usuário
# User Defined Functions

# Declaração
# Nome: saudacoes
# Parâmetros: nenhum
# Retorno: nenhum
def saudacoes():
    print("Bom dia!")


# Chamada
saudacoes()
saudacoes()


# Declaracao
# Nome: saudacoes
# Parametros: nome
# Retorno: nenhum
def saudacoes(nome):
    print(f"Olá {nome}")


# Chamada
# É possível passar literais, variáveis e expressões como argumentos
saudacoes("Guilherme") # "Guilherme" é um argumento para a função
saudacoes("Maria")
sobrenome = "Silva"
saudacoes(sobrenome)



# Declaração
# Nome: calcular_media
# Argumentos: nota1, nota2, nota3
# Retorno: nenhum
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    print(media)


# Chamada
# Chamada com literal
calcular_media(10, 6.8, 9.2)

n1 = 8
n2 = 9
n3 = 10
# Chamada com variáveis
calcular_media(n1, n2, n3)



# Declaração
# Nome: calcular_media
# Argumentos: nota1, nota2, nota3
# Retorno: media
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media


media = calcular_media(7.4, 8.6, 9.9)
print(f"Valor da media {media}")