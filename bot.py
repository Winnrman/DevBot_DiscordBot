import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime
from discord import client

client = discord.Client()


load_dotenv()
GUILD = os.getenv('DISCORD_GUILD')
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='~')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to DevServer!!'
    )

@bot.command(name='DevBot', help='DevBot says hi!')
async def hello(ctx):
    responses = [
        'Hi There!',
        'Hello!',
        (
            'Yay! A Friend! :) '
        ),
    ]
    response = random.choice(responses)
    await ctx.send(response)

@bot.command(name='coinFlip', help='Flips a coin')
async def coinflip(ctx):
    options = [
        'Heads!',
        'Tails!'
    ]
    response = random.choice(options)
    await ctx.send(response)

@bot.command(name='time', help="Tells the current time")
async def gettime(ctx):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") + ' AM'
    # print(current_time.split(':')[0])
    if int(current_time.split(':')[0]) > 12:
        # print("Past Noon")
        newHour = int(current_time.split(':')[0]) - 12
        current_time = str(newHour)+":"+str(current_time.split(':')[1])+":"+str(current_time.split(':')[2]) + " PM"
    response = current_time
    await ctx.send(response)

# @bot.command(name='listUsers', help='Lists online users')
# async def userList(ctx):
#     for guild in client.guilds:
#         if guild.name == GUILD:
#             break
#     members = '\n - '.join([member.name for member in guild.members])
#     # print(f'Guild Members:\n - {members}')
    
#     response = members
#     await ctx.send(response)

# @bot.command(name='example_js', help="Gives an example of code from specified language")
# async def display_example(ctx):
#     if command == 'js':
#         example = "```console.log('Hello, World')```"
#     response = example
#     await ctx.send(response)

bot.run(TOKEN)