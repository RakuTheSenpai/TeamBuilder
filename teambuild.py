import discord

TOKEN =''
client = discord.Client()

@client.event
async def on_ready():
    print('Bot online. Connected as {0.user}'.format(client))

client.run(TOKEN)