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

bot = Bot("!")
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
   print("Ready")

# help box
@client.command()
async def info(ctx):
    embed = discord.Embed(title="list of commands", color=discord.Color.red())
    embed.add_field(name="!kafka", value="generate a kafka quote", inline=False)
    embed.add_field(name="!bird", value="generate an image of a bird", inline=False)
    embed.add_field(name="!gatz", value="generate an image of an airplane", inline=False)
    embed.add_field(name="!willow", value="generate an image of a cat along with an ominous quote", inline=False)
    embed.add_field(name="additional functionality", value="if you say hi to me, i will respond :)", inline=False)
    await ctx.send(embed=embed)
        
client.run(TOKEN)