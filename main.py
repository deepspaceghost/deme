import discord
import os
import random

from discord.ext import commands
from dotenv import load_dotenv
from googlesearch import search
from time import sleep

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

help_command = commands.DefaultHelpCommand(no_caregory="Commands")
bot = commands.Bot(command_prefix="!", help_command=help_command)


@bot.command(name="ascii", help="Takes an ASCII code. Returns the corresponding character.")
async def ascii(ctx, ascii_code: int):
    """
    Handles the command to convert an ASCII code to an ASCII character.
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
        
        
@bot.command(name="clean", help="Responds with a random cleaning task, by time period.")
async def cleandex(ctx, period: str):
    """
    Handles the command to request to a suggestion for cleaning, depending on the period.
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
        if message.content == "Do you read me Deme?":
            await message.channel.send(f"Affirmative, {message.author}. I read you.")

        elif message.content == "What is the meaning of life Deme?":
            await message.channel.send("To experience ice cream, I suppose.")

        elif message.content == "Why am I here Deme?":
            await message.channel.send("It's inherent to the programming of the matrix.")

        elif message.content == "Will you marry me Deme?":
            await message.channel.send("No.")


@bot.command(name="countdown", help="Takes an integer and begins counting down.")
async def countdown(ctx, number: int):
    """
    Handles the command to begin a countdown.
    """

    count = int(number)

    while count > 0:
        await ctx.send(count)
        count = count - 1

    if count == 0:
        await ctx.send("Go!")
            
            
@bot.command(name="createchannel", help="Creates a channel.")
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


@bot.command(name="createfile", help="Creates a file.")
@commands.has_role("admin")
async def create_file(ctx, file_name: str, content: str):
    """
    Handles the command to create a new text (.txt) file, as long as the user is an administrator.
    """

    await ctx.send("I'll write this down for later.")
    if not os.path.exists(file_name):
        file = open(file_name, "w")
        file.write(content)
        file.close()
        await ctx.send(f"{file_name} has been created.")
        
        
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


@bot.command(name="hex", help="Takes a number and returns the corresponding hexadecimal digits.")
async def hexadecimal(ctx, number: int):
    """
    Handles the command to convert an integer to a string object containing two hexadecimal digits.
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
        sleep(6.5)
    
    
@bot.command(name="rockpaperscissors", help="Play rock, paper, scissors, with Deme.")
async def rock_paper_scissors(ctx, user_action: str):
    """
    Handles the command to play rock, paper, scissors.
    """

    possible_actions = [
        "rock",
        "paper",
        "scissors"
    ]

    computer_action = random.choice(possible_actions)
    if user_action == computer_action:
        await ctx.send(f"We both selected {user_action}. It's a tie!")

    elif user_action == "rock":
        if computer_action == "scissors":
            await ctx.send("Rock smashes scissors! You win!")
        else:
            await ctx.send("Paper covers rock! You lose.")

    elif user_action == "paper":
        if computer_action == "rock":
            await ctx.send("Paper covers rock! You win!")
        else:
            await ctx.send("Scissors cuts paper! You lose.")

    elif user_action == "scissors":
        if computer_action == "paper":
            await ctx.send("Scissors cuts paper! You win!")
        else:
            await ctx.send("Rock smashes scissors! You lose.")
    
    
@bot.command(name="rolldice", help="Simulates rolling dice.")
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    """
    Handles the command to roll dice.
    """

    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]

    await ctx.send(', '.join(dice))


@bot.command(name="selfcare", help="Responds with a self-care suggestion.")
async def self_care(ctx):
    """
    Handles the command to request a self-care suggestion.
    """

    self_care = [
        "Sleep is 10 percent of self-care. Five more minutes won't hurt.",
        "Hydration is 10 percent of self-care. So...shots?",
        "Food is 10 percent of self-care. And you're not you when you're hungry.",
        "Support is 10 percent of self-care. Phone a friend (I am your friend, but I don't count).",
        "Safety is 10 percent of self-care. You locked the door, right?",
        "Showers are 5 percent of self-care. r/showerthoughts",
        "Exercise is 5 percent of self-care. Beats mode, activate!",
        "Meditation is 5 percent of self-care. Om.",
        "Naps are 5 percent of self-care. 20 minutes sound okay?",
        "Massages are 5 percent of self-care. ",
        "Walking is 5 percent of self-care.",
        "Write this down: journaling is 4 percent of self-care.",
        "Therapy is 4 percent of self-care.",
        "Setting intentions is 4 percent of self-care.",
        "Inner work is 4 percent of self-care.",
        "Setting goals is 4 percent of self-care."
    ]

    response = random.choice(self_care)
    await ctx.send(response)

bot.run("TOKEN")
