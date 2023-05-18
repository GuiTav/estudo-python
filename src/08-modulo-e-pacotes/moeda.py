
def aumentar(valor, aumento):
    return valor + (valor * (aumento / 100))


def diminuir(valor, diminuicao):
    return valor - (valor * (diminuicao / 100))


def dobro(valor):
    return valor * 2


def metade(valor):
    return valor / 2


def moeda(valor):
    return f"R${valor:.2f}".replace(".", ",")