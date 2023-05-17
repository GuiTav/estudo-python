breakpoint()

def calcular_volume(comprimento, largura, altura):
    return (comprimento * largura * altura) / 1000


def potencia_termostato(volume, temp_desejada, temp_ambiente):
    return volume * 0.05 * (temp_desejada - temp_ambiente)


def filtragem_hora(volume):
    return volume * 3


comprimento = float(input("Digite o comprimento do aquario: "))
largura = float(input("Digite a largura do aquario: "))
altura = float(input("Digite a altura do aquario: "))
temp_desejada = float(input("Digite a temperatura desejada: "))
temp_ambiente = float(input("Digite a temperatura do ambiente: "))


volume = calcular_volume(comprimento, largura, altura)
print("Volume:", volume)
print("Potência do termostato:", potencia_termostato(volume, temp_desejada, temp_ambiente))
print("Filtragens por hora:", filtragem_hora(volume))