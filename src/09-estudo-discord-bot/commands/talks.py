from discord.ext import commands


class Talks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.command(name="oi", help="Envia uma saudação para o usuário.Uso: !oi")
    async def send_hi(self, ctx):
        name = ctx.author.name
        response = f"Olá, {name}"

        await ctx.send(response)
    

    @commands.command(name="segredo", help="Isso é um segredo...Uso: !segredo")
    async def secret(self, ctx):
        await ctx.author.send("shhh, não conta pra ninguém")
        await ctx.author.send("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnZZiyl1EJJji3kVQRH6O_RIg036fIgMBDyw&usqp=CAU")




async def setup(bot):
    await bot.add_cog(Talks(bot))