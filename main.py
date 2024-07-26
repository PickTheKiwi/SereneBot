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


def start_bot():
    bot.run(TOKEN)


start_bot()
