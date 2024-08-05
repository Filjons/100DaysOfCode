# This example requires the 'message_content' intent.
# Login token for RainMan: MTI2MTc0NzY0MzM0NTAxMDg1MA.G7GQ0G.1VZLG1ek1JKNHf51QHz54treOYVN7It9hIz7ig

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

client.run('MTI2MTc0NzY0MzM0NTAxMDg1MA.G7GQ0G.1VZLG1ek1JKNHf51QHz54treOYVN7It9hIz7ig')
