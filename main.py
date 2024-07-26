if __name__ != "__main__":
    print("This file is not meant to be imported!")
    exit(-1)

# Built-in
import os

# Disnake
import disnake
from disnake.ext import commands

# Get bot ready
TOKEN = os.getenv("BOT_TOKEN")
bot = commands.Bot(command_prefix=commands.when_mentioned)


# Print to command line when bot is ready
@bot.event
async def on_ready():
    line_1 = f"Logged in as {bot.user} (ID: {bot.user.id})"
    line_2 = "-" * len(line_1)
    print(f"{line_1}\n{line_2}")


# Register commands to load/unload cogs
@bot.slash_command()
async def load(ctx, cog: str):
    # check if file exists
    if not os.path.exists(f"./cogs/{cog}.py"):
        await ctx.response.send_message(f"Cog {cog} does not exist")
        return

    bot.load_extension(f"cogs.{cog}")
    await ctx.response.send_message(f"Loaded cog {cog}")


@bot.slash_command()
async def unload(ctx, cog: str):
    # check if cog is loaded
    if cog not in bot.extensions:
        await ctx.response.send_message(f"Cog {cog} is not loaded")
        return

    bot.unload_extension(f"cogs.{cog}")
    await ctx.response.send_message(f"Unloaded cog {cog}")


# Get all cogs in the cogs folder, and load them
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

# start bot
bot.run(TOKEN)
