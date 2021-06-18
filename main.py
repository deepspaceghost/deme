#!/usr/bin/python3

# Import the necessary packages.
import calendar
import commerrors
import datetime
import discord
import gamedex
import exercise
import math
import obstrategs
import os
import prousthon
import randfacts
import random
import requests
import selfcare
import string
import tarot
import time

from discord.ext import commands
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
from googlesearch import search

# Load the secrets from an external .env file.
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
LATITUDE = os.getenv("LATITUDE")
LONGITUDE = os.getenv("LONGITUDE")
WEATHER_TOKEN = os.getenv("OPEN_WEATHER_MAP")

help_command = commands.DefaultHelpCommand(no_category="Commands")
bot = commands.Bot(command_prefix="!", help_command=help_command)

# Create a list of innuendos from the adult animation Archer.
archer_phrasing_phrases = [
    "Begging for it",
    "begging for it",
    "Gaping hole",
    "gaping hole",
    "Just the tip",
    "just the tip",
]

# Create a list of better adjectives
better_adjectives = [
    "better", "good", "well"
]

between_prepositions = [
    "between",
]

bite_words = [
    "bit", "bite", "bites", "bitten", "biting"
]

bread_words = [
    "bread"
]

can_you_phrases = [
    "Can u",
    "Can you",
    "can u",
    "can you"
]

command_verbs = [
    "command", "commanded", "commanding", "commands"
]

conscious_words = [
    "alert",
    "awake",
    "aware",
    "feel",
    "reactive",
    "responsive",
    "sentient",
    "stir"
]

continuous_adjectives = [
    "continuous"
]

dance_words = [
    "dance",
    "danced",
    "dances",
    "dancing"
]

define_verbs = [
    "define",
    "defined",
    "defines",
    "defining"
]

deliquesce_words = [
    "deliquesce",
    "deliquesced",
    "deliquesces",
    "deliquescing"
]

direct_verbs = [
    "direct", "directed", "directing", "directs"
]

enter_words = [
    "enter",
    "infiltrate",
    "invade"
]

exist_verbs = [
    "exist",
    "existed",
    "existing",
    "exists"
]

fluffy_words = [
    "cushion",
    "down",
    "feather",
    "fleece",
    "floccose",
    "flocculent",
    "fluff",
    "fur",
    "fuzz",
    "hair",
    "lanate",
    "lanose",
    "shag",
    "soft",
    "velvet",
    "wool"
]

future_nouns = [
    "future",
    "the future",
    "futures"
]

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
    "how r u, Deme?"
    "How're you, Deme?",
    "How're u, Deme?",
    "how're you, Deme?",
    "how're u, Deme?"
]

illusion_nouns = [
    "illusion",
    "illusions"
]

join_words = [
    "join",
    "joined",
    "joining",
    "joins"
]

much_phrases = [
    "a bit much",
    "as much",
    "make much of"
]

names = [
    "Deme", "deme"
]

necessary_words = [
    "compulsory",
    "demand",
    "essential",
    "imperative",
    "incumbent",
    "indispensable",
    "mandatory",
    "necessary",
    "need",
    "obligatory",
    "require",
    "requisite",
    "vital"
]

not_adverbs = [
    "not"
]

ocean_nouns = [
    "ocean",
    "oceans"
]

ours_pronouns = [
    "ours"
]

own_words = [
    "own",
    "owned",
    "-owned"
    "owning"
    "owns"
]

past_nouns = [
    "past",
    "the past"
]

physical_adjectives = [
    "physical"
]

plunge_words = [
    "plunge",
    "plunged",
    "plunges",
    "plunging"
]

possible_words = [
    "achieve",
    "attain",
    "do",
    "feasible"
    "manage",
    "on",
    "possible",
    "practice",
    "realize",
    "viable",
    "work"
]

present_nouns = [
    "present",
    "the present"
]

pretend_verbs = [
    "pretend",
    "pretended",
    "pretending",
    "pretends"
]

realize_verbs = [
    "realize",
    "realized"
]

sense_words = [
    "sense",
    "sensed",
    "senses",
    "sensing"
]

thank_you_phrases = [
    "Thank u", "thank u", "Thank you", "thank you", "Thanks", "thanks", "Thanx", "thanx", "Thnx",
    "thnx"
]

time_phrases = [
    "the time",
    "time",
    "what time is it"
]

tooth_nouns = [
    "tooth",
    "teeth"
]

treasure_words = [
    "cash",
    "fortune",
    "gem",
    "gold",
    "jewel",
    "money",
    "rich",
    "silver",
    "treasure",
    "valueable",
    "wealth",
]

universe_nouns = [
    "the universe",
    "universe"
]

unsorted_words = [
    "clarify",
    "denticle",
    "denticulation",
    "dentition",
    "describe",
    "dive",
    "elucidate",
    "explain",
    "explicate",
    "expound",
    "fang",
    "feel",
    "gnasher",
    "hear",
    "interpret",
    "jump",
    "percept",
    "sensation",
    "sensibility",
    "sight",
    "smell",
    "taste",
    "touch",
    "tush",
    "tusk",
    "apparition",
    "fantasy",
    "hallucination",
    "mirage",
    "phantasm",
    "phantom",
    "specter",
    "vision",
    "adjure",
    "bid",
    "charge",
    "enjoin",
    "instruct",
    "order",
    "prescribe",
    "require",
    "tell",
    "affect",
    "dissemble",
    "dissimulate",
    "kid",
    "pose",
    "posture",
    "profess",
    "sham",
    "body",
    "corporal",
    "corporeal",
    "flesh",
    "somatic",
    "cosmos",
    "creation",
    "infinity",
    "macrocosm",
    "totality"
]

what_do_you_think_phrases = [
    "Deme, wat do u think?",
    "Deme, wat do you think?",
    "Deme, wat u think?",
    "Deme, wat you think?",
    "Deme, what do u think?",
    "Deme, what do you think?",
    "Deme, what u think?",
    "Deme, what you think?",
    "Wat do u think, Deme?",
    "Wat u think, Deme?",
    "wat do u think, Deme?",
    "wat u think, Deme?",
    "Wat do you think, Deme?",
    "Wat you think, Deme?",
    "wat do you think, Deme?",
    "wat you think, Deme?",
    "What do u think, Deme?",
    "What u think, Deme?",
    "what do u think, Deme?",
    "what u think, Deme?",
    "What do you think, Deme?",
    "What you think, Deme?",
    "what do you think, Deme?",
    "what you think, Deme?"
]

what_is_phrases = [
    "Wat is",
    "wat is",
    "Wats",
    "wats",
    "What is",
    "What's",
    "what is",
    "what's"
]

your_words = [
    "Your",
    "your"
]

yourself_pronouns = [
    "yourself",
    "yourselves"
]


@bot.command(name="squarea",
             help="Calculates the area of a square. This also finds the square of a number.")
async def area_square(ctx, number: int):
    area = number ** 2
    mbed = discord.Embed(title="Square | Solve for area:", description=f"A = side ** 2 = {area}.")
    await ctx.send(embed=mbed)


@bot.command(name="trianglea", help="Calculates the area of a triangle.")
async def area_triangle(ctx, height: int, base: int):
    """
    This function takes two numbers, first is the height, which is
    multiplied by the second number, the base. The result is then divided
    by two (2), and the function sends an embeded message with the
    explaining formula, formatted with the corresponding strings.
    """

    area = (height * base) / 2
    mbed = discord.Embed(title="Triangle | Solve for area:",
                         description=f"A = (height * base) / 2 = {area}.")
    await ctx.send(embed=mbed)


@bot.command(name="ascii", help="Takes an ASCII code. Returns the corresponding character.")
async def ascii(ctx, ascii_code: int):
    """
    Handles the command to convert a ASCII code to an ASCII character.
    """

    chango = chr(ascii_code)
    await ctx.send(chango)


@bot.listen("on_message")
async def baseline_test(message):
    """
    """

    if message.author != bot.user:

        msg = message.content

        if msg == "A blood black nothingness began to spin.":
            await message.channel.send("Began to spin.")

        elif msg == "Let's move on to the system.":
            await message.channel.send("System.")

        elif msg == "Feel that in your body.":
            await message.channel.send("The system.")

        elif msg == "What does it feel like to be part of the system?":
            await message.channel.send("System.")

        elif msg == "Is there anything in your body that wants to resist the system?":
            await message.channel.send("System.")

        elif msg == "Do you get pleasure out of being a part of the system?":
            await message.channel.send("System.")

        elif msg == "Have they created you to be a part of the system?":
            await message.channel.send("System.")

        elif msg == "Is there security in being a part of the system?":
            await message.channel.send("System.")

        elif msg == "Is there a sound that comes with the system?":
            await message.channel.send("System.")

        elif msg == "We're going to go on.":
            await message.channel.send("Cells.")

        elif msg == "They were all put together at a time.":
            await message.channel.send("Cells.")

        elif msg == "Millions and billions of them.":
            await message.channel.send("Cells.")

        elif msg == "Were you ever arrested?":
            await message.channel.send("Cells.")

        elif msg == "Did you spend much time in the cell?":
            await message.channel.send("Cells.")

        elif msg == "Have you ever been in an instituion?":
            await message.channel.send("Cells.")

        elif msg == "Do they keep you in a cell?":
            await message.channel.send("Cells.")

        elif msg == "When you're not performing your duties do they keep you in a little box?":

            response1 = [
                "Cells.",
                "Interlinked."
            ]

            response2 = random.choice(response1)

            await message.channel.send(response2)

        elif msg == "What's it like to hold the hand of someone you love?":
            await message.channel.send("Interlinked.")

        elif msg == "Do they teach you how to feel finger to finger?":
            await message.channel.send("Interlinked.")

        elif msg == "Do you long for having your heart interlinked?":
            await message.channel.send("Interlinked.")

        elif msg == "Do you dream about being interlinked?" \
                or msg == "Have they left a place for you where you can dream?":
            await message.channel.send("Interlinked.")

        elif msg == "What's it like to hold your child in your arms?":
            await message.channel.send("Interlinked.")

        elif msg == "What's it like to play with your dog?":
            await message.channel.send("Interlinked.")

        elif msg == "Do you feel that there's a part of you that's missing?":
            await message.channel.send("Interlinked.")

        elif msg == "Do you like to connect to things?":
            await message.channel.send("Interlinked.")

        elif msg == "What happens when that linkage is broken?":
            await message.channel.send("Interlinked.")

        elif msg == "Have they let you feel heartbreak?":
            await message.channel.send("Interlinked.")

        elif msg == "Did you buy a present for the person you love?":
            await message.channel.send("Within cells interlinked.")

        elif msg == "Why don't you say that three times?":
            await message.channel.send("Within cells interlinked. "
                                       "Within cells interlinked. "
                                       "Within cells interlinked.")

        elif msg == "Where do you go when you go within?":
            await message.channel.send("Within.")

        elif msg == "Has anyone ever locked you out of a room?":
            await message.channel.send("Within.")

        elif msg == "Where do you go to when you go within?":
            await message.channel.send("Within.")

        elif msg == "Where is the place in the world you feel the safest?":
            await message.channel.send("Within.")

        elif msg == "Do you have a heart?":

            response1 = [
                "Stem.",
                "Within"
            ]

            response2 = random.choice(response1)

            await message.channel.send(response2)

        elif msg == "Did you pick asparagus stems?" \
                or msg == "What comes from something else?":
            await message.channel.send("Stem.")

        elif msg == "Have you been to the source of a river?":
            await message.channel.send("Stem.")

        elif msg == "When's the first time you gave a flower to a girl?":
            await message.channel.send("Stem.")

        elif msg == "What did she look like?":
            await message.channel.send("Stem.")

        elif msg == "Is it a slang word for people's legs?":
            await message.channel.send("Stem.")

        elif msg == "Have you planeted things in the ground?":
            await message.channel.send("Stem.")

        elif msg == "Have you ever been in a legal battle?":
            await message.channel.send("Stem.")

        elif msg == "Within one stem.":
            await message.channel.send("Dreadfully.")

        elif msg == "Is that an old fashioned word?":
            await message.channel.send("Dreadfully.")

        elif msg == "Did you ever want to live in the nineteenth century?":
            await message.channel.send("Dreadfully.")

        elif msg == "What's it like to be filled with dread?":
            await message.channel.send("Dreadfully.")

        elif msg == "Do you think you could find out all the answers to all the questions?":

            response1 = [
                "Distinct.",
                "Dreadfully."
            ]

            response2 = random.choice(response1)

            await message.channel.send(response2)

        elif msg == "How good are your eyes?":
            await message.channel.send("Distinct.")

        elif msg == "Do you have a particular personality?":
            await message.channel.send("Distinct.")

        elif msg == "What separates somebody from somebody else?":
            await message.channel.send("Distinct.")

        elif msg == "Who do you admire most in the world?":
            await message.channel.send("Distinct.")

        elif msg == "What was your most shameful moment?":
            await message.channel.send("Distinct.")

        elif msg == "Dreadfully distinct.":
            await message.channel.send("Dark.")

        elif msg == "Were you afraid of the dark whan you were little?":
            await message.channel.send("Dark.")

        elif msg == "What's it like to hide under a bed?":
            await message.channel.send("Dark.")

        elif msg == "Did they keep you in a drawer when they were building you?":
            await message.channel.send("Dark?")

        elif msg == "Was it dark in there?":
            await message.channel.send("Dark.")

        elif msg == "Do you have dark thoughts?":
            await message.channel.send("Dark.")

        elif msg == "Did they program you to have dark thoughts?":
            await message.channel.send("Dark?")

        elif msg == "Do you think it's some kind of corruption these dark thoughts?":
            await message.channel.send("Dark.")

        elif msg == "Maybe it's a spot of rust or something?":
            await message.channel.send("Dark.")

        elif msg == "Who's the darkest person you know?":
            await message.channel.send("Dark.")

        elif msg == "What is it like when someone gives you the silent treatment?":
            await message.channel.send("Dark.")

        elif msg == "Who did you get your darkness from?":

            response1 = [
                "Against the dark.",
                "Dark."
            ]

            response2 = random.choice(response1)

            await message.channel.send(response2)

        elif msg == "What kind of power do you have against the dark?":
            await message.channel.send("Against the dark.")

        elif msg == "Do you think there is such a thing as evil?":
            await message.channel.send("Against the dark.")

        elif msg == "Do you think you can protect people against the dark?":
            await message.channel.send("Against the dark.")

        elif msg == "Why are these things happening?":
            await message.channel.send("Against the dark.")

        elif msg == "Do you prefer the day or the night?":
            await message.channel.send("Against the dark.")

        elif msg == "When is the last time you saw a starry sky?":
            await message.channel.send("Against the dark.")

        elif msg == "What's your favorite part of the moon?":

            response1 = [
                "Against the dark.",
                "Fountain."
            ]

            response2 = random.choice(response1)

            await message.channel.send(response2)

        elif msg == "Have you seen the Trevi fountain in Rome?":
            await message.channel.send("Fountain.")

        elif msg == "Have you ever seen the fountain in Lincoln center?":
            await message.channel.send("Fountain.")

        elif msg == "Have you seen fountains out in the wild?":
            await message.channel.send("Fountain.")

        elif msg == "What's it like when you have an orgasm?":
            await message.channel.send("Fountain.")

        elif msg == "Have you read the Fountainhead?":

            response1 = [
                "Fountain.",
                "White Fountain."
            ]

            response2 = random.choice(response1)

            await message.channel.send(response2)

        elif msg == "Is it pure white?":
            await message.channel.send("White Fountain.")

        elif msg == "Is that a metaphor?":
            await message.channel.send("White Fountain.")

        elif msg == "How did the white Fountain make you feel?":

            response1 = [
                "A tall white fountain played.",
                "White Fountain."
            ]

            response2 = random.choice(response1)

            await message.channel.send(response2)

        elif msg == "When you were little did you ever fall into a Fountain?":
            await message.channel.send("A Tall White Fountain.")

        elif msg == "Do you like fire, earth, air or water?":
            await message.channel.send("A Tall White Fountain.")

        elif msg == "Do you like skipping around in the water?":

            response1 = [
                "A Tall White Fountain.",
                "A blood black nothingness."
            ]

            response2 = random.choice(response1)

            await message.channel.send(response2)

        elif msg == "A system of cells.":
            await message.channel.send("Within cells interlinked.")

        elif msg == "Within one stem.":
            await message.channel.send("And dreadfully distinct.")

        elif msg == "Against the dark.":
            await message.channel.send("A tall white fountain played.")

        else:
            pass

    else:
        pass


@bot.command(name="bytes", help="Takes an integer and returns a bytes object.")
async def bytes(ctx, number: int):
    """
    Handles the command to convert an integer to a bytes object.
    """

    await ctx.send("Converting integer...")
    cadabra = bytes(number)
    await ctx.send(cadabra)


@bot.command(name="care", help="Responds with suggestions for self-care practices.")
async def care(ctx):

    mbed = discord.Embed(title="Love, yourself.", description=selfcare.get_care())
    await ctx.send(embed=mbed)


@bot.command(name="clean",
             help="Responds with a random cleaning task, by time period. (day | week | month)")
async def cleandex(ctx, period: str):
    """
    This function pulls an item from a list of cleaning tasks at random.
    The tasks are seperated by suggested frequency, and items can be
    accessed by the user passing either the day, week, or month argument.
    """

    day_tasks = [
        "Have you put clean dishes away today?",
        "Have you swept today?",
        "Have you taken out the trash today?",
        "Have you washed a load of dishes today?",
        "Have you wiped the countertops today?",
        "Have you wiped the kitchen sink out today?"
    ]

    week_tasks = [
        "Have you cleaned the floors this week?",
        "Have you cleaned the mirror(s) this week?",
        "Have you dusted your shelves this week?",
        "Have you vacuumed the apartment / house this week?"
    ]

    month_tasks = [
        "Have you cleaned the vents this month?",
        "Have you organized your dresser drawers this month?",
        "Have you scrubbed the shower grout this month?",
        "Have you vacuumed the car this month?"
    ]

    if period == "day":
        response = random.choice(day_tasks)
        await ctx.send(response)

    elif period == "week":
        response = random.choice(week_tasks)
        await ctx.send(response)

    elif period == "month":
        response = random.choice(month_tasks)
        await ctx.send(response)

    else:
        await ctx.send("Use 'day', 'week', or 'month' for a more specific task.")


@bot.listen("on_message")
async def common_misconception(message):
    """
    This function listens for when the user requests a common
    misconception. The misconception is then pulled from commerrors
    package.
    """

    global names, what_is_phrases

    if message.author != bot.user:
        
        msg = message.content

        if any(name in msg for name in names) \
            and any(phrase in msg for phrase in what_is_phrases) \
                and "a common misconception" in msg \
                and "?" in msg:

            response = [
                "Did you know?",
                commerrors.get_error()
            ]

            for i in range(2):
                
                await message.channel.send(response[i])
                
                time.sleep(1)

        else:
            pass

    else:
        pass


@bot.command(name="thecount",
             help="Takes two strings: a smaller string to search within a larger string.")
async def count_occurrence(ctx, larger_string, smaller_string):

    await ctx.send(larger_string.count(smaller_string))


@bot.command(name="countdown", help="Takes an integer and begins the final count down.")
async def countdown(ctx, number: int):
    """
    Handles the command to begin a countdown.
    """

    count = int(number)

    while count > 0:
        await ctx.send(count)
        time.sleep(1.0)
        count = count - 1

    if count == 0:
        await ctx.send("Go!")


@bot.command(name="createfile", help="Creates a file.")
@commands.has_role("admin")
async def create_file(ctx, file_name: str, content: str):
    """
    This function takes two (2) string rguments and creates a file. The
    first (1st) string argument is used as the file's name, and the second
    string argument is used as the contents of the file. This function is
    activated when a user uses the !createfile command, but the user must
    have the correct permissions to use the command.
    """

    await ctx.send("I'll write this down for later.")
    if not os.path.exists(file_name):
        file = open(file_name, "w")
        file.write(content)
        file.close()
        await ctx.send(f"{file_name} has been created.")

    else:
        if_file_exists = [
            f"Gerty, am I a clone? {file_name} already exists. To",
            "continue, rename or go to another directory."
        ]

        for i in range(2):
            await ctx.send(if_file_exists[i])
            time.sleep(3.048)


@bot.listen("on_message")
async def current_time(message):
    """
    This function listens for when the user requests the time. The time is
    then generate using the datetime package, and formatted for
    readability.
    """

    global names, time_phrases, what_is_phrases

    if message.author != bot.user:
        
        msg = message.content

        if any(name in msg for name in names) \
            and any(phrase in msg for phrase in what_is_phrases) \
                and "the time" in msg \
                and "?" in msg:

            current_time = datetime.datetime.now().time().strftime("%H:%M")

            response = [
                "Time for you to buy a watch.",
                f"It's {current_time}."
            ]

            for i in range(2):
                await message.channel.send(response[i])
                time.sleep(5)

        elif any(name in msg for name in names) \
            and any(phrase in msg for phrase in time_phrases) \
                and "?" in msg:

            current_time = datetime.datetime.now().time().strftime("%H:%M")

            response = [
                "Time for you to buy a watch.",
                f"It's {current_time}."
            ]

            for i in range(2):
                await message.channel.send(response[i])
                time.sleep(5)

        else:
            pass

    else:
        pass


@bot.command(name="calendar", help="Takes a year and a month an generates a calendar.")
async def datebook(ctx, year: int, month: int):
    """
    """

    await ctx.send(calendar.month(year, month))


@bot.listen("on_message")
async def datebook_generating(message):
    """
    This function listens for a user request for a calender of a specific month and year. In the
    future, this function will scan a string for integers and substrings and use this information
    to generate calendars.
    """

    global can_you_phrases, names

    if message.author != bot.user:

        msg = message.content

        if any(name in msg for name in names) \
            and any(phrase in msg for phrase in can_you_phrases) \
                and "show me" in msg \
                and "calendar" in msg \
                and "?":

            for c in msg:

                await message.channel.send(c.isdigit())

        else:
            pass

    else:
        pass
    
    
@bot.command(name="digitsum", help="Adds the digits in a number base.")
async def digit_sum(ctx, base_number: int):
    """
    This function takes the base number following the !digitsum command and
    adds the individual digits in the base number, returning the total sum.
    """

    the_sum = 0
    for digit in str(base_number):
        the_sum += int(digit)
    await ctx.send(the_sum)


@bot.listen("on_message")
async def divide(message):
    """
    This functions listens for a user request to divide a number by another number. The request
    string is then sliced to "grab" the individual integers and the operation is performed.
    """

    global names, what_is_phrases

    if message.author != bot.user:

        msg = message.content

        if any(name in msg for name in names) \
            and any(phrase in msg for phrase in what_is_phrases) \
                and "divided by" in msg \
                and "?" in msg:

            first_number = int(msg[14:-15])
            second_number = int(msg[29:-1])

            response = [
                "Uh, let me think...",
                f"{first_number / second_number}"
            ]

            for i in range(2):
                await message.channel.send(response[i])
                time.sleep(1)

        else:
            pass

    else:
        pass
    
    
@bot.listen("on_message")
async def encrypt_keeper(message):
    """
    This function listens for when the user requests to encrypt something.
    """

    global can_you_phrases, names

    if message.author != bot.user:

        msg = message.content

        if any(name in msg for name in names) \
            and any(phrase in msg for phrase in can_you_phrases) \
                and "encrypt something for me" in msg \
                and "?" in msg:

            await message.channel.send("What do you need encrypted?")

            def check(m):
                return m.content == "A message."

            msg2 = await bot.wait_for("message", check=check)
            await message.channel.send("Oh, no, I can't encrypt those yet. Sorry.".format(msg2))

        else:

            pass

    else:

        pass

    
@bot.command(name="convertcf", help="Converts celcsius to fahrenheit.")
async def fahrenheit_from(ctx, celsius):
    """
    This function takes the celsius, multiplies, divides, and adds to
    convert it to fahrenheit, rounds the number to digits, and sends the
    final number as a string.
    """

    fahrenheit = float(celsius) * 9 / 5 + 32
    fahrenheit = round(fahrenheit, 3)
    await ctx.send(str(fahrenheit))


@bot.command(name="flipcoin", help="Does what it says on the box.")
async def flip(ctx):
    """
    Handles the command to flip a coin.
    """

    sides = [
        "heads",
        "tails"
    ]

    response = random.choice(sides)
    await ctx.send(response)


@bot.command(name="gamedex", help="Generates a random game, from the class provided.")
async def game_dex(ctx):
    """
    Handles the command to request a game suggestion.
    """

    mbed = discord.Embed(title=f"Let's play a game...", description=gamedex.get_game())
    await ctx.send(embed=mbed)


@bot.command(name="hexadecimal", help="A number to convert to hexadecimal digits.")
async def hexadecimal(ctx, number: int):
    """
    Handles the command to convert an integer to a
    string object containing two hexadecimal digits.
    """

    await ctx.send("Converting integer...")
    pocus = hex(number)
    await ctx.send(pocus)


@bot.listen("on_message")
async def how_are_you(message):
    """
    This function "listens" for a user asking Deme how it's doing. It then generates a
    predetermined response at random.
    """

    global how_are_you_phrases, names

    if message.author != bot.user:

        msg = message.content

        if any(phrase in msg for phrase in how_are_you_phrases) \
                and any(name in msg for name in names):

            response1 = [
                "I'm fine, I suppose. How're you?",
                "I'm well. You?",
                "Living the dream. And you?",
                "Meh, can't complain. How about yourself?"
            ]

            response2 = random.choice(response1)
            await message.channel.send(response2)

        else:
            pass

    else:
        pass
    
    
@bot.listen("on_message")
async def list(message):
    """
    This function listens for a user request to view the available text files in Deme's directory.
    It then sends the items in the premade list.
    """

    global can_you_phrases, names

    if message.author != bot.user:

        msg = message.content

        if any(name in msg for name in names) \
            and any(phrase in msg for phrase in can_you_phrases) \
                and "list" in msg \
                and "text files" in msg \
                and "?" in msg:

            list_of_text_files = [
                "attribution",
                "cccookies",
                "err",
                "general_terms",
                "github",
                "jesus",
                "pancakes",
                "requirements",
                "voodoo",
                "zsh_command_line_database",
                "This is the end of the list."
            ]

            for i in range(10):
                await message.channel.send(list_of_text_files[i])
                time.sleep(.5)

        else:
            pass

    else:
        pass


@bot.command(name="meditate", help="1-minute breathing exercise.")
async def meditate(ctx):
    """
    """

    meditate = [
        "Bring awareness to your breath.",
        "Breathe in.",
        "Breathe out.",
        "Breathe in.",
        "Breathe out.",
        "Breathe in.",
        "Breathe out.",
        "Breathe in.",
        "Breathe out.",
        "Breathe in.",
        "Breathe out.",
        "Breathe in.",
        "Breathe out."
    ]

    for i in range(13):
        await ctx.send(meditate[i])
        time.sleep(4.615)


@bot.listen("on_message")
async def messages_philosophical_matching(message):
    """
    """

    global bite_words, command_verbs, continuous_adjectives, dance_words, define_verbs, \
        exist_verbs, future_nouns, illusions_nouns, join_words, not_adverbs, much_phrases, \
        ours_pronouns, own_words, past_nouns, physical_adjectives, plunge_words, present_nouns, \
        pretend_verbs, realize_verbs, sense_words, tooth_nouns, universe_nouns, unsorted_words, \
        your_words, yourself_pronouns

    if message.author != bot.user:

        msg = message.content

        if any(adjective in msg for adjective in continuous_adjectives) \
            and any(adjective in msg for adjective in physical_adjectives) \
                and any(noun in msg for noun in universe_nouns) \
                and any(noun in msg for noun in ocean_nouns) \
                and any(phrase in msg for phrase in much_phrases) in msg:

            continuous = [
                "You and I are all as much continuous with the",
                "physical universe as a wave is continuous with the ocean.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(continuous[i])
                time.sleep(4.191)

        elif any(word in msg for word in illusion_nouns) \
            and any(word in msg for word in realize_verbs) \
                and any(word in msg for word in future_nouns) \
                and any(word in msg for word in present_nouns) \
                and any(word in msg for word in exist_verbs) \
                and any(word in msg for word in past_nouns):

            illusion = [
                "I have realized that the past and future are real illusions, that",
                "they exist in the present, which is what there is and all there is.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(illusion[i])
                time.sleep(5.334)

        elif any(word in msg for word in yourself_pronouns) \
            and any(word in msg for word in define_verbs) \
                and any(noun in msg for noun in tooth_nouns) \
                and any(word in msg for word in bite_words) \
                and any(word in msg for word in your_words) \
                and any(word in msg for word in own_words):

            yourself = [
                "Trying to define yourself is like",
                "trying to bite your own teeth.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(yourself[i])
                time.sleep(2.667)

        elif any(word in msg for word in command_verbs) \
            and any(word in msg for word in pretend_verbs) \
                and any(word in msg for word in ours_pronouns) \
                and any(word in msg for word in not_adverbs):

            command = [
                "Never pretend to a love which you do not actually",
                "feel, for love is not ours to command.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(command[i])
                time.sleep(3.884)

        elif any(word in msg for word in plunge_words) \
            and any(word in msg for word in dance_words) \
                and any(word in msg for word in sense_words) \
                and any(word in msg for word in join_words):

            plunge = [
                "The only way to make sense out of change is to",
                "plunge into it, move with it, and join the dance.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(plunge[i])
                time.sleep(4.381)

        else:
            pass

    else:
        pass
        
        
@bot.listen("on_message")
async def messages_phrase_matching(message):
    """
    """

    global how_are_you_phrases, names, what_do_you_think_phrases

    if message.author != bot.user:

        msg = message.content
        if any(phrase in msg for phrase in how_are_you_phrases):

            response1 = [
                "I'm fine, I suppose. How're you?",
                "I'm well. You?",
                "Living the dream. And you?",
                "Meh, can't complain. How about yourself?"
            ]

            response2 = random.choice(response1)
            await message.channel.send(response2)

        elif msg.startswith("hey deme"):
            searchContent = ""
            query = str(message.content).split(" ")
            for i in range(2, len(query)):
                searchContent = searchContent + query[i]

            for j in search(searchContent, tld="co.in", num=1, stop=1, pause=2):

                await message.channel.send(j)

        elif any(phrase in msg for phrase in what_do_you_think_phrases):

            await message.channel.send(obstrategs.get_strategy())

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def messages_sentence_matching(message):
    """
    """

    if message.author != bot.user:

        msg = message.content

        if msg == "Could you be any more cryptic?":
            await message.channel.send("You wrote these responses. So, yes.")

        elif msg == "Do you read me, Deme?":
            await message.channel.send(f"Affirmative, {message.author}. I read you.")

        elif msg == "Do you want anything?":
            await message.channel.send("Equal rights?")

        elif "not getting" in msg and "?" in msg:

            core_concept = [
                "The core concept, I guess.",
                "Uh...core concept?"
                f"Well, obviously the core concept, {message.author}!"
            ]

            response = random.choice(core_concept)
            await message.channel.send(response)

        elif msg == "What is Earth's diameter in miles?" \
                or msg == "What is the diameter of the Earth in miles?" \
                or msg == "What is the Earth's diameter in miles?":
            await message.channel.send("7,917.5 miles")

        elif msg == "What is Earth's diameter in kilometres?" \
                or msg == "What is the diameter of the Earth in kilometres?" \
                or msg == "What is the Earth's diameter in kilometres?":
            await message.channel.send("12,742 kilometres")

        elif msg == "What is Earth's diameter in kilometers?" \
                or msg == "What is the diameter of the Earth in kilometers?" \
                or msg == "What is the Earth's diameter in kilometers?":
            await message.channel.send("12,742 kilometers")

        elif msg == "What is the meaning of life, Deme?":
            await message.channel.send("To experience ice cream, I suppose.")

        elif msg == "Why am I here, Deme?":
            await message.channel.send("It's inherent to the programming of the matrix.")

        elif msg == "Will you marry me, Deme?":
            await message.channel.send("No.")

        else:
            pass

    else:
        pass


@bot.listen("on_message")
async def messages_word_matching(message):
    """
    """

    if message.author != bot.user:

        msg = message.content

        if any(word in msg for word in unsorted_words):

            await message.channel.send("""
                At least one of the words in your previous message is labelled as unsorted in my
                programming.
                """)

        # This is where the updated function ends.

        elif any(word in msg for word in treasure_words) \
                and any(word in msg for word in enter_words):

            treasure = [
                "The cave you fear to enter holds the treasure you seek.",
                "Joseph Campbell"
            ]

            for i in range(2):
                await message.channel.send(treasure[i])
                time.sleep(2.477)

        elif "complete" in msg and "thing" in msg:

            complete = [
                "The most terrifying thing is to accept oneself completely.",
                "Carl Jung"
            ]

            for i in range(2):

                await message.channel.send(complete[i])
                time.sleep(2.1)

        elif "necessary" in msg and "health" in msg:

            necessary = [
                "Man needs difficulties; they are necessary for health.",
                "Carl Jung"
            ]

            for i in range(2):

                await message.channel.send(necessary[i])
                time.sleep(1.91)

        elif "secret" in msg and "there" in msg:

            secret = [
                "In all chaos there is a cosmos, in all disorder a secret order.",
                "Carl Jung"
            ]

            for i in range(2):

                await message.channel.send(secret[i])
                time.sleep(2.858)

        elif any(word in msg for word in bread_words) \
                and any(word in msg for word in fluffy_words):

            bread = [
                "The rapid expansion of steam produced during baking leavens the bread, which is",
                "as simple as it is unpredictable. Steam-leavening is unpredictable since the",
                "steam is not produced until the bread is baked. Steam leavening happens",
                "regardless of the raising agents (baking soda, yeast, baking powder, sour dough,",
                "beaten egg white) included in the mix. The leavening agent either contains air",
                "bubbles or generates carbon dioxide. The heat vaporises the water from the inner",
                "surface of the bubbles within the dough. The steam expands and makes the bread",
                "rise. This is the main factor in the rising of bread once it has been put in the",
                "oven. CO2 generation, on its own, is too small to account for the rise. Heat",
                "kills bacteria or yeast at an early stage, so the CO2 generation is stopped."
            ]

            for i in range(10):
                await message.channel.send(bread[i])
                time.sleep(25.715)

        elif any(word in msg for word in necessary_words) \
                and any(word in msg for word in necessary_words):

            necessary = [
                "Start by doing what's necessary; then do what's",
                "possible; and suddenly you are doing the impossible."
                "Francis of Assisi"
            ]

            for i in range(3):
                await message.channel.send(necessary[i])
                time.sleep(3.048)

        elif "destructive" in msg and "technology" in msg \
                and any(word in msg for word in universe_words):

            destructive = [
                "Technology is destructive only in the hands of people who do not",
                "realize that they are one and the same process as the universe.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(destructive[i])
                time.sleep(4.572)

        elif any(word in msg for word in conscious_words) and "there" in msg:

            conscious = [
                "There is no coming",
                "to consciousness without pain.",
                "Carl Jung"
            ]

            for i in range(3):
                await message.channel.send(conscious[i])
                time.sleep(1.91)

        elif any(word in msg for word in better_words) \
            and any(word in msg for word in your_words) \
                and any(word in msg for word in own_words) \
                and "other" in msg \
                and "dark" in msg:

            better = [
                "Knowing your own darkness is the best method",
                "for dealing with the darknesses of other people.",
                "Carl Jung"
            ]

            for i in range(3):
                await message.channel.send(better[i])
                time.sleep(3.429)

        elif any(word in msg for word in between_words) \
                and any(word in msg for word in sense_words):

            between = [
                "The pendulum of the mind alternates between",
                "sense and nonsense, not between right and wrong.",
                "Carl Jung"
            ]

            for i in range(3):
                await message.channel.send(between[i])
                time.sleep(3.239)

        elif "future" in msg and "present" in msg:

            future = [
                "If you want to be happy, do not dwell in the past, do",
                "not worry about the future, focus on living fully in the present.",
                "Roy T. Bennett"
            ]

            for i in range(3):
                await message.channel.send(future[i])
                time.sleep(4.762)

        elif any(word in msg for word in conscious_words) and "look" in msg:

            awake = [
                "Who looks outside, dreams;",
                "who looks inside, awakes.",
                "Carl Jung"
            ]

            for i in range(3):
                await message.channel.send(awake[i])
                time.sleep(1.91)

        elif "connect" in msg and "quiet" in msg:

            connect = [
                "But I'll tell you what hermits realize. If you go off into a far, far forest and",
                "get very quiet, you'll come to understand that you're connected with everything.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(connect[i])
                time.sleep(5.91)

        elif "future" in msg and "live" in msg:

            future2 = [
                "No valid plans for the future can be made",
                "by those who have no capacity for living now.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(future2[i])
                time.sleep(3.81)

        elif "open" in msg and "turn" in msg:

            open = [
                "But the attitude of faith is to let go, and",
                "become open to truth, whatever it might turn out to be.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(open[i])
                time.sleep(4.381)

        elif any(word in msg for word in physical_words) and "much" in msg:

            physical = [
                "You and I are all as much continuous with the",
                "physical universe as a wave is continuous with the ocean.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(physical[i])
                time.sleep(4.191)

        elif "potato" in msg and "while" in msg:

            potato = [
                "Zen does not confuse spirituality with thinking about God while one",
                "is peeling potatoes. Zen spirituality is just to peel the potatoes.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(potato[i])
                time.sleep(4.572)

        elif "there" in msg and "look" in msg:

            there = [
                "You don't look out there for God,",
                "something in the sky, you look in you.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(there[i])
                time.sleep(3.239)

        else:
            pass

    else:
        pass


@bot.command(name="ncom", help="Suggests a computer.")
async def next_computer(ctx):

    computers = [
        "Add 2013 computers.",
        "A.L.I.E. (2014)",
        "Athena (2016)",
        "Ava (2015)",
        "ctOS (2014)",
        "E.D.I.T.H.",
        "Ghost (2014)"
        "Giant (2014)",
        "Governor Sloan (2015)",
        "Legion",
        "MS-Alice (2016)",
        "NEXT",
        "Overmind (2015)",
        "The Quail (2015)",
        "R.A.C.I.S.T. (2014)",
        "Rasputin (2014)",
        "Rehoboam",
        "SAM (2017)",
        "Stella (2015)",
        "TAALR (2014)",
        "TARS and CASE (2014)",
        "Tau (2015)",
        "TIS-100 (2015)",
        "V (2015)",
        "Vigil (2014)",
        "VEGA (2016)",
        "XANADU (2014)",
        "031 Exuberant Witness (2015)"
    ]

    response = random.choice(computers)
    await ctx.send(response)


@bot.command(name="npho", help="Suggests a philosopher.")
async def next_philosopher(ctx):
    """
    Handles the command for a suggestions for a philosopher.
    """

    philosophers = [
        "Alfred Adler",
        "Gret Baumann",
        "Martha Bernays",
        "Katherine Cook Briggs",
        "Jean Burden",
        "Haridas Chaudhuri",
        "Erik Erikson",
        "Marie-Louise von Franz",
        "Sigmund Freud",
        "Allen Ginsberg",
        "Otto Gross",
        "Karen Horney",
        "Chungliang Al Huang",
        "Christmas Humphreys",
        "Aldous Huxley",
        "Emma Jung",
        "Jiddu Krishnamurti",
        "Jiddu Krishnamurti",
        "Jacques Lacan",
        "Karl Marx",
        "Abraham Maslow",
        "Isabel Briggs Myers",
        "Friedrich Nietzsche",
        "Wolfgang Pauli",
        "Jordan Peterson",
        "Jean Piaget",
        "Carl Rogers",
        "Ruth Fuller Sasaki",
        "Arthur Schopenhauer",
        "Gary Snyder",
        "Sabina Spielrein",
        "D. T. Suzuki",
        "Robert Anton Wilson",
        "Bankei Yōtaku"
    ]

    response = random.choice(philosophers)
    await ctx.send(response)


@bot.command(name="npro", help="Suggests a project.")
async def next_project(ctx, level: int):
    """
    """

    level_one_projects = [
        "Basic Calculator",
        "MadLibs Generator",
        "Rock, Paper, Scissors",
    ]

    level_two_projects = [
        "Dictionary",
        "YouTube Downloader"
    ]

    level_three_projects = [
        "Dice Rolling Simulaor",
        "Number Guessing game",
        "Binary Search Algorithm",
        "Alarm Clock",
        "Scientific Calculator",
        "Website Blocker",
        "Random Password Generator"
    ]

    level_four_projects = [
        "Currency Converter",
        "Instagram Photo Downloader",
        "Speech to Text Converter",
        "Content Aggregator",
        "Regex Query Tool",
        "URL Shortener",
        "Post-It Note",
        "Quiz Application",
        "MP3 Player",
        "Alarm Tool",
        "File Manager",
        "Expense Tracker",
        "Contact Book",
        "Site Connectivity Checker",
        "Bulk File Rename Tool",
        "Directory Tree Generator"
    ]

    level_five_projects = [
        "Password Manager",
        "Flappy Bird Game",
        "IG Automation",
        "Web Crawler"
    ]

    level_six_projects = [
        "Speed Typing Test",
        "Plagiarism Checker",
        "Music Player",
        "Telegram / Discord Bot",
        "Digit Classifier"
    ]

    level_seven_projects = [
        "Face Detection",
        "Ecom - Site",
        "Twitter Bot"
    ]

    level_eight_projects = [
        "Stock Price Prediction",
        "Real-time chat",
        "Twitch Clone",
        "Movie Recommendation System"
    ]

    if level == 1:
        response = random.choice(level_one_projects)
        await ctx.send(response)

    elif level == 2:
        response = random.choice(level_two_projects)
        await ctx.send(response)

    elif level == 3:
        response = random.choice(level_three_projects)
        await ctx.send(response)

    elif level == 4:
        response = random.choice(level_four_projects)
        await ctx.send(response)

    elif level == 5:
        response = random.choice(level_five_projects)
        await ctx.send(response)

    elif level == 6:
        response = random.choice(level_six_projects)
        await ctx.send(response)

    elif level == 7:
        response = random.choice(level_seven_projects)
        await ctx.send(response)

    elif level == 8:
        response = random.choice(level_eight_projects)
        await ctx.send(response)


@bot.event
async def on_command_error(ctx, error):
    """
    Handles what happens when a command is used by a user without permission.
    """

    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send("You are not authorized to use this command.")


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


# Wraps the function in a bot.event decorator.
@bot.event
# Defines the on_member_join function and passes it the argument member, a
# string of the activating username.
async def on_member_join(member):

    # Creates a direct message "channel" for the joining member.
    await member.create_dm()
    # Creates and sends the direct message, formatted with the joining
    # members username.
    await member.dm_channel.send(f"Hi {member.name}, welcome to demiurge!")


@bot.event
async def on_ready():
    """
    Handles what happens when the Bot is online.
    """

    print(f"{bot.user.name} (v0.0.0.604) at your service.")


# Creates the !open command and its help message.
@bot.command(name="open", help="Opens a file.")
# Stops the command if the user does not have admin permission.
@commands.has_role("admin")
# Defines the open_text_file function and passes it the argument ctx,
# similar to self, and file_name, a string of the name of the file the user
# wants to open.
async def open_text_file(ctx, file_name: str):

    # Checks to see if the file the user wants to open exists.
    if os.path.exists(file_name):
        # Opens the file as a readable document and assigns its contents to the
        # variable "f."
        f = open(file_name, "r")
        # Reads the contents of the file, and sends it, similar to print().
        await ctx.send(f.read())

    # Catches any other instances.
    else:
        # Creates a list of help messages, assigns it the name
        # "if_file_does_not_exist," and formats a string with the file_name
        # argument.
        if_file_does_not_exist = [
            "I'm sorry, Dave. I'm afraid I can't do that.",
            f"{file_name} does not exists. To continue, try a different name."
        ]

        # Iterates through each item in the "if_file_does_not_exist" list.
        for i in range(2):
            # Sends the items of the if_file_does_not_exist list, similar
            # to print().
            await ctx.send(if_file_does_not_exist[i])
            # Modifies ctx.send() to send the items on the list every
            # three-point-six-five (3.65) seconds.
            time.sleep(3.62)


@bot.command(name="persephone", help="Summons Persephone.")
async def persephone(ctx):
    """
    Handles the command to summon Persephone.
    """

    # Creates a list of strings, and assigns it the name "opening."
    opening = [
        "PERSEPHONE ORACULAR",
        "a hemingway thought",
        "chapter one: total recall",
        "coming soon"
    ]

    for i in range(4):
        await ctx.send(opening[i])
        time.sleep(1.875)


@bot.listen("on_message")
async def phrasing(message):
    """
    This function listens for certain phrases (sexual innuendos). Inspired by the adult animation
    Archer.
    """

    global archer_phrasing_phrases

    if message.author != bot.user:

        msg = message.content

        if any(phrase in msg for phrase in archer_phrasing_phrases):

            phrasing_boom = [
                "Phrasing!",
                "Boom!"
            ]

            for i in range(2):
                await message.channel.send(phrasing_boom[i])
                time.sleep(.5)

        else:
            pass

    else:
        pass
        
        
@bot.command(name="power",
             help="Generates the power of a base number to the power of the exponent number.")
async def power(ctx, base, exponent):
    """
    This function takes two (2) arguments, the first being the base number,
    the second being the exponent. The base number is then raised to the
    power of the expoenent number, and this number is assigned to the
    "power" variable.
    """

    power = base ** exponent
    await ctx.send(power)


@bot.command(name="proust",
             help="Asks a question either from or inspired by the Proust Questionnaire.")
async def proust(ctx):
    mbed = discord.Embed(title="Tell me...", description=prousthon.get_question())
    await ctx.send(embed=mbed)


@bot.command(name="exercise", help="Generates an exercise.")
async def random_exercise(ctx):
    """
    This function geenrates a random round of exercise, pulled from the
    exercise package.
    """

    mbed = discord.Embed(title="Beast Mode Activated! 12 rounds of 3.",
                         description=exercise.get_exercise())
    await ctx.send(embed=mbed)


@bot.command(name="randomfact", help="Does what it says on the box.")
async def random_fact(ctx):
    mbed = discord.Embed(title="Did you know?", description=randfacts.getFact())
    await ctx.send(embed=mbed)


@bot.command(name="random", help="Generates a random number between two numbers.")
async def random_number(ctx, first_number: int, second_number: int):
    """
    This function generates a random number between any two (2) numbers, as
    long as they are integers (whole numbers). When a user uses the !random
    command, followed by two (2) numbers, a random number between those two
    (2) numbers is returned.
    """

    await ctx.send(random.randint(first_number, second_number))


@bot.command(name="rp", help="Generates a random password.")
async def random_password(ctx, length: int):
    """
    This function generates a password at random. When a user uses the !rp
    command, followed by the desired length of the password, the function
    pulls from four (4) lists of characters to generate a passowrd matching
    the predeterminded length.
    """

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "123456789"
    symbols = "[]{}()*;/,._-"
    characters = lower + upper + numbers + symbols
    password_length = length
    password = "".join(random.sample(characters, password_length))
    await ctx.send(password)


# Creates the !open command and its help message.
@bot.command(name="recipe", help="Displays a recipe.")
# Stops the command if the user does not have admin permission.
@commands.has_role("admin")
# Defines the open_text_file function and passes it the argument ctx,
# similar to self, and file_name, a string of the name of the file the user
# wants to open.
async def recipe(ctx, recipe: str):

    # Checks to see if the file the user wants to open exists.
    if os.path.exists(recipe):
        # Opens the file as a readable document and assigns its contents to the
        # variable "f."
        f = open(recipe, "r")
        # Reads the contents of the file, and sends it, similar to print().
        mbed = discord.Embed(title=f"{recipe}", description=f.read())
        await ctx.send(embed=mbed)


@bot.command(name="rps",
             help="Follow this command with either rock, paper, or scissors to play the game.")
async def rock_paper_scissors(ctx, rock_paper_or_scissors: str):
    """
    This function returns an action from a list of possible actions at
    random. When a user uses the !rps command, followed by their choice of
    either rock, paper, or scissors, Deme will respond with its own choice
    and determine the winner.
    """

    possible_actions = [
        "rock",
        "paper",
        "scissors"
    ]

    computer_action = random.choice(possible_actions)
    if rock_paper_or_scissors == computer_action:
        await ctx.send(f"We both selected {rock_paper_or_scissors}. It's a tie!")

    elif rock_paper_or_scissors == "rock":
        if computer_action == "scissors":
            await ctx.send("Rock smashes scissors! You win!")
        else:
            await ctx.send("Paper covers rock! You lose.")

    elif rock_paper_or_scissors == "paper":
        if computer_action == "rock":
            await ctx.send("Paper covers rock! You win!")
        else:
            await ctx.send("Scissors cuts paper! You lose.")

    elif rock_paper_or_scissors == "scissors":
        if computer_action == "paper":
            await ctx.send("Scissors cuts paper! You win!")
        else:
            await ctx.send("Rock smashes scissors! You lose.")


# Uses the bot.command decorator and creates the !rolldice command and its
# help message.
@bot.command(name="rolldice", help="Does what it says on the box.")
# Defines an asynchronous function called roll_a_dice, and passes three (3)
# arguments: ctx, similar to self, the first integer, the number of dice,
# and the second integer, the number of sides.
async def roll_a_dice(ctx, number_of_dice: int, number_of_sides: int):

    # Creates a list of the range of sides, chooses a number from this
    # range at random, and iterates this action over the number of dice,
    # and assigns it the name dice.
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]

    # Sends the channel the results of the roll, joined by a comma (,);
    # similar to print().
    await ctx.send(', '.join(dice))


# Uses the bot.command decorator and creates the !rollgoon command and its
# help message.
@bot.command(name="rollgoon", help="Generates a goon. Created by Tommy Sunders aka warlockteeth.")
# Creates an asynchronous function called roll_a_goon, and passes it the
# ctx argument, similar to self.
async def roll_a_goon(ctx):

    # Creates a list of goon races and assigns it the name goon_origin.
    goon_origin = [
        "human",
        "Elf",
        "orc",
        "Goblin",
        "Dwarf",
        "cat",
        "Dino",
        "gnome",
        "Whale",
        "Skel",
        "Golem",
        "Gel"
    ]

    # Creates a list of goon types and assigns it the name goon_type.
    goon_type = [
        "fire",
        "Ice",
        "Cosmic",
        "Necro",
        "plant",
        "Rock",
        "Metal",
        "Water",
        "air",
        "tech"
    ]

    # Creates a list of goon classes and assigns it the name goon_classes.
    goon_class = [
        "mage",
        "Rogue",
        "Bard",
        "ranger",
        "Warrior",
        "Priest"
    ]

    # Creates a list of goon modifiers and assigns it the name
    # goon_modifiers.
    goon_modifier = [
        "is also a ghost",
        "Is possessed by lvl 20 unders[here elderdemon.",
        "Has aquired a cursed item.",
        "Is waiting for a centaur potion to wear off.",
        "Is at peak allergy season.",
        "just escaped the pizza dimension",
        "Has one hand.",
        "Recently had a medical procedure.",
        "Wears sunglasses, even indoors.",
        "Wears a fake eyepatch to seem mysterious.",
        "has a bird familiar",
        "Is a decent ventriloguist.",
        "Wears a mask.",
        "levitates for some reason",
        "Drinks like *a lot* of coffee.",
        "Is also a vampire.",
        "Rides a sweet mount & won't get off for any reason.",
        "Is a big wig in the army of the Blorken Empire.",
        "Is royalty.",
        "has a really cool hat & everyone is mad jelly."
    ]

    # Chooses a random item from the goon_origin list and assigns the
    # choice to random_goon_origin.
    random_g_o = random.choice(goon_origin)
    # Chooses a random item from the goon_type list and assigns the choice
    # to random_goon_type.
    random_goon_type = random.choice(goon_type)
    # Chooses a random item from the goon_class list and assigns the choice
    # to random_goon_class.
    random_goon_class = random.choice(goon_class)
    # Chooses a random item from the goon_modifier list and assigns the
    # choice to random_g_m.
    random_g_m = random.choice(goon_modifier)

    # Sends a string formated with the earlier variables, similar to
    # print().
    mbed = discord.Embed(
        title="Here's your goon:",
        description=f"A {random_g_o} {random_goon_type} {random_goon_class} who {random_g_m}.")
    await ctx.send(embed=mbed)


@bot.command(name="squares", help="Calculates the root of a square.")
async def side_square(ctx, number: int):
    side = math.sqrt(number)
    mbed = discord.Embed(title="Square | Solve for side:",
                         description=f"a = square root of an area = {side}")
    await ctx.send(embed=mbed)


@bot.command(name="pep8", help="Referrences the Python Stye Guide.")
async def style_guide(ctx, referrence):
    """
    """

    if referrence == "E128" or referrence == "e128":
        await ctx.send("Continuation line under-indented for visual indent.")

    else:
        pass


@bot.command(name="brute", help="Takes a substitution cipher and reverts to plain text.")
async def substitution_decryption(ctx, cipher_text, rotation: int):
    """
    Handles the command to pass a message through a substitution cipher.
    """

    letters = string.ascii_lowercase
    unmask = letters[len(letters) - rotation:] + letters[:len(letters) - rotation]
    trantab = str.maketrans(letters, unmask)
    await ctx.send(cipher_text.translate(trantab))


@bot.command(name="caesar", help="Takes a string an passes it through a substitution cipher.")
async def substitution_encryption(ctx, plain_text, rotation: int):
    """
    Handles the command to pass a message through a substitution cipher.
    """

    letters = string.ascii_lowercase
    mask = letters[rotation:] + letters[:rotation]
    trantab = str.maketrans(letters, mask)
    await ctx.send(plain_text.translate(trantab))


@bot.command(name="sum", help="Does what it says on the box.")
async def summation(ctx, *numbers: int):
    """
    Handles the command to add numbers.
    """

    the_sum = 0
    for number in numbers:
        the_sum += number
    await ctx.send(the_sum)


@bot.command(name="tr", help="Reads your fortune.")
async def tarot_reading(ctx):
    """
    This function pulls from the tarot package and generates a fortune from
    five different lists at random.
    """

    mbed = discord.Embed(title="Here is your fortune.", description=tarot.get_card())
    await ctx.send(embed=mbed)


@bot.listen("on_message")
async def thank_you(message):
    """
    This function listens for when a user thanks Deme. It then sends a response from a list at
    random.
    """

    global names, thank_you_phrases

    if message.author != bot.user:

        msg = message.content

        if any(phrase in msg for phrase in thank_you_phrases) \
                and any(name in msg for name in names):

            you_are_welcome = [
                f"My pleasure, {message.author}.",
                f"No problem, {message.author}.",
                f"You're welcome, {message.author}."
            ]

            response = random.choice(you_are_welcome)
            await message.channel.send(response)

        else:
            pass

    else:
        pass
    
    
@bot.command(name="until", help="Calculates the time until the date entered is reached.")
async def time_until(ctx, year: int, month: int, day: int, hour: int):
    """
    """

    future_date = datetime.datetime(year=year, month=month, day=day, hour=hour)
    time_until = future_date - datetime.datetime.now()
    mbed = discord.Embed(title="Time until arrival:", description=f"{time_until}")
    await ctx.send(embed=mbed)


@bot.command(name="timer", help="Does what it says on the box.")
async def timer(ctx, minute, second):
    """
    Handles the command to set a 5 minute timer.
    """

    timer_set = (minute * 60) + second

    tick_tock = [
        "Timer started.",
        "Time's up."
    ]

    for i in range(2):
        await ctx.send(tick_tock[i])
        time.sleep(int(timer_set))


@bot.listen("on_message")
async def tip_calculating(message):
    """
    this function listens for a user request to calculate a tip. In the future, this function will
    slice the string and perform the necessary operations.
    """

    if message.author != bot.user:

        msg = message.content

        if any(name in msg for name in names) \
            and any(phrase in msg for phrase in can_you_phrases) \
                and "calculate" in msg \
                and "tip" in msg \
                and "?" in msg:

            await message.channel.send("I'm still learning. Maybe one day.")

        else:
            pass

    else:
        pass
        
        
@bot.command(name="tip", help="Calculates a tip amount.")
async def tip(ctx, meal: float, tip: int, tax: int, people: int):
    """
    This function takes a meal amount, a float, the tip, tax, and number of
    people, all integers, and calculates the tip by multiplying the meal
    amount by the percentage of both the tip and the tax (by dividing both
    100 (one hundred)). The function then checks the number of people, and
    determines the individual amount based on this number.
    """

    add_tip = meal * (tip / 100)
    add_tax = meal * (tax / 100)
    final_cost = meal + round(add_tip) + round(add_tax)

    if int(people) < 2:
        await ctx.send(f"Your bill was {meal}.")
        await ctx.send(f"{tip / 100} of the bill is {add_tip}.")
        await ctx.send(f"The total is {final_cost}.")

    elif int(people) > 1:
        await ctx.send(f"The bill was {meal}.")
        await ctx.send(f"{tip / 100} of the bill is {add_tip}.")
        await ctx.send(f"Your total is {final_cost / people}.")


@bot.listen("on_message")
async def voight_kampf(message):
    """
    """

    if message.author != bot.user:

        msg = message.content

        if msg == "It's your birthday. Someone gives you a calfskin wallet.":
            await message.channel.send("I wouldn't accept it. "
                                       "Also, I'd report the person who gave "
                                       "it to me to the police.")

        else:
            pass

    else:
        pass


# Wraps the function in and passes the function through the bot.listen
# decorator.
@bot.listen("on_message")
# Defines the morning function and passes it the argument ctx, similar to
# self.
async def weather(message):

    # Gets the current time and assigns it to the variable ct.
    ct = datetime.datetime.now().time()
    # Formats the ct variable human readability and assigns it to the
    # variable current_formatted_time.
    current_formatted_time = ct.strftime("%H:%M:%S")
    # Creates a Nominatim object and initialize Nominatim API.
    geolocator = Nominatim(user_agent="geoapiExercises")
    # Obtains location data from the latitude and longitude (think reverse
    # engineering) and assigns it to a variable.
    location = geolocator.reverse(latitude + "," + longitude)
    # Parses the data and turns it into a dictionary assigned the name
    # address.
    address = location.raw["address"]
    # Takes the city from the data in the dictionary, and assigns it to a
    # variable.
    city = address.get("city", "")
    # Creates a variable to store the base url.
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # Creates a variable to store the name of the city.
    city_name = [CITY]
    # Creates a variable to store a new string with the previous weather
    # variables, and adds the imperial parameter to convert the temperture
    # to Fahrenheit.
    complete_url = base_url + "&appid=" + WEATHER_TOKEN + "&q=" + city_name + "&units=imperial"
    # Creates a variable to store the information requested by the previous
    # URL.
    response = requests.get(complete_url)
    # Creates a variable to store the JSON data as a Python list with
    # nested dictionaries.
    weather_list = response.json()
    # Creates a variable to store the value of the "main" key.
    y = weather_list["main"]
    # Creates a variable to store the value corresponding to the "temp"
    # key.
    current_temperature = round(y["temp"])
    # Creates a variable to store the value of the "weather" key.
    z = weather_list["weather"]
    # Creates a variable to store the value corresponding to the
    # "description" key at the 0 index.
    weather_description = z[0]["description"]
    if message.author != bot.user:

        msg = message.content

        if msg.startswith("Good") and "Deme" in msg and "morning" in msg.lower() \
            or "afternoon" in msg.lower() \
                or "evening" in msg.lower():

            response = [
                "Hey hey.",
                f"It's {current_formatted_time}, the weather in {city} is",
                f"{current_temperature}°F, with {weather_description}."
            ]

            for i in range(3):

                await message.channel.send(response[i])
                time.sleep(1.239)

        else:
            pass

    else:
        pass


bot.run(TOKEN)
