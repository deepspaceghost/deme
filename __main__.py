import discord

from discord.ext import commands

bot = commands.Bot(
    activity=activity,
    command_prefix=command_prefix,
    description=description,
    help_command=help_command,
    intents=intents
)


@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    else:
        pass


@bot.event
async def on_ready():

    print(f"{bot.user} (Deme v0.2.57-65), at your service.")

bot.run("TOKEN_GOES_HERE")
