import discord
from discord.ext import commands

TOKEN =''

client = commands.Bot(command_prefix='!')
playerPool = []

@client.command()
async def removeplayer(ctx,arg):
    playerPool.remove(arg)
    await ctx.send('Removed player '+arg)

@client.command()
async def addplayer(ctx,arg):
    playerPool.append(arg)
    await ctx.send('Added player '+arg)

@client.command()
async def showplayers(ctx):
    await ctx.send('Players: '+', '.join(playerPool))

@client.event
async def on_ready():
    print('Bot online. Connected as {0.user}'.format(client))

client.run(TOKEN)



