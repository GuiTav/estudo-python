from discord.ext import commands, tasks
import datetime


class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @tasks.loop(seconds=10)
    async def tempo(self):
        now = datetime.datetime.now()
        now = now.strftime("%d/%m/%Y - %H:%M:%S")
        channel = self.bot.get_channel(1111735377443692666)
        await channel.send(now)




async def setup(bot):
    await bot.add_cog(Tasks(bot))