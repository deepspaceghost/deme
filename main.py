import datetime
import discord
import os
import random
import time

from discord.ext import commands
from dotenv import load_dotenv
from googlesearch import search

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

help_command = commands.DefaultHelpCommand(no_category="Commands")
bot = commands.Bot(command_prefix="!", help_command=help_command)


@bot.command(name="add", help="Does what it says on the box.")
async def add(ctx, *args: int):
    """
    Handles the command to add numbers.
    """

    the_sum = 0
    for x in args:
        the_sum += x
    await ctx.send(the_sum)


@bot.command(name="ascii", help="Takes an ASCII code. Returns the corresponding character.")
async def ascii(ctx, ascii_code: int):
    """
    Handles the command to convert a ASCII code to an ASCII character.
    """

    await ctx.send("Let's see...")

    if ValueError:
        await ctx.send(f"{ascii_code} is either not within range, or is not an integer.")
        await ctx.send("To continue, give me a number between 0 and 1,114,111.")

    else:
        await ctx.send("Converting integer...")
        chango = chr(ascii_code)
        await ctx.send(chango)


@bot.command(name="bytes", help="Takes an integer and returns a bytes object.")
async def bytes(ctx, number: int):
    """
    Handles the command to convert an integer to a bytes object.
    """

    await ctx.send("Converting integer...")
    cadabra = bytes(number)
    await ctx.send(cadabra)


@bot.command(name="care", help="Responds with suggestions for self-directed care.")
async def care(ctx):
    """
    Handles the command for self-directed care suggestions.
    """

    care = [
        "Journal Therapy: Create both sides to a conversation involving anything.",
        "Journal Therapy: Describe the essence and emotional experience of a memory.",
        "Self-care: drink a glass of water.",
        "Self-care: eat some food.",
        "Self-care: get some sleep.",
        "Journal Therapy: Share a journal entry with someone you trust. Ask for their thoughts.",
        "Journal Therapy: Write a number of connected items to help prioritize and organize.",
        "Journal Therapy: Write about anything for a designated period.",
        "Unsent letters: silence your internal censor.",
        "Support is 10 percent of self-care. Phone a friend (I don't count).",
        "Safety is 10 percent of self-care. You locked the door, right?",
        "Showers are 5 percent of self-care. r/showerthoughts",
        "Exercise is 5 percent of self-care. Beast mode, activate!",
        "Meditation is 5 percent of self-care. Om.",
        "Naps are 5 percent of self-care. 20 minutes sound okay?",
        "Massages are 5 percent of self-care. ",
        "Walking is 5 percent of self-care.",
        "Write this down: journaling is 4 percent of self-care.",
        "Therapy is 4 percent of self-care.",
        "Setting intentions is 4 percent of self-care.",
        "Inner work is 4 percent of self-care. Take 20 minutes to self-reflect.",
        "Setting goals is 4 percent of self-care.",
        "Take a walk.",
        "Cuddle someone.",
        "Read a book.",
        "Put pen to paper.",
        "Go on an adventure.",
        "Play a game.",
        "Work out. Type !exercise for some suggestions.",
        "Make something.",
        "Have a dance party."
    ]

    response = random.choice(care)
    await ctx.send(response)


@bot.command(name="clean",
             help="Responds with a random cleaning task, by time period. (day | week | month)")
async def cleandex(ctx, period: str):
    """
    Handles the command to request to a
    suggestion for cleaning, depending on the period.
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
async def conversation_tree(message):
    """
    Handles what happens when the user wants to have a conversation with Deme.
    """

    if message.author != bot.user:
        if message.content == "Do you read me, Deme?":
            await message.channel.send(f"Affirmative, {message.author}. I read you.")

        elif message.content == "What is the meaning of life, Deme?":
            await message.channel.send("To experience ice cream, I suppose.")

        elif message.content == "Why am I here, Deme?":
            await message.channel.send("It's inherent to the programming of the matrix.")

        elif message.content == "Will you marry me, Deme?":
            await message.channel.send("No.")


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


@bot.command(name="createchannel", help="Creates a channel.")
@commands.has_role("admin")
async def create_channel(ctx, channel_name: str):
    """
    Handles the command to create a new text
    channel, as long as the user is an administrator.
    """

    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)


@bot.command(name="createfile", help="Creates a file.")
@commands.has_role("admin")
async def create_file(ctx, file_name: str, content: str):
    """
    Handles the command to create a new text (.txt)
    file, as long as the user is an administrator.
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


@bot.command(name="currenttime", help="Gives the time.")
async def current_time(ctx):
    """
    Handles the command to give the time.
    """

    ct = datetime.datetime.now().time()
    await ctx.send(ct.strftime("%H:%M:%S"))


@bot.command(name="exercise", help="Reminders for daily exercise.")
async def exercise(ctx):
    """
    Handles the command to request a daily exercise reminder.
    """

    exercises = [
        "Ab workout, 15 minutes",
        "Full body workout, 20 minutes."
    ]

    response = random.choice(exercises)
    await ctx.send(response)


@bot.command(name="flipcoin", help="Does what it says on he box.")
async def flip(ctx):
    """
    Handles the command to flip a coin.
    """

    sides = [
        "heads",
        "heads",
        "tails",
        "tails",
        "tails"
    ]

    response = random.choice(sides)
    await ctx.send(response)


@bot.command(name="game", help="Responds with a random game suggestion.")
async def gamedex(ctx):
    """
    Handles the command to request a game suggestion.
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
async def hey_deme(message):
    """
    Handles what happens when a user wants to conduct an internet search.
    """

    if message.author != bot.user:
        if message.content.startswith("hey deme"):
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
    Handles what happens when a new user joins a guild.
    """

    await member.create_dm()
    await member.dm_channel.send(f"Hi {member.name}, welcome to demiurge!")


@bot.event
async def on_ready():
    """
    Handles what happens when the Bot is online.
    """

    print(f"{bot.user.name} (v0.0.0.179) is connected to Discord.")


@bot.command(name="open", help="Opens a file.")
@commands.has_role("admin")
async def open_text_file(ctx, file_name: str):
    """
    Handles the command to open a text (.txt)
    file, as long as the user is an administrator.
    """

    await ctx.send("Opening text file...")
    if os.path.exists(file_name):
        f = open(file_name, "r")
        await ctx.send(f.read())

    else:
        if_file_does_not_exist = [
            "I'm sorry, Dave. I'm afraid I can't do that.",
            f"{file_name} does not exists. To continue, try a different name."
        ]

        for i in range(2):
            await ctx.send(if_file_does_not_exist[i])
            time.sleep(3.62)


@bot.command(name="persephone", help="Summons Persephone.")
async def persephone(ctx):
    """
    Handles the command to summon Persephone.
    """

    opening = [
        "PERSEPHONE ORACULAR",
        "a hemingway thought",
        "chapter one: total recall",
        "coming soon"
    ]

    for i in range(4):
        await ctx.send(opening[i])
        time.sleep(1.875)


@bot.command(name="random", help="Generates a random number between two numbers.")
async def random_number(ctx, first_number: int, second_number: int):
    """
    Handles the command for a random number between two numbers.
    """

    await ctx.send(random.randint(first_number, second_number))


@bot.command(name="rockpaperscissors", help="Does what it says on the box.")
async def rock_paper_scissors(ctx, rock_paper_or_scissors: str):
    """
    Handles the command to play rock, paper, scissors.
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


@bot.command(name="rolldice", help="Does what it says on the box.")
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    """
    Handles the command to roll dice.
    """

    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]

    await ctx.send(', '.join(dice))


@bot.command(name="timer", help="Sets a timer for 5 minutes.")
async def timer(ctx):
    """
    Handles the command to set a 5 minute timer.
    """

    timer = [
        "Timer started.",
        "4 minutes left.",
        "3 minutes left.",
        "2 minutes left.",
        "1 minute left.",
        "Time's up."
    ]

    for i in range(6):
        await ctx.send(timer[i])
        time.sleep(60)


@bot.listen("on_message")
async def watts(message):
    """
    Handles what happens when the user triggers Deme to wax philosophical.
    """

    if message.author != bot.user:
        if "change" in message.content.lower() and "sense" in message.content.lower():

            change = [
                "The only way to make sense out of change is to",
                "plunge into it, move with it, and join the dance.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(change[i])
                time.sleep(4.381)

        elif "bite" in message.content.lower() and "like" in message.content.lower():

            bite = [
                "Trying to define yourself is like trying to bite your own teeth.",
                "Alan Watts"
            ]

            for i in range(2):
                await message.channel.send(bite[i])
                time.sleep(2.667)

        elif "future" in message.content.lower() and "present" in message.content.lower():

            future = [
                "I have realized that the past and future are real illusions, that",
                "they exist in the present, which is what there is and all there is.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(future[i])
                time.sleep(5.334)

        elif "future" in message.content.lower() and "live" in message.content.lower():

            future2 = [
                "No valid plans for the future can be made",
                "by those who have no capacity for living now.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(future2[i])
                time.sleep(3.81)

        elif "physical" in message.content.lower() and "much" in message.content.lower():

            physical = [
                "You and I are all as much continuous with the",
                "physical universe as a wave is continuous with the ocean.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(physical[i])
                time.sleep(4.191)

        elif "potato" in message.content.lower() and "while" in message.content.lower():

            potato = [
                "Zen does not confuse spirituality with thinking about God while one",
                "is peeling potatoes. Zen spirituality is just to peel the potatoes.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(potato[i])
                time.sleep(4.572)


bot.run("TOKEN")
