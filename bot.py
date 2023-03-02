from dotenv import dotenv_values
from ia.rebecca import Rebecca_ai
from discord.ext import commands
import discord


ia = Rebecca_ai()
DISCORD_KEY:str = str(dotenv_values(".env")["DISCORD_KEY"])
prefix = "--"


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.reply('pong')
    
@bot.command()
async def rebecca(ctx):
    await ctx.reply(ia.chat(ctx.message.content))

@bot.command()    
async def resetar_conversa(ctx):
    ia.reset()
    await ctx.reply("Rebecca resetada com sucesso!")


all_commands = {
    "ping": ping,
    "rebecca": rebecca,
    "resetar_conversa": resetar_conversa,
}

@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return
    elif ctx.content.startswith(prefix):
        for comm in all_commands:
            if ctx.content.startswith(prefix + comm):
                await all_commands[comm](ctx)
                return
    text = ""
    try:
        text = ia.chat(ctx.content)
    except Exception as e:
        ia.reset()
        text = "Não entendi o que você disse, mas vou tentar aprender!"
        print(e)
        
        
    print(f"{ctx.author}: {ctx.content}")
    await ctx.reply(text, mention_author=False)
    await bot.process_commands(ctx)
    
    

bot.run(DISCORD_KEY)