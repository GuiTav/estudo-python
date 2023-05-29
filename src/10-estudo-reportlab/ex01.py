from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Cria um novo arquivo PDF
pdf_file = "exemplo.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)

# Adiciona o texto "Hello World"
c.setFont("Helvetica", 12)
c.drawString(100, 700, "Hello World")

# Adiciona um retângulo
c.rect(100, 650, 200, 100, fill=1, stroke=0)

# Adiciona um círculo
c.ellipse(350, 650, 450, 750, fill=1, stroke=0)

# Salva e fecha o arquivo PDF
c.showPage()
c.save()

print("PDF criado com sucesso.")
