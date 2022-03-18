# Creating a connection to Discord
import os

# Importing packages
import discord
from dotenv import load_dotenv

# .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Contacting Discord's API, connecting to server
client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
    f'{client.user} has connected to the guild:\n'
    f'{guild.name}(id: {guild.id})'
    )

client.run(TOKEN)