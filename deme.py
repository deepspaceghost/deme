import discord
import os

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
client = discord.Client()


@client.event
async def when_ready():
    """
    Handles what happens when the Client has established a connection to Discord and it has
    finished preparing the data Discord has sent. It will be called (and print its messages) once
    client is ready for further action.
    """

    guild = discord.utils.get(client.guilds, name="Artinov")

    print(
        f"{client.user} is connected to the following guild:\n"
        f"{guild.name}(id: {guild.id})\n"
    )

    members = "\n - ".join([member.name for member in guild.members])
    print(f"Guild Members:\n - {members}")


@client.event
async def when_member_joins(member):
    """
    Handles what happens when a new member joins a guild.
    """

    await member.create_dm()
    await member.dm_channel.send(
        f"Hi {member.name}, welcome to Artinov!"
    )

client.run(TOKEN)
