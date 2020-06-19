import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Bot online. Connected as {0.user}'.format(client))

client.run('NzIzNjA1NDA1NTc3NjQyMDI0.Xu0ExQ.RgmHz8c99i5o8ZJ_DuQbzM-wDbw')