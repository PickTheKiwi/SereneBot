import disnake
from disnake.embeds import Embed
from disnake.ext import commands

ENABLED = True


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Misc cog loaded")

    @commands.slash_command()
    async def ping(self, interaction):
        latency = round(self.bot.latency * 1000)
        embed_colour = 0x0
        match latency:
            case latency if latency < 50:
                embed_colour = 0x0000FF
            case latency if latency < 100:
                embed_colour = 0x00FFFF
            case latency if latency < 200:
                embed_colour = 0x00FF00
            case latency if latency < 300:
                embed_colour = 0xFFFF00
            case _:
                embed_colour = 0xFF0000

        embed_colour = int(embed_colour)
        embed = Embed(
            title="Pong!", description=f"Bot latency is {latency}ms", color=embed_colour
        )

        await interaction.response.send_message(embed=embed)


def setup(bot):
    if ENABLED:
        bot.add_cog(Misc(bot))
        print("adding cog")


def teardown(bot):
    bot.remove_cog("misc")
    print("removing cog")
