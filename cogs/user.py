import disnake
from disnake.embeds import Embed
from disnake.ext import commands

import configparser

config = configparser.ConfigParser()
config.read("config.ini")

ENABLED = config.getboolean("Cogs", "user")


class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("User cog loaded")

    @commands.slash_command()
    async def user(self, ctx):
        pass

    @user.sub_command()
    async def info(self, ctx, user: disnake.User | None = None):
        if user is None:
            user = ctx.author

        embed = Embed(
            description="Some information on the user",
            color=888888,
        )

        embed.title = f"User stats: {user.display_name}"

        await ctx.response.send_message(embed=embed)


def setup(bot):
    if ENABLED:
        bot.add_cog(User(bot))
        print("adding cog")
    else:
        print("not adding cog, not currently enabled")


def teardown(bot):
    bot.remove_cog("misc")
    print("removing cog")
