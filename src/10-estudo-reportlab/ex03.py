from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

# Cria um objeto SimpleDocTemplate com o nome do arquivo e o tamanho da página
pdf_file = "exemplo.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter)

# Obtém o estilo de folha de estilos de exemplo
styles = getSampleStyleSheet()

# Imagem do ReportLab
logo = Image(filename="logo_reportlab.png", width=200, height=40)

# Título com fonte 16pt
titulo = Paragraph("<font size='16'>Título do Relatório</font>", styles["Heading1"])

# Parágrafo com fonte 12pt
paragrafo_texto = "Este é um parágrafo com fonte 12pt."
paragrafo = Paragraph(paragrafo_texto, styles["BodyText"])

# Tabela
dados = [["Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4"],
         ["Linha 1", "Linha 1", "Linha 1", "Linha 1"]]

tabela = Table(dados)

# Espaçamentos
espaco_titulo_paragrafo = Spacer(1, 20)  # Espaço de 20pt entre o título e o parágrafo
espaco_paragrafo_tabela = Spacer(1, 15)  # Espaço de 15pt entre o parágrafo e a tabela

# Constrói o documento PDF com o conteúdo fornecido
content = [logo, titulo, espaco_titulo_paragrafo, paragrafo, espaco_paragrafo_tabela, tabela]
doc.build(content)
