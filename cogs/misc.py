import disnake
from disnake.ext import commands

ENABLED = True


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Misc cog loaded")

    @commands.slash_command()
    async def ping(self, interaction):
        await interaction.response.send_message(f"{round(self.bot.latency * 1000)}ms")


def setup(bot):
    if ENABLED:
        bot.add_cog(Misc(bot))
        print("adding cog")


def teardown(bot):
    bot.remove_cog("misc")
    print("removing cog")
