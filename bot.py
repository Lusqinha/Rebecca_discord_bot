from dotenv import dotenv_values
DISCORD_KEY:str = str(dotenv_values(".env")["DISCORD_KEY"])

from ia.rebecca import Rebecca_ai

ia = Rebecca_ai()

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def rebecca(ctx):
    await ctx.send(ia.chat(ctx.message.content))

@bot.command()    
async def becca(ctx):
    await ctx.send(ia.chat(ctx.message.content))
    
    

bot.run(DISCORD_KEY)