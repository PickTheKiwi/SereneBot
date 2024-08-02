import disnake
from disnake.embeds import Embed
from disnake.ext import commands
from typing import Union

ENABLED = True


class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("User cog loaded")

    @commands.slash_command()
    async def user(self, ctx):
        pass


def setup(bot):
    if ENABLED:
        bot.add_cog(User(bot))
        print("adding cog")


def teardown(bot):
    bot.remove_cog("misc")
    print("removing cog")
