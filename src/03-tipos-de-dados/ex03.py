meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

mes = int(input("Digite o número do mês do ano: "))

if 1 <= mes <= 12:
    print(f"O mês do ano é: {meses[mes - 1]}")
else:
    print("Mês inválido")