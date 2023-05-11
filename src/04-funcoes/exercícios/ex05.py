
def calcular_imc(individuo):
    imc = individuo["peso"] / (individuo["altura"] ** 2)
    return imc


def obter_classificacao(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Excesso de peso"
    elif 30 <= imc < 35:
        return "Obesidade de classe 1"
    elif 35 <= imc < 40:
        return "Obesidade de classe 2"
    else:
        return "Obesidade de classe 3"


def situacao_individuo(imc):
    if imc < 18.5:
        return "Ganhar peso"
    elif 18.5 <= imc < 25:
        return "Normal"
    else:
        return "Perder peso"



peso = float(input("Digite o seu peso: "))
altura = float(input("Digite o seu altura: "))

individuo = {
    "peso": peso,
    "altura": altura
}


imc = calcular_imc(individuo)
print("IMC:", imc)
print("Classificação:", obter_classificacao(imc))
print("Situação:", situacao_individuo(imc))