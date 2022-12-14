import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):''
    if message.content.startswith('bruh'):
        channel = message.channel
        await channel.send('brah')

client = discord.Client(activity=discord.Game('Beep Boop'))