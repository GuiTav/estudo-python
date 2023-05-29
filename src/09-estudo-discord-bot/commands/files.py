import discord
from discord.ext import commands
from discord import app_commands, ui
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, Spacer, TableStyle
from reportlab.lib.styles import getSampleStyleSheet


class Files(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    

    @commands.command()
    async def sync(self, ctx):
        comandos_sincronizados = await ctx.bot.tree.sync()
        await ctx.send(f"{len(comandos_sincronizados)} slash commands sincronizados.")


    @app_commands.command(name="modal-cadastro" ,description="Cadastra um aluno no arquivo alunos.txt")
    async def modal_insert(self, interaction):
        await interaction.response.send_modal(modal_aluno())

    

    @app_commands.command(name="listar-alunos", description="Exibe todos os alunos do arquivo alunos.txt")
    async def list_students(self, interaction, modo: str = None):
        if modo == "pdf":
            await cria_pdf_alunos(interaction)
        
        elif modo == None:
            await cria_embed_alunos(interaction, self.bot)
        
        else:
            interaction.response.send_message("Por enquanto só há o modo padrão e o pdf")




async def cria_embed_alunos(interaction, bot):
    embed = discord.Embed(title="Lista de alunos cadastrados", color=0x0000FF)
    embed.set_author(name=bot.user, icon_url=bot.user.avatar.url)

    try:
        linhas = ler_alunos("alunos.txt")
        for linha in linhas:
            embed.add_field(name=linha[0], value=f"Nome: {linha[1]} --- Email: {linha[2]}", inline=False)
        
        await interaction.response.send_message(embed=embed)

    
    except FileNotFoundError:
        await interaction.response.send_message("Não há nenhum aluno cadastrado")
    
    except Exception as e:
        print(e)
        await interaction.response.send_message("Algum erro inesperado ocorreu")




async def cria_pdf_alunos(interaction):

    try:
        dados = ler_alunos("alunos.txt")
    
    except FileNotFoundError:
        await interaction.response.send_message("Não há nenhum aluno cadastrado")
        return
    
    except Exception as e:
        print(e)
        await interaction.response.send_message("Algum erro inesperado ocorreu")
        return



    nome_pdf = "alunos.pdf"
    doc = SimpleDocTemplate(nome_pdf, pagesize=letter)

    styles = getSampleStyleSheet()
    conteudo = []

    titulo = Paragraph("Alunos cadastrados", style=styles["Heading1"])
    conteudo.append(titulo)


    conteudo.append(Spacer(1, 30))

    header = ["Prontuário", "Nome", "Email"]
    dados.insert(0, header)

    estiloTabela = TableStyle([
        ("BACKGROUND", (0,0), (2,0), "black"),
        ("TEXTCOLOR", (0,0), (2,0), "white"),
        ("GRID", (0,0), (-1,-1), 1, "black"),
        ("FONTSIZE", (0, 0), (-1, -1), 12),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE")
    ])

    tabela = Table(dados, colWidths="33%", rowHeights=30)
    tabela.setStyle(estiloTabela)

    conteudo.append(tabela)


    conteudo.append(Spacer(1, 20))


    total_alunos = Paragraph(f"<b>Total de alunos: </b>{len(dados) - 1}")
    conteudo.append(total_alunos)

    doc.build(conteudo)
    
    await interaction.response.send_message("O pdf foi criado com sucesso")



def ler_alunos(path):
    linhas = []

    with open(path, mode="r", encoding="utf8") as arquivo:
        for linha in arquivo:
            dados = linha.split(",")
            linhas.append(dados)

    return linhas



class modal_aluno(ui.Modal, title="Informações do aluno"):
    prontuario = ui.TextInput(label="Digite o prontuário do aluno")
    nome = ui.TextInput(label="Digite o nome do aluno")
    email = ui.TextInput(label="Digite o email do aluno")

    async def on_submit(self, interaction):
        try:
            arquivo = open("./alunos.txt", "r+", encoding="utf8")
            for linha in arquivo:
                prontuario_arquivo = linha.split(",")[0]
                if self.prontuario.value == prontuario_arquivo:
                    await interaction.response.send_message("O aluno já está cadastrado")
                    return
        

        except FileNotFoundError:
            arquivo = open("./alunos.txt", "w", encoding="utf8")
        

        except Exception as e:
            arquivo.close()
            print(e)
            await interaction.response.send_message("Um erro desconhecido ocorreu")
            return
        

        linha_adicional = f"{self.prontuario.value},{self.nome.value},{self.email.value}\n"
        arquivo.write(linha_adicional)
        arquivo.close()
        await interaction.response.send_message("Aluno cadastrado com sucesso!")




async def setup(bot):
    await bot.add_cog(Files(bot))