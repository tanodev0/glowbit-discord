import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Cargar variables de .env
load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} está conectado y listo!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! Latencia: {round(bot.latency * 1000)}ms')
    
bot.run(str(TOKEN))