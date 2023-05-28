import discord
import asyncio
from decouple import config
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


asyncio.run(bot.load_extension("manager"))



TOKEN = config("TOKEN")
bot.run(TOKEN)
