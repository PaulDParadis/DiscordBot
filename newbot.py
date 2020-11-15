#bot.py
import os
import random
from dotenv import load_dotenv

#1
from discord.ext import commands

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# 2
bot = commands.Bot(command_prefix='!')

@bot.command(name='Me')
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

bot.run(token)

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    quotes_from_me = [
        'I am a happy little radish.',
        'Sweet muffins!',
        'Life\'s too short to give a snort.'
    ]

    if message.content == 'Me!':
        response = random.choice(quotes_from_me)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

client.run(token)
