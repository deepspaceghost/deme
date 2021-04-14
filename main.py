import argparse
import click
import discord
import os
import random

from theconverter import The_Converter
from discord.ext import commands
from dotenv import load_dotenv
from googlesearch import search
from lumberjack import Logger

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="!")


@click.group()
def cli():
    """
    Deme (short for Demeter) is a command line interface (CLI) program, Discord IM bot, and
    primitive virtual assistant, as well as an exercise in natural language processing.
    """

    pass


@cli.command()
@click.option("--ascii-code", default=100, help="An integer to convert to an ASCII character.")
def ascii(ascii_code):
    """
    Handles the command to convert an integer within ASCII code to an ASCII character.
    """

    the_converter = The_Converter()
    lumberjack = Logger()
    chango = the_converter.ascii(ascii_code, lumberjack.get_logger())
    click.echo(chango)


@bot.command(name="ascii", help="Takes an ASCII code and returns the corresponding character.")
async def ascii_bot(ctx, ascii_code: int):
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


def parse_tree():
    """
    Handles commands from the command line.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--bytes",
                        action="store",
                        nargs=1,
                        help="Usage: ./deme.py --bytes [number]",
                        dest="bytes_args")
    parser.add_argument("--hexadecimal",
                        action="store",
                        nargs=1,
                        help="Usage: ./deme.py --hexadecimal [number]",
                        dest="hex_args")

    args = parser.parse_args()

    if args.bytes_args:
        number = int(args.bytes_args[0])
        the_converter = The_Converter()
        lumberjack = Logger()
        the_converter.bytes(number, lumberjack.get_logger())

    elif args.hexadecimal_args:
        number = int(args.hexadecimal_args[0])
        the_converter = The_Converter()
        lumberjack = Logger()
        the_converter.hexadecimal(number, lumberjack.get_logger())
    
    
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

when_propmted = input("Would you like to connect to Discord? [Y]es/[n]o: ")
if when_propmted == "y":
    print("Okay. Deme is connecting to Discord.")
    bot.run("ODI4MDg0NDcxMzg2NzM0NjIy.YGkbww.zTtM1puL-cucIgCTWeKR70ryqjU")

elif when_propmted == "n":
    print("Okay. Deme was not connected to Discord.")
    if __name__ == "__main__":
        """
        """

        parse_tree()
        cli()

else:
    pass

bot.run("TOKEN")
