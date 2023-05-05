# Input e output de dados (entrada e saída de dados)

# A função print realiza a saída de dados pelo sys stdout, a saída padrão
print("Hello world!")


# É possível substituir a saída padrão também
arquivo = open("saida.txt", "w", encoding="utf-8")
print("Isso aqui não vai sair pelo stdout, vai sair pelo arquivo saída.txt", file=arquivo)


# Input de dados - Entrada
# A entrada padrão é feita pela função input
entrada = input("Digite algo: ") # A entrada de dados sempre será feita pelo tipo string
print(f"O usuário entrou com os seguintes dados: {entrada} {type(entrada)}")


# Também é possível realizar a entrada de dados por arquivos
entrada_arquivo = open("entrada.txt", "r", encoding="utf-8")
conteudo = entrada_arquivo.read() # O conteúdo do arquivo vem sempre como uma string
print(conteudo.split(";")) # É possível "quebrar" strings em caracteres específicos e fazer uma lista com as partes separadas