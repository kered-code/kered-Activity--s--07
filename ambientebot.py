import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='#', intents=intents)

@bot.event
async def on_ready():
    print(f'Bienvenido a este server {bot.user} ,yo soy un bot que te ayudara a cuidar el medio ambiente :)')

@bot.command()
async def sugerencia1(ctx):
    await ctx.send(f'reutiliza los plasticos')

@bot.command()
async def sugerencia2(ctx):
    await ctx.send(f'el vidrio tarda en desintegrarse mas de mil años! no lo tires')

@bot.command()
async def sugerencia3(ctx):
    await ctx.send(f'aqui te dejo un video que te ayudara: https://youtu.be/nvUqnpicSd0?feature=shared ')

@bot.command()
async def sugerencia1(ctx):
    await ctx.send(f'¿porque hay que cuidar el ambiente?: https://youtu.be/aWgHk8Mso0s?feature=shared')

bot.run("")
