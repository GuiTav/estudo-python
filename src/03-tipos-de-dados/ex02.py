meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
"Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

mes = int(input("Digite o número do mês do ano: "))

if 1 <= mes <= 12:
    print(f"O mês do ano é: {meses[mes - 1]}")
else:
    print("Mês inválido")