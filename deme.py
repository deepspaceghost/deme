import discord
import os
import random

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()


@client.event
async def on_ready():
    """
    Handles what happens when the Client has established a connection to Discord.
    """

    print(
        f"{client.user.name} is connected to Discord."
    )


@client.event
async def when_member_joins(member):
    """
    Handles what happens when a new member joins a server.
    """

    await member.create_dm()
    await member.dm_channel.send(
        f"Hi {member.name}, welcome to the server!"
    )


@client.event
async def on_message(message):
    """
    Handles what happens when a message is posted in a channel Deme has access to.
    """

    if message.author == client.user:
        return

    mr_robot_quotes = [
        "We're all living in each other's paranoia.",
        "I wanted to save the world.",
        "No rest for the wicked.",
        "Exciting time in the world right now. Exciting time.",
        (
            "I never want to be right about my hacks, but people always find a way to disappoint."
        ),
    ]

    if message.content == "e1110t!":
        response = random.choice(mr_robot_quotes)
        await message.channel.send(response)

client.run(TOKEN)
