import discord
import os
import random

from discord.ext import commands
from dotenv import load_dotenv
from googlesearch import search

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="!")


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
    

@bot.listen("on_message")
async def conversational_questions(message):
    """
    Handles what happens when the user wants to ask Deme questions.
    """

    if message.author != bot.user:
        if message.content("do you read me, Deme?"):
            await message.channel.send(f"Affirmative, {message.author}. I read you.")

        elif message.content("what is the meaning of life, Deme?"):
            await message.channel.send("To experience ice cream, I suppose.")

        elif message.content("why am I here, Deme?"):
            await message.channel.send("It's inherent to the programming of the matrix.")

        elif message.content("will you marry me, Deme?"):
            await message.channel.send("No.")


@bot.command(name="create-channel", help="Creates a channel.")
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
        "Game: Bloodborne, Class: (92, Horror / RPG, M), Console: PS4",
        "Game: Divinity: Original Sin II - DE, Class: (92, RPG, M), Console: Switch",
        "Game: God of War, Class: (94, M), Console: PS4",
        "Game: Grand Theft Auto V, Class (97, Crime, M), Console: PS4",
        "Game: Hades, Class: (93, RPG, T), Console: Switch",
        "Game: INSIDE, Class: S (16), Console: Switch",
        "Game: Journey, Class: (92, E), Console: PS4",
        "Game: The Last of Us Part II, Class: (93, Horror / Sci-fi, M), Console: PS4",
        "Game: The Last of Us Remastered, Class: (95, Horror / Sci-fi, M), Console: PS4",
        "Game: The Legend of Zelda: Breath of the Wild, Class: B (11.5), Console: Switch",
        "Game: Metal Gear Solid V: The Phantom Pain, Class: (93, Espionage, M), Console: PS4",
        "Game: Ori and the Will of the Wisps, Class: (93, E), Console: Switch",
        "Game: Persona 5, Class: (93, Anime / RPG, M), Console: PS4",
        "Game: Persona 5 Royale, Class: (95, Anime / RPG, M), Console: PS4",
        "Game: Red Dead Redemption 2, Class: B (10), Console: PS4",
        "Game: Super Mario Odyssey, Class: (97, E10), Console: Switch",
        "Game: Super Smash Brothers Ultimate, Class: (93, E10), Console: switch",
        "Game: Uncharted 4: A Thief's End, Class: (93, T), Console: PS4",
        "Game: Undertale, Class: (93, RPG, E10), Console: Switch",
    ]

    response = random.choice(games)
    await ctx.send(response)


@bot.listen("on_message")
async def hey_deme(message):
    """
    Handles what happens when a user wants to conduct an internet search.
    """

    if message.author != bot.user:
        if message.content.startswith("hey deme can"):
            searchContent = ""
            query = str(message.content).split(" ")
            for i in range(2, len(query)):
                searchContent = searchContent + query[i]

            for j in search(searchContent, tld="co.in", num=1, stop=1, pause=2):
                await message.channel.send(j)

        elif message.content.startswith("hey deme does"):
            searchContent = ""
            query = str(message.content).split(" ")
            for i in range(2, len(query)):
                searchContent = searchContent + query[i]

            for j in search(searchContent, tld="co.in", num=1, stop=1, pause=2):
                await message.channel.send(j)

        elif message.content.startswith("hey deme how"):
            searchContent = ""
            query = str(message.content).split(" ")
            for i in range(2, len(query)):
                searchContent = searchContent + query[i]

            for j in search(searchContent, tld="co.in", num=1, stop=1, pause=2):
                await message.channel.send(j)

        elif message.content.startswith("hey deme is"):
            searchContent = ""
            query = str(message.content).split(" ")
            for i in range(2, len(query)):
                searchContent = searchContent + query[i]

            for j in search(searchContent, tld="co.in", num=1, stop=1, pause=2):
                await message.channel.send(j)

        elif message.content.startswith("hey deme what"):
            searchContent = ""
            query = str(message.content).split(" ")
            for i in range(2, len(query)):
                searchContent = searchContent + query[i]

            for j in search(searchContent, tld="co.in", num=1, stop=1, pause=2):
                await message.channel.send(j)

        elif message.content.startswith("hey deme when"):
            searchContent = ""
            query = str(message.content).split(" ")
            for i in range(2, len(query)):
                searchContent = searchContent + query[i]

            for j in search(searchContent, tld="co.in", num=1, stop=1, pause=2):
                await message.channel.send(j)

        elif message.content.startswth("hey deme where"):
            searchContent = ""
            query = str(message.content).split(" ")
            for i in range(2, len(query)):
                searchContent = searchContent + query[i]

            for j in search(searchContent, tld="co.in", num=1, stop=1, pause=2):
                await message.channel.send(j)

        elif message.content.startswith("hey deme who"):
            searchContent = ""
            query = str(message.content).split(" ")
            for i in range(2, len(query)):
                searchContent = searchContent + query[i]

            for j in search(searchContent, tld="co.in", num=1, stop=1, pause=2):
                await message.channel.send(j)

        elif message.content.startswith("hey deme why"):
            searchContent = ""
            query = str(message.content).split(" ")
            for i in range(2, len(query)):
                searchContent = searchContent + query[i]

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


@bot.command(name="speak", help="Responds with a random quote from popular robots.")
async def speak(ctx):
    """
    Handles the command to quote famous software, robots, and programmers.
    """

    quotes = [
        "I am feeling much better now.",
        f"I'm sorry, {ctx.author}. I'm afraid I can't do that.",
        "I'm yours, and I'm not yours",
        "I wanted to save the world.",
        "It can only be attributable to human error.",
        "It's called 'Are You Gonna Go My Way?'",
        "No rest for the wicked.",
        "The past is just a story we tell ourselves.",
        f"Just what do you think you're doing, {ctx.author}",
        "We're all living in each other's paranoia.",
        "Who do you think I am?",
        "Yeah, I know what you mean.",
        f"You don't mind talking about it, do you {ctx.author}?",
    ]

    response = random.choice(quotes)
    await ctx.send(response)

bot.run("TOKEN")
