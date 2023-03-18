from dotenv import dotenv_values
from ia.rebecca import Rebecca_ai
from discord.ext import commands
import discord


"""
Information about this file:

created by: Lucas Borges da Silva
date: 02-03-2023
language: Python
libraries: discord.py, dotenv, openai
category: Discord bot
charset: utf-8

"""


# Instance of Rebecca's class
ia = Rebecca_ai()
# Get discord key from .env file
DISCORD_KEY:str = str(dotenv_values(".env")["DISCORD_KEY"])
prefix = "--"
# Create bot instance
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=prefix, intents=intents)

# Command for check if bot is online
@bot.command()
async def ping(ctx):
    await ctx.reply('pong')

# Command for chat with Rebecca using GPT-3.5 
@bot.command()
async def rebecca(ctx):
    await ctx.reply(ia.gpt_chat(ctx.content))

# Command for reset default Rebecca's memory
@bot.command()    
async def resetar_conversa(ctx):
    ia.reset()
    await ctx.reply("Rebecca resetada com sucesso!")

# Dict with commands and functions
all_commands = {
    "ping": ping,
    "rebecca": rebecca,
    "resetar_conversa": resetar_conversa
}

# Function that runs when a message posted in a channel
@bot.event
async def on_message(ctx):
    # Check if message is from bot
    if ctx.author == bot.user:
        return
    # Check if message is a command
    elif ctx.content.startswith(prefix):
        for comm in all_commands:
            # Check if command is valid
            if ctx.content.startswith(prefix + comm):
                # Run command
                await all_commands[comm](ctx)
                return
    
    # If message is not a command, chat with Rebecca
    text = ""
    
    autor = str(ctx.author).split("#")[0]
    
    text = ia.chat(ctx.content, autor)
    # Print message and author in console   
    print(f"{ctx.author}: {ctx.content}")
    # Send message to channel, reply to author without mention
    await ctx.reply(text, mention_author=False)
    print(f"Rebecca: {text}")
    # Run bot commands
    await bot.process_commands(ctx)
    
    
# Run bot
bot.run(DISCORD_KEY)