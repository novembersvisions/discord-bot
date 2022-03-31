# Importing packages
import os
from dotenv import load_dotenv

# .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# connect to discord
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random

bot = Bot("!")
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
   print("Ready")

# Generate airplane images
NumImages = 22
ImageBaseLink = 'http://hivemindbot.surge.sh/img/'
ImageExtension = '.jpg'
ImageLinks = []
for x in range(NumImages):
   ImageLink = f'{ImageBaseLink}{x}{ImageExtension}'
   ImageLinks.append(ImageLink)
     
@client.command()
async def gatz(ctx):
   GatzLink = ImageLinks[random.randint(0, len(ImageLinks)-1)]
   embed = discord.Embed(title="airplane", color=discord.Color.red())
   embed.set_image(url=GatzLink)
   await ctx.send(embed=embed)

client.run(TOKEN)