numeros = []

for i in range(3):
    numeros.append(float(input(f"Digite o {i + 1}º número: ")))


menor = numeros[0]
maior = numeros[0]

for x in numeros:
    if x < menor:
        menor = x
    if x > maior:
        maior = x

print("Menor:", menor, "Maior:", maior)