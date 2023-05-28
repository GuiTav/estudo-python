from discord.ext import commands
import discord


class Files(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name="cadastrar-aluno", help="Cadastra um aluno no arquivo alunos.txt. Uso: !cadastrar-aluno <prontuário> <nome> <email>")
    async def insert_student(self, ctx, prontuario, nome, email):
        try:
            arquivo = open("./alunos.txt", "r+", encoding="utf8")
            for linha in arquivo:
                prontuario_arquivo = linha.split(",")[0]
                if prontuario == prontuario_arquivo:
                    await ctx.send("O aluno já está cadastrado")
                    return
        

        except FileNotFoundError:
            arquivo = open("./alunos.txt", "w", encoding="utf8")
        

        except Exception as e:
            arquivo.close()
            print(e)
            await ctx.send("Um erro desconhecido ocorreu")
            return
        

        linha_adicional = f"{prontuario},{nome},{email}\n"
        arquivo.write(linha_adicional)
        arquivo.close()
        await ctx.send("Aluno cadastrado com sucesso!")
    


    @commands.command(name="listar-alunos", help="Exibe todos os alunos do arquivo alunos.txt. Uso: !listar-alunos")
    async def list_students(self, ctx):
        embed = discord.Embed(title="Lista de alunos cadastrados", color=0x0000FF)
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar.url)

        try:
            with open("./alunos.txt", "r", encoding="utf8") as arquivo:
                for linha in arquivo:
                    dados = linha.split(",")
                    embed.add_field(name=dados[0], value=f"Nome: {dados[1]} --- Email: {dados[2]}", inline=False)
                
                await ctx.send(embed=embed)
        
        except FileNotFoundError:
            await ctx.send("Não há nenhum aluno cadastrado")
        
        except Exception as e:
            print(e)
            await ctx.send("Algum erro inesperado ocorreu")





async def setup(bot):
    await bot.add_cog(Files(bot))