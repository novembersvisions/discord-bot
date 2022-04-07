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

# Generate Shay's images
NumImages = 50
ImageBaseLink = 'http://hivemindbot.surge.sh/shay/'
ImageExtension = '.jpg'
ImageLinks = []
for x in range(NumImages):
   ImageLink = f'{ImageBaseLink}{x}{ImageExtension}'
   ImageLinks.append(ImageLink)
     
@client.command()
async def shay(ctx):
   ShayLink = ImageLinks[random.randint(0, len(ImageLinks)-1)]
   embed = discord.Embed(title="an image for shay", color=discord.Color.gold())
   embed.set_image(url=ShayLink)
   await ctx.send(embed=embed)

client.run(TOKEN)