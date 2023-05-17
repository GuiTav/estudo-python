
def linha_para_dict(linha, lista_chaves):
    dicio = {}
    dados = linha.strip().split(",")
    for iter in range(len(lista_chaves)):
        dicio[lista_chaves[iter]] = dados[iter]
    
    return dicio