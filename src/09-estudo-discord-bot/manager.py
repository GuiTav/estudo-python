import os
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument


class Manager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.load_extension("tasks")

        for file in os.listdir("./src/09-estudo-discord-bot/commands"):
            if file.endswith(".py"):
                await self.bot.load_extension(f"commands.{file[:-3]}")
        

        print(f"Pronto! Bot disponível como {self.bot.user}")


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            await ctx.send("Comando não existente. Digite !help para ver a lista de comandos do bot")
        elif isinstance(error, MissingRequiredArgument):
            await ctx.send("Está faltando algum argumento para o comando. Verifique seu uso em !help")
        else:
            raise error



async def setup(bot):
    await bot.add_cog(Manager(bot))