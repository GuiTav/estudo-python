from discord.ext import commands
from discord import Embed
import requests


class Miscellaneous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(help="Busca pelos dados de um pokemon e retorna-os ao usuário.Uso: !pokemon <nome_do_pokemon>")
    async def pokemon(self, ctx, pokemon):
        try:
            poke_name = pokemon.lower()
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke_name}/")
            if response.status_code == 404:
                raise ValueError() # O pokémon não foi encontrado pela API
            
            data = response.json()
            nome = data.get("name")
            id = data.get("id")
            peso = data.get("weight")
            tipos = data.get("types")
            img_link = data.get("sprites").get("front_default")

            await ctx.send(embed=create_embed_pokemon(self.bot, nome, id, peso, tipos, img_link))

        except ValueError:
            await ctx.send("Pokémon não encontrado")
            return

        except Exception as e:
            print(e)
            await ctx.send("Houve algum erro")
            return





def create_embed_pokemon(bot, nome, id, peso, tipos, img_link):
    embed = Embed(title="PokeDex do Massa", color=0xFF0000)
    
    embed.set_author(
        name=bot.user.name,
        icon_url=bot.user.avatar.url
    )

    embed.add_field(name="Nome", value=nome.upper())
    embed.add_field(name="ID", value=id)
    embed.add_field(name="Peso", value=peso)

    nome_tipos = []
    for tipo in tipos:
        nome_tipos.append(tipo.get("type").get("name"))
    embed.add_field(name=f"Tipos", value=", ".join(nome_tipos), inline=False)

    embed.set_image(url=img_link)

    return embed





async def setup(bot):
    await bot.add_cog(Miscellaneous(bot))