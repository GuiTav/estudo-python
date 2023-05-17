
def carregar_dados_projetos(nome_arquivo):
    lista = []

    with open(nome_arquivo, "r", encoding="utf8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            aluno = {"codigo": int(dados[0]), "titulo": dados[1], "responsavel": dados[2]}
            lista.append(aluno)
    
    return tuple(lista)


print(carregar_dados_projetos("./src/06-arquivos/projeto.txt"))