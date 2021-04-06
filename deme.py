import discord
import os
import random

from discord.ext import commands
from dotenv import load_dotenv
from googlesearch import search

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


@bot.command(name="clean", help="Responds with a random cleaning tasks.")
async def cleandex(ctx):
    """
    Handles the command to request to a suggestion for cleaning.
    """

    tasks = [
        "Have you put clean dishes away today?",
        "Have you swept today?",
        "Have you taken out the trash today?",
        "Have you washed a load of dishes today?",
        "Have you wiped the kitchen sink out today?",
        "Have you cleaned the floors this week?",
        "Have you cleaned the mirror(s) this week?",
        "Have you dusted your shelves this week?"
        "Have you cleaned the vents this month?",
        "Have you organized your dresser drawers this month?",
        "Have you scrubbed the shower grout this month?",
        "Have you vacuumed your car this month?"
    ]

    response = random.choice(tasks)
    await ctx.send(response)
    

@bot.command(name="create-channel")
@commands.has_role("admin")
async def create_channel(ctx, channel_name="test-channel"):
    """
    Handles the command to create a new text channel, as long as the user is an administrator.
    """

    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)


@bot.command(name="game", help="Responds with a random game suggestion.")
async def gamedex(ctx):
    """
    Handles the command to request to a game suggestion.
    """

    games = [
        "Game: INSIDE, Class: S (16), Console: Any",
        "Game: The Legend of Zelda: Breath of the Wild, Class: B (11.5), Console: Switch",
        "Game: Red Dead Redemption 2, Class: B (10), Console: PS4"
    ]

    response = random.choice(games)
    await ctx.send(response)


@bot.listen("on_message")
async def google(message):
    """
    Handles what happens when a user wants to conduct a google search.
    """

    if message.author == bot.user:
        return

    if message.content.startswith("hey deme google"):
        searchContent = ""
        text = str(message.content).split(" ")
        for i in range(2, len(text)):
            searchContent = searchContent + text[i]

        for j in search(searchContent, tld="co.in", num=1, stop=1, pause=2):
            await message.channel.send(j)


@bot.event
async def on_command_error(ctx, error):
    """
    Handles what happens when a command is used by a user without permission.
    """

    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send("You do not have the correct role for this command.")


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
