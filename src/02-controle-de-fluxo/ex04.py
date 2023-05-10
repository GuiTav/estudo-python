codigo = input("Digite o código identificador: ")

erros = []


if len(codigo) != 7:
    erros.append("Tamanho inválido para código")

if codigo[0:2] != "BR":
    erros.append("O identificador não inicia com a sequência 'BR'")

if codigo[-1] != "X":
    erros.append("O identificador não finaliza com 'X'")

try:
    inteiros = int(codigo[2:6])
    if inteiros < 1 or inteiros > 9999:
        erros.append("Sequência de números inválida")
except:
    erros.append("Sequência de números inválida")
finally:
    if erros:
        print("Código inválido")
    else:
        print("Código válido")

    print(erros)