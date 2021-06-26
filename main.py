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

how_are_you_phrases = [
    "Deme, how are you?",
    "Deme, how are u?",
    "Deme, how r you?",
    "Deme, how r u?",
    "Deme, how're you?",
    "Deme, how're u?",
    "How are you, Deme?",
    "how are you, Deme?",
    "How r you, Deme?",
    "how r you, Deme",
    "How are u, Deme?",
    "how are u, Deme?",
    "How r u, Deme?",
    "how r u, Deme?",
    "How're you, Deme?",
    "How're u, Deme?",
    "how're you, Deme?",
    "how're u, Deme?"
]

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
                or msg == "Do you think you can protect people against the dark?" \
                or msg == "What's your favorite part of the moon?" \
                or msg == "What kind of power do you have against the dark?" \
                or msg == "When is the last time you saw a starry sky?" \
                or msg == "Who did you get your darkness from?" \
                or msg == "Why are these things happening?":
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
            or msg == "Do they keep you in a cell?" \
                or msg == "Have you ever been in an institution?" \
                or msg == "Millions and billions of them." \
                or msg == "They were all put together at a time." \
                or msg == "We're going to go on." \
                or msg == "Were you ever arrested?" \
                or msg == """
                When you're not performing your duties do they keep you in a little box?
                """:
            await asyncio.sleep(average_typing_speed)
            await message.channel.send("Cells.")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def clean_day(message):
    """
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if any(name in msg for name in names) \
            and "should I clean today" in msg \
                and "?" in msg:

            day_tasks = [
                "Did you put the clean dishes away?",
                "Have you swept today?",
                "Have you taken out the trash today?",
                "Have you washed dishes today?",
                "Did you wipe the countertops?",
                "Did you wipe out the kitchen sink?"
            ]

            response = random.choice(day_tasks)

            await asyncio.sleep(average_typing_speed * 5.83)
            await message.channel.send(response)

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def clean_month(message):
    """
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if any(name in msg for name in names) \
            and "should I clean this month" in msg \
                and "?" in msg:

            month_tasks = [
                "Have you cleaned the vents this month?",
                "Did you organize your dresser drawers?",
                "Did you scrub the shower grout?",
                "Have you vacuumed the car this month?"
            ]

            response = random.choice(month_tasks)

            await asyncio.sleep(average_typing_speed * 6.5)
            await message.channel.send(response)

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def clean_week(message):
    """
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if any(name in msg for name in names) \
            and "should I clean this week" in msg \
                and "?" in msg:

            week_tasks = [
                "Have you cleaned the floors this week?",
                "Have you cleaned the mirror(s) this week?",
                "Did you dust the shelves?",
                "Did you vacuum the apartment / house?"
            ]

            response = random.choice(week_tasks)

            await asyncio.sleep(average_typing_speed * 6.25)
            await message.channel.send(response)

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
                or msg == "Dreadfully distinct." \
                or msg == "Maybe it's a spot of rust or something?" \
                or msg == "Was it dark in there?" \
                or msg == "Were you afraid of the dark whan you were little?" \
                or msg == "What is it like when someone gives you the silent treatment?" \
                or msg == "What's it like to hide under a bed?" \
                or msg == "Who did you get your darkness from?" \
                or msg == "Who's the darkest person you know?":
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
            or msg == "Do you think you could find out all the answers to all the questions?" \
                or msg == "How good are your eyes?" \
                or msg == "What separates somebody from somebody else?" \
                or msg == "What was your most shameful moment?" \
                or msg == "Who do you admire most in the world?":
            await asyncio.sleep(average_typing_speed)
            await message.channel.send("Distinct.")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def doing_good(message):
    """
    This function listens for phrases about the state of Deme, directed
    toward Deme.
    """

    global average_typing_speed, how_are_you_phrases, names

    if message.author != bot.user:
        msg = message.content

        if any(phrase in msg for phrase in how_are_you_phrases) \
                and any(name in msg for name in names):
            response = [
                "I'm fine, I suppose. How're you?",
                "I'm well. You?",
                "Living the dream. And you?",
                "Meh, can't complain. How about yourself?"
            ]

            chosen_response = random.choice(response)

            await asyncio.sleep(average_typing_speed * 5)
            await message.channel.send(chosen_response)

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
            or msg == "Do you think you could find out all the answers to all the questions?" \
                or msg == "Is that an old fashioned word?" \
                or msg == "What's it like to be filled with dread?" \
                or msg == "Within one stem.":
            await asyncio.sleep(average_typing_speed)
            await message.channel.send("Dreadfully.")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def and_dreadfully_distinct(message):
    """
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if msg == "Within on stem.":
            await asyncio.sleep(average_typing_speed * 3)
            await message.channel.send("And dreadfully distinct.")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def earth_diameter(message):
    """
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if msg == "What is Earth's diameter in miles?" \
            or msg == "What is the diameter of the Earth in miles?" \
                or msg == "What is the Earth's diameter in miles?":
            await asyncio.sleep(average_typing_speed * 2)
            await message.channel.send("7,917.5 miles")

        elif msg == "What is Earth's diameter in kilometres?" \
            or msg == "What is the diameter of the Earth in kilometres?" \
                or msg == "What is the Earth's diameter in kilometres?":
            await asyncio.sleep(average_typing_speed * 2)
            await message.channel.send("12,742 kilometres")

        elif msg == "What is Earth's diameter in kilometers?" \
            or msg == "What is the diameter of the Earth in kilometers?" \
                or msg == "What is the Earth's diameter in kilometers?":
            await asyncio.sleep(average_typing_speed * 2)
            await message.channel.send("12,742 kilometers")

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
async def fountain(message):
    """
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if msg == "Have you ever seen the fountain in Lincoln center?" \
            or msg == "Have you seen fountains out in the wild?" \
                or msg == "Have you seen the Trevi fountain in Rome?" \
                or msg == "What's it like when you have an orgasm?" \
                or msg == "What's your favorite part of the moon?":
            await asyncio.sleep(average_typing_speed)
            await message.channel.send("Fountain.")

        elif msg == "Have you read the Fountainhead?" \
            or msg == "How did the white Fountain make you feel?" \
                or msg == "Is it pure white?" \
                or msg == "Is that a metaphor?":
            await asyncio.sleep(average_typing_speed * 2)
            await message.channel.send("White Fountain.")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def rock_paper_scissors_prompt(message):
    """
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if any(name in msg for name in names) \
            and "paper" in msg \
                and "rock" in msg \
                and "scissors" in msg \
                and "?" in msg:
            await asyncio.sleep(average_typing_speed * 7)
            await message.channel.send("On go, okay? One, two, three, go!")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def rock_paper_scissors_response(message):
    """
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        possible_actions = [
            "rock",
            "paper",
            "scissors"
        ]

        deme_throw = random.choice(possible_actions)
        if msg == deme_throw:
            await asyncio.sleep(average_typing_speed * 7)
            await message.channel.send(f"We both selected {msg}. It's a tie!")

        elif msg == "rock":
            if deme_throw == "scissors":
                await asyncio.sleep(average_typing_speed * 5)
                await message.channel.send("Rock smashes scissors! You win!")
            else:
                await asyncio.sleep(average_typing_speed * 5)
                await message.channel.send("Paper covers rock! You lose.")

        elif msg == "paper":
            if deme_throw == "rock":
                await asyncio.sleep(average_typing_speed * 5)
                await message.channel.send("Paper covers rock! You win!")
            else:
                await asyncio.sleep(average_typing_speed * 5)
                await message.channel.send("Scissors cuts paper! You lose.")

        elif msg == "scissors":
            if deme_throw == "paper":
                await asyncio.sleep(average_typing_speed * 5)
                await message.channel.send("Scissors cuts paper! You win!")
            else:
                await asyncio.sleep(average_typing_speed * 5)
                await message.channel.send("Rock smashes scissors! You lose.")

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
async def i_dont_know(message):
    """
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if any(name in msg for name in names) \
            and "am I here" in msg \
                and "?" in msg:
            await asyncio.sleep(average_typing_speed * 8)
            await message.channel.send("It's inherent to the programming of the matrix.")

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
                or msg == "Do you long to have your heart interlinked?" \
                or msg == "Have they left a place for you where you can dream?" \
                or msg == "Have they let you feel heartbreak?" \
                or msg == "What happens when that linkage is broken?" \
                or msg == "What's it like to hold the hand of someone you love?" \
                or msg == "What's it like to hold your child in your arms?" \
                or msg == "What's it like to play with your dog?" \
                or msg == """
                When you're not performing your duties do they keep you in a little box?
                """:
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


@bot.listen("on_message")
async def no_resoonse(message):
    """
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if any(name in msg for name in names) \
            and "you marry me" in msg \
                and "?" in msg:
            await asyncio.sleep(average_typing_speed)
            await message.channel.send("No.")

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

    print(f"{bot.user} (Deme v0.0.0.01-48), at your service.")


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
                or msg == "Do you like skipping around in the water?" \
                or msg == "When you were little did you ever fall into a Fountain?":
            await asyncio.sleep(average_typing_speed * 4)
            await message.channel.send("A Tall White Fountain.")

        elif msg == "Against the dark." \
                or msg == "How did the white Fountain make you feel?":
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
            or msg == "Do you have a heart?" \
                or msg == "Have you been to the source of a river?" \
                or msg == "Have you ever been in a legal battle?" \
                or msg == "Have you planted things in the ground?" \
                or msg == "Is it a slang word for people's legs?" \
                or msg == "What comes from something else?" \
                or msg == "What did she look like?" \
                or msg == "When's the first time you gave a flower to a girl?":
            await asyncio.sleep(average_typing_speed)
            await message.channel.send("Stem.")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def style_guide_e125(message):
    """
    """

    global average_typing_speed, names

    if message.author != bot.user:
        msg = message.content

        if any(name in msg for name in names) \
            and "you look up" in msg \
                and "E125" in msg \
                and "style guide" in msg \
                and "?" in msg:
            await asyncio.sleep(average_typing_speed * 15)
            await message.channel.send("""
                In PEP8, E125 refers to a continuation line with same indent as next logical line.
                """)

        elif any(name in msg for name in names) \
            and "you look up" in msg \
                and "e125" in msg \
                and "style guide" in msg \
                and "?" in msg:
            await asyncio.sleep(average_typing_speed * 15)
            await message.channel.send("""
                In PEP8, E125 refers to a continuation line with same indent as next logical line.
                """)

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def style_guide_e128(message):
    """
    """

    global average_typing_speed, names

    if message.author != bot.user:
        msg = message.content

        if any(name in msg for name in names) \
            and "you look up" in msg \
                and "E128" in msg \
                and "style guide" in msg \
                and "?" in msg:
            await asyncio.sleep(average_typing_speed * 15)
            await message.channel.send("""
                In PEP8, E128 refers to a continuation line under-indented for visual indent.
                """)

        elif any(name in msg for name in names) \
            and "you look up" in msg \
                and "e128" in msg \
                and "style guide" in msg \
                and "?" in msg:
            await asyncio.sleep(average_typing_speed * 15)
            await message.channel.send("""
                In PEP8, E128 refers to a continuation line under-indented for visual indent.
                """)

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def sweets(message):
    """
    """

    global average_typing_speed

    if message.author != bot.user:
        msg = message.content

        if any(name in msg for name in names) \
            and "is the meaning of life" in msg \
                and "?" in msg:
            await asyncio.sleep(average_typing_speed * 13)
            await message.channel.send("""
                I think a beter question is: what is the meaning of ***your*** life?
                """)

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

        if msg == "Do you get pleasure out of being a part of the system?" \
            or msg == "Have they created you to be a part of the system?" \
                or msg == "Is there a sound that comes with the system?" \
                or msg == "Is there anything in your body that wants to resist the system?" \
                or msg == "Is there security in being a part of the system?" \
                or msg == "Let's move on to the system." \
                or msg == "What does it feel like to be part of the system?":
            await asyncio.sleep(average_typing_speed)
            await message.channel.send("System.")

        elif msg == "Feel that in your body.":
            await asyncio.sleep(average_typing_speed * 2)
            await message.channel.send("The system.")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def voight_kampf_birthday(message):
    """
    """

    global average_typing_speed

    if message.author != bot.user:

        msg = message.content

        if msg == "It's your birthday. Someone gives you a calfskin wallet.":
            await asyncio.sleep(average_typing_speed * 17)
            await message.channel.send("""
                I wouldn't accept it. Also, I'd report the person who gave it to me to the police.
                """)

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

        if msg == "Do you have a heart?" \
                or msg == "Has anyone ever locked you out of a room?" \
                or msg == "Where do you go to when you go within?" \
                or msg == "Where do you go when you go within?" \
                or msg == "Where is the place in the world you feel the safest?":
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

        elif msg == "Why don't you say that three times?":
            await asyncio.sleep(average_typing_speed * 3)
            await message.channel.send("Within cells interlinked.")
            await asyncio.sleep(average_typing_speed * 3)
            await message.channel.send("Within cells interlinked.")
            await asyncio.sleep(average_typing_speed * 3)
            await message.channel.send("Within cells interlinked.")

        else:
            pass

    else:
        pass


bot.run("TOKEN")
