from ex03 import linha_para_dict


def carregar_dados_alunos(nome_arquivo):
    lista = []

    with open(nome_arquivo, "r", encoding="utf8") as arquivo:
        for linha in arquivo:
            aluno = linha_para_dict(linha, ["prontuario", "nome", "email"])
            lista.append(aluno)
    
    return tuple(lista)



# Não é possível reutilizar a mesma função do ex03.py pois ela não converte o código para int
# A conversão é requerida no enunciado

def carregar_dados_projetos(nome_arquivo):
    lista = []

    with open(nome_arquivo, "r", encoding="utf8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            aluno = {"codigo": int(dados[0]), "titulo": dados[1], "responsavel": dados[2]}
            lista.append(aluno)
    
    return tuple(lista)