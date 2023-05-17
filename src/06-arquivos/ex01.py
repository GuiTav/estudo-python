from ex03 import linha_para_dict


def carregar_dados_alunos(nome_arquivo):
    lista = []

    with open(nome_arquivo, "r", encoding="utf8") as arquivo:
        for linha in arquivo:
            aluno = linha_para_dict(linha, ["prontuario", "nome", "email"])
            lista.append(aluno)
    
    return tuple(lista)



print(carregar_dados_alunos("./src/06-arquivos/dados.txt"))