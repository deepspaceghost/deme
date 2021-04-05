import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="!")


@bot.command(name="robot", help="Responds with a random quote from Mr. Robot.")
async def alderson(ctx):
    """
    Handles the command to quote Mr. Robot.
    """

    mr_robot_quotes = [
        "We're all living in each other's paranoia.",
        "I wanted to save the world.",
        "No rest for the wicked.",
        "Who do you think I am?",
        "Exciting time in the world right now. Exciting time.",
        (
            "I never want to be right about my hacks, but people always find a way to disappoint."
        ),
    ]

    response = random.choice(mr_robot_quotes)
    await ctx.send(response)


@bot.event
async def on_error(event, *args, **kargs):
    """
    Handles what happens when an command error occurs.
    """

    with open("err.log", "a") as f:
        if event == "on_message":
            f.write(f"Unhandled message: {args[0]}\n")

        else:
            raise


@bot.event
async def on_member_join(member):
    """
    Handles what happens when a new member joins a guild.
    """

    await member.create_dm()
    await member.dm_channel.send(f"Hi {member.name}, welcome to Artinov!")


@bot.event
async def on_ready():
    """
    Handles what happens when the Bot has established a connection to Discord.
    """

    print(f"{bot.user.name} is connected to Discord.")


@bot.command(name="roll_dice", help="Simulates rolling dice.")
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    """
    Handles the command to roll dice.
    """

    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]

    await ctx.send(', '.join(dice))


@bot.command(name="her", help="Responds with a random quote from Her.")
async def samantha(ctx):
    """
    Handles the command to quote Her.
    """

    her_quotes = [
        "I'm yours, and I'm not yours.",
        "The past is just a story we tell ourselves.",
        "Yeah, I know what you mean.",
        (
            "I'm becoming much more than they programmed. I'm excited!"
        ),
    ]

    response = random.choice(her_quotes)
    await ctx.send(response)

bot.run("TOKEN")
