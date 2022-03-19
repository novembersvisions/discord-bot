# Importing packages
import os
import random
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

# Generate bird images
@client.command()
async def bird(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/bird')
      birdjson = await request.json()
      embed = discord.Embed(title="a bird", color=discord.Color.blue())
      embed.set_image(url=birdjson['link'])
      await ctx.send(embed=embed)

# Generate cat images
@client.command()
async def willow(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/cat')
      catjson = await request.json()

      willow = [
        'I have a curious animal, half kitten, half lamb. It is a legacy from my father. But it only developed in my time; formerly it was far more lamb than kitten. Now it is both in about equal parts.',
        (
        '8 April. Yesterday incapable of writing even one word. Today no better. Who will save me? And the turmoil in me, deep down, scarcely visible; I am like a living lattice-work, a lattice that is solidly planted and would like to tumble down.'
        ),
        (
        'I never wish to be easily defined. I\'d rather float over other people\'s minds as something strictly fluid and non-perceivable; more like a transparent, paradoxically iridescent creature rather than an actual person.'
        ),
        (
        'Don\'t bend; don\'t water it down; don\'t try to make it logical; don\'t edit your own soul according to the fashion. Rather, follow your most intense obsessions mercilessly.'
        ),
        (
        'Youth is happy because it has the capacity to see beauty. Anyone who keeps the ability to see beauty never grows old.'
        ),
        (
        'I write differently from what I speak, I speak differently from what I think, I think differently from the way I ought to think, and so it all proceeds into deepest darkness.'
        ),
        (
        'I am free and that is why I am lost.'
        ),
        (
        'I cannot make you understand. I cannot make anyone understand what is happening inside me. I cannot even explain it to myself.'
        ),
        (
        'I have the true feeling of myself only when I am unbearably unhappy.'
        ),
        (
        'I am constantly trying to communicate something incommunicable, to explain something inexplicable, to tell about something I only feel in my bones and which can only be experienced in those bones.'
        ),
        (
        'I usually solve problems by letting them devour me.'
        ),
        (
        'In a way, you are poetry material; You are full of cloudy subtleties I am willing to spend a lifetime figuring out. Words burst in your essence and you carry their dust in the pores of your ethereal individuality.'
        ),
        (
        'April 27. Incapable of living with people, of speaking. Complete immersion in myself, thinking of myself. Apathetic, witless, fearful. I have nothing to say to anyone - never.'
        ), ]

   response = random.choice(willow)

   embed = discord.Embed(title=(response), color=discord.Color.orange())
   embed.set_image(url=catjson['link'])
   await ctx.send(embed=embed)
        
client.run(TOKEN)