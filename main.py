import asyncio
import discord
import logging
import random

from discord.ext import commands

handler = logging.FileHandler(
    encoding="utf-8",
    filename="discord_err.log",
    mode="w"
)

handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

games = [
    "Amnesia: A Machine for Pigs",
    "Dear Esther",
    "Everybody's Gone to the Rapture",
    "flOw",
    "Flower",
    "INSIDE",
    "Journey",
    "Limbo",
    "Little Orpheus",
    "Monument Valley",
    "Monument Valley II",
    "Sky",
    "So Let Us Melt"
]

game_name = random.choice(games)

films_and_shows = [
    "The Girl with the Dragon Tattoo",
    "Mr. Robot",
    "Under the Skin"
]

activities = [
    discord.Activity(
        name=random.choice(films_and_shows),
        type=discord.ActivityType.watching),
    discord.Game(name=random.choice(games))
]

activity = random.choice(activities)
command_prefix = "?"
description = None
help_command = commands.DefaultHelpCommand(no_category="Boons")
intents = discord.Intents(
    guilds=True,
    messages=True,
    presences=False,
    reactions=True,
    typing=False
)

bot = commands.Bot(
    activity=activity,
    command_prefix=command_prefix,
    description=description,
    help_command=help_command,
    intents=intents
)

average_typing_speed = 0.833

names = [
    "Deme",
    "deme"
]


@bot.listen("on_message")
async def began_to_spin(message):
    """
    This function listens for the initial phrase of the Baseline Test
    from Blade Runner 2049.
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if msg == "A blood black nothingness began to spin.":
            await asyncio.sleep(average_typing_speed * 3)
            await message.channel.send("Began to spin.")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def affirmative(message):
    """
    """

    global average_typing_speed, names

    if message.author != bot.user:
        msg = message.content

        if any(name in msg for name in names) \
            and "you read me" in msg \
                and "?" in msg:
            await asyncio.sleep(average_typing_speed * 5)
            await message.channel.send(f"Affirmative, {message.author}. I read you.")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def against_the_dark(message):
    """
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if msg == "Do you prefer the day or the night?" \
            or msg == "Do you think there is such a thing as evil?" \
                or msg == "Do you think you can protect people against the dark?":
            await asyncio.sleep(average_typing_speed * 3)
            await message.channel.send("Against the dark.")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def a_blood_black_nothingness(message):
    """
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if msg == "Do you like skipping around in the water?":
            await asyncio.sleep(average_typing_speed * 4)
            await message.channel.send("A blood black nothingness.")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def cells(message):
    """
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if msg == "Did you spend much time in the cell?" \
                or msg == "Do they keep you in a cell?":
            await asyncio.sleep(average_typing_speed)
            await message.channel.send("Cells.")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def dark_response(message):
    """
    This function listens for phrases with the "Dark?" response from
    the Baseline Test from Blade Runner 2049.
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if msg == "Did they keep you in a drawer when they were building you?" \
                or msg == "Did they program you to have dark thoughts?":
            await asyncio.sleep(average_typing_speed)
            await message.channel.send("Dark?")

        elif msg == "Do you have dark thoughts?" \
            or msg == "Do you think it's some kind of corruption these dark thoughts?" \
                or msg == "Dreadfully distinct.":
            await asyncio.sleep(average_typing_speed)
            await message.channel.send("Dark.")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def distinct(message):
    """
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if msg == "Do you have a particular personality?" \
                or msg == "Do you think you could find out all the answers to all the questions?":
            await asyncio.sleep(average_typing_speed)
            await message.channel.send("Distinct.")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def dreadful(message):
    """
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if msg == "Did you ever want to live in the nineteenth century?" \
                or msg == "Do you think you could find out all the answers to all the questions?":
            await asyncio.sleep(average_typing_speed)
            await message.channel.send("Dreadfully.")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def equal_rights(message):
    """
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if any(name in msg for name in names) \
            and "you want anything" in msg \
                and "?" in msg:
            await asyncio.sleep(average_typing_speed * 2)
            await message.channel.send("Equal rights?")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def hmm_response(message):
    """
    This function listens of Deme's name, when asked in the form of a
    question.
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if msg == "Deme?":
            await asyncio.sleep(average_typing_speed)
            await message.channel.send("Hmm?")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def interlinked(message):
    """
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if msg == "Do they teach you how to feel finger to finger?" \
                or msg == "Do you dream about being interlinked?" \
                or msg == "Do you feel that there's a part of you that's missing?" \
                or msg == "Do you like to connect to things?" \
                or msg == "Do you long to have your heart interlinked?":
            await asyncio.sleep(average_typing_speed)
            await message.channel.send("Interlinked.")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def mystery(message):
    """
    This function listens for the initial phrase of the Baseline Test from
    Blade Runner 2049.
    """

    if message.author != bot.user:
        msg = message.content

        if msg == "Could you be any more cryptic?":
            await asyncio.sleep(average_typing_speed * 6)
            await message.channel.send("It's a mystery. You'll love it.")

        else:
            pass

    else:
        pass


@bot.event
async def on_message(message):
    """
    This function checks who sent the message.
    """

    if message.author == bot.user:
        return

    else:
        pass


@bot.event
async def on_ready():
    """
    This function sends a message to the temrinal when Deme has finisshed
    setting up with Discord.
    """

    print(f"{bot.user} (Deme v0.0.0.45-09), at your service.")


@bot.listen("on_message")
async def a_tall_white_fountain(message):
    """
    This function checks for one of the prompts from the Baseline Test from
    Blade Runner 2049.
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if msg == "Do you like fire, earth, air or water?" \
                or msg == "Do you like skipping around in the water?":
            await asyncio.sleep(average_typing_speed * 4)
            await message.channel.send("A Tall White Fountain.")

        elif msg == "Against the dark.":
            await asyncio.sleep(average_typing_speed * 5)
            await message.channel.send("A tall white fountain played.")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def stem(message):
    """
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if msg == "Did you pick asparagus stems?" \
                or msg == "Do you have a heart?":
            await asyncio.sleep(average_typing_speed)
            await message.channel.send("Stem.")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def system(message):
    """
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if msg == "Do you get pleasure out of being a part of the system?":
            await asyncio.sleep(average_typing_speed)
            await message.channel.send("System.")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def within(message):
    """
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if msg == "Do you have a heart?":
            await asyncio.sleep(average_typing_speed)
            await message.channel.send("Within.")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def within_cells_interlinked(message):
    """
    This function checks for one of the prompts from the Baseline Test from
    Blade Runner 2049.
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if msg == "A system of cells." \
                or msg == "Did you buy a present for the person you love?":
            await asyncio.sleep(average_typing_speed * 3)
            await message.channel.send("Within cells interlinked.")

        else:
            pass

    else:
        pass


bot.run("TOKEN")
