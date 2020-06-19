import discord
from discord.ext import commands
import numpy as np

TOKEN ='YOUR TOKEN GOES HERE'

client = commands.Bot(command_prefix='!')
playerPool = []

def chunkify(players, numberOfTeams:int):
    teams = np.array_split(playerPool,numberOfTeams)
    return teams
    
@client.command()
async def maketeams(ctx, arg):
    teams = chunkify(playerPool,int(arg))
    for i in range(0,len(teams)):
        await ctx.send('Team '+ str(i+1)+': '+', '.join(teams[i]))
    
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
    await ctx.send('Players: '+', '.join(playerPool)if len(playerPool)>0 else 'No players have been added.')

@client.event
async def on_ready():
    print('Bot online. Connected as {0.user}'.format(client))

client.run(TOKEN)



