from discord.ext import commands


class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name="soma", help="Realiza a soma dos argumentos do comando.Uso: !soma <valor1> <valor2> <valorn>")
    async def sum(self, ctx, *values):
        soma = 0
        try:
            for i in values:
                soma += float(i)
        except:
            await ctx.send("Não foi possível processar a soma. Por favor verifique se tudo está certo.")

        await ctx.send(f"O resultado é: {str(soma)}")




async def setup(bot):
    await bot.add_cog(Math(bot))