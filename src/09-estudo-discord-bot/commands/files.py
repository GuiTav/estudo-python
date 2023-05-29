from discord.ext import commands
from discord import app_commands, ui
import discord


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
    async def list_students(self, interaction):
        embed = discord.Embed(title="Lista de alunos cadastrados", color=0x0000FF)
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar.url)

        try:
            with open("./alunos.txt", "r", encoding="utf8") as arquivo:
                for linha in arquivo:
                    dados = linha.split(",")
                    embed.add_field(name=dados[0], value=f"Nome: {dados[1]} --- Email: {dados[2]}", inline=False)
                
                await interaction.response.send_message(embed=embed)
        
        except FileNotFoundError:
            await interaction.response.send_message("Não há nenhum aluno cadastrado")
        
        except Exception as e:
            print(e)
            await interaction.response.send_message("Algum erro inesperado ocorreu")



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