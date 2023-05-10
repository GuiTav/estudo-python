QTDE_NOTAS = 3

notas = []

for i in range(QTDE_NOTAS):
    notas.append(float(input(f"Digite o {i + 1}º número: ")))


soma = 0
for i in notas:
    soma += i

print(f"A média das {QTDE_NOTAS} notas é: {soma/QTDE_NOTAS}")