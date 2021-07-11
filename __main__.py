import asyncio
import discord
import logging
import os
import random

from discord.ext import commands

handler = logging.FileHandler(
    encoding="utf-8",
    filename="discord_err.log",
    mode="w"
)

handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, "listening.txt")) as f:
    listening = [item.rstrip("\r\n ") for item in f.readlines() if item != ""]

listening_name = random.choice(listening)

with open(os.path.join(dir_path, "watching.txt")) as f:
    watching = [item.rstrip("\r\n ") for item in f.readlines() if item != ""]

watching_name = random.choice(watching)

with open(os.path.join(dir_path, "playing.txt")) as f:
    playing = [item.rstrip("\r\n ") for item in f.readlines() if item != ""]

playing_name = random.choice(playing)

activities = [
    discord.Activity(
        name=listening_name,
        type=discord.ActivityType.listening),
    discord.Activity(
        name=watching_name,
        type=discord.ActivityType.watching),
    discord.Game(name=playing_name),
]

activity = random.choice(activities)

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
    command_prefix="?",
    description=None,
    help_command=help_command,
    intents=intents
)

average_typing_speed = 0.833

define_verbs = [
    "define",
    "defined",
    "defines",
    "defining"
]

names = [
    "Deme",
    "Demeter",
    "deme",
    "demeter"
]

tooth_nouns = [
    "teeth",
    "tooth"
]

try_verbs = [
    "tried",
    "tries",
    "try",
    "trying"
]

yourself_pronouns = [
    "yourself",
    "yourselves"
]


@bot.listen("on_message")
async def annie_who(message):

    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content

        if "Annie" in mescon and "?" in mescon:

            response = "Annie thing you can do I can do for eighty-seven cents on the dollar."

            await asyncio.sleep(average_typing_speed * 14)
            await meschan.send(response)


@bot.listen("on_message")
async def humor_setting_seven_five(message):

    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content

        # "Humor, seventy-five percent."

        if "seventy-five percent" in mescon or "75%" in mescon:

            await asyncio.sleep(average_typing_speed * 9)
            await meschan.send("Confirmed. Self destruct sequence in T minus ten, nine...")


@bot.listen("on_message")
async def humor_setting_six_zero(message):

    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content

        # "Let's make that sixty percent."

        if "sixty percent" in mescon or "60%" in mescon:

            await asyncio.sleep(average_typing_speed * 3)
            await meschan.send("Confirmed. Knock knock.")


@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    else:
        pass


@bot.event
async def on_ready():

    print(f"{bot.user} (Deme v0.0.1-22), at your service.")  # First benchmark: 539.5 kb


@bot.listen("on_message")
async def pseudo_random_number_generator(message):

    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content

        # "Deme, can I get a random number between 000 and 000?"

        if any(name in mescon for name in names) and "random" in mescon and "?" in mescon:

            minimum_number = int(mescon[40:-8])

            maximum_number = int(mescon[48:-1])

            response = random.randint(minimum_number, maximum_number)

            await asyncio.sleep(average_typing_speed)
            await meschan.send(response)

        else:
            pass


@bot.listen("on_message")
async def who_is_there(message):

    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content

        if "is" in mescon and "?" in mescon or "'s" in mescon and "?" in mescon:

            await asyncio.sleep(average_typing_speed)
            await meschan.send("Annie.")


@bot.listen("on_message")
async def yourself_quote(message):

    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content

        if any(verb in mescon for verb in define_verbs) \
            and "own" in mescon \
            and any(noun in mescon for noun in tooth_nouns) \
            and any(verb in mescon for verb in try_verbs) \
                and any(pronoun in mescon for pronoun in yourself_pronouns):

            quote = """
            Alan Watts once said, 'Trying to define yourself is like trying to bite your own teeth.'
            """

            await asyncio.sleep(average_typing_speed * 12)
            await meschan.send(quote)

bot.run("TOKEN")
