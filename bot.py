import discord
from discord.ext import commands
import os

TOKEN = os.environ["TOKEN"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command(name='enviar')
async def enviar(ctx, *, mensaje: str):
    await ctx.message.delete()
    await ctx.send(mensaje)

bot.run(TOKEN)
