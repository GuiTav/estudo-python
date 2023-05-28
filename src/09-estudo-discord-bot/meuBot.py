import discord
import os
from decouple import config
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)



@bot.event
async def on_ready():
    await bot.load_extension("manager")

    for file in os.listdir("./src/09-estudo-discord-bot/commands"):
        if file.endswith(".py"):
            await bot.load_extension(f"commands.{file[:-3]}")
    

    print(f"Pronto! Bot disponível como {bot.user}")


TOKEN = config("TOKEN")
bot.run(TOKEN)
