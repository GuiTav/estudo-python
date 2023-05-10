codigo = input("Digite o código identificador: ")


if len(codigo) != 7:
    print("Código inválido")

elif codigo[0:2] != "BR":
    print("Código inválido")

elif codigo[-1] != "X":
    print("Código inválido")

else:    
    try:
        inteiros = int(codigo[2:6])
        print("Código válido")
    except:
        print("Código inválido")