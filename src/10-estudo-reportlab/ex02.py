from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# Cria um objeto SimpleDocTemplate com o nome do arquivo e o tamanho da página
pdf_file = "exemplo.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter)

# Obtém o estilo de folha de estilos de exemplo
styles = getSampleStyleSheet()

# Cria uma lista de elementos de conteúdo do PDF
content = []

# Adiciona um título com fonte 16pt
title_text = "<font size='16'>Título do Documento</font>"
title = Paragraph(title_text, styles["Heading1"])
content.append(title)

# Adiciona um espaço de 20pt após o título
content.append(Spacer(1, 20))

# Adiciona o primeiro parágrafo com fonte 12pt
paragraph1_text = "Este é o primeiro parágrafo com fonte 12pt."
paragraph1 = Paragraph(paragraph1_text, styles["BodyText"])
content.append(paragraph1)

# Adiciona um espaço de 15pt entre os parágrafos
content.append(Spacer(1, 15))

# Adiciona o segundo parágrafo com fonte 12pt
paragraph2_text = "Este é o segundo parágrafo com fonte 12pt."
paragraph2 = Paragraph(paragraph2_text, styles["BodyText"])
content.append(paragraph2)

# Adiciona o terceiro parágrafo
estilo_parag_3 = ParagraphStyle(
    name="paragrafo3",
    fontSize = 30,
    alignment = 1,
    leading = 24
)


paragraph3_text = "Este é o terceiro parágrafo, adicionado para o exercício da semana."
paragraph3 = Paragraph(paragraph3_text, estilo_parag_3)
content.append(paragraph3)




# Adiciona o quarto parágrafo
estilo_parag_4 = ParagraphStyle(
    name="paragrafo4",
    fontSize = 6,
    alignment = 0,
    leading = 10
)


paragraph4_text = "Este é o quarto parágrafo, bem pequeno."
paragraph4 = Paragraph(paragraph4_text, estilo_parag_4)
content.append(paragraph4)




# Constrói o documento PDF com o conteúdo fornecido
doc.build(content)

print("PDF criado com sucesso.")
