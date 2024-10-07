import disnake
from disnake.embeds import Embed
from disnake.ext import commands

import sqlite3

ENABLED = True


class ExpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("ExpCommand cog loaded")

    @commands.slash_command()
    async def rank(self, context):
        pass

    @rank.sub_command()
    async def check(self, context, user: disnake.User):
        """
        Fetch user xp from the database and respond with required information
        """
        await context.response.defer()
        conn = sqlite3.connect("Serene.db")
        cur = conn.cursor()
        cur.execute(f"SELECT user_xp FROM user WHERE user_id IS {context.author.id}")
        user_xp = cur.fetchone()
        if user_xp is None:
            embed = Embed(
                title="Level",
                description=f"User {context.author.mention} does not exist.",
                color=0x010101,
            )
        else:
            user_xp = user_xp[0]
            embed = Embed(
                title="Level",
                description=f"User {context.author.mention} has {user_xp} xp",
                color=0xFFFF00,
            )
        # Edit defer message
        await context.edit_original_message(embed=embed)

    @rank.sub_command()
    @commands.is_owner()  # This came to mind quickly I'll change it to admin later
    async def add_xp(self, context, xp: int):
        await context.response.defer()
        conn = sqlite3.connect("Serene.db")
        cur = conn.cursor()
        cur.execute(f"SELECT user_xp FROM user WHERE user_id IS {context.author.id}")
        user_xp = cur.fetchone()
        embed = None
        if user_xp is None:
            embed = Embed(
                title="Add XP",
                description=f"User {context.author.mention} does not exist.",
                color=0x010101,
            )
        else:
            user_xp = user_xp[0]
            user_xp += xp
            cur.execute(
                f"UPDATE user SET userxp = {user_xp} WHERE user_id IS {context.author.id}"
            )
            conn.commit()
            embed = Embed(
                title="Add XP",
                description=f"User {context.author.mention} has {user_xp} xp",
                color=0x00FF00,
            )
        await context.edit_original_message(embed=embed)


def setup(bot):
    if ENABLED:
        bot.add_cog(ExpCommand(bot))
        print("adding cog")


def teardown(bot):
    bot.remove_cog("exp_command")
    print("removing cog")
