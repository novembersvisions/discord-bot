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

@client.command()
async def bird(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/bird')
      birdjson = await request.json()
      embed = discord.Embed(title="a bird", color=discord.Color.blue())
      embed.set_image(url=birdjson['link'])
      await ctx.send(embed=embed)

client.run(TOKEN)