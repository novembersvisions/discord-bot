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
import aiohttp

bot = Bot("!")
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
   print("Ready")

# Generate airplane images
@client.command()
async def gatz(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://biriyani.anoram.com/get')
      planejson = await request.json()
      embed = discord.Embed(title="airplane", color=discord.Color.red())
      embed.set_image(url=planejson['link'])
      await ctx.send(embed=embed)
      