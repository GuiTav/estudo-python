notas = input("Digite as notas no formato (nota1, nota2, nota3, ...):")
notas = notas.split(",")

print(notas)

soma = 0
for i in notas:
    soma += float(i)

print(f"A média das notas é: {soma/len(notas)}")
