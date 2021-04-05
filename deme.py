import discord
import os

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()


@client.event
async def on_ready():
    """
    Handles the event when the Client has established a connection to Discord and it has finished
    preparing the data Discord has sent.
    """

    guild = discord.utils.get(client.guilds, name="DISCORD_GUILD")

    print(
        f"{client.user} is connected to the following guild:\n"
        f"{guild.name}(id: {guild.id})\n"
    )

    members = "\n - ".join([member.name for member in guild.members])
    print(f"Guild Members:\n - {members}")

client.run(TOKEN)
