import discord
import asyncio
import random
import aiohttp
import time
import datetime
import json
from discord.ext import commands
from discord import Game
from discord.voice_client import VoiceClient
from discord.ext.commands import Bot
from random import randint

class Info:
    counter = 0
    def __init__(self):
        pass
count = Info()
Info.counter = 0

startup_extensions = ["Music"]
Client = discord.Client()
bot = commands.Bot("::")

start_time = time.time()
starttime2 = time.ctime(int(time.time()))

@bot.event
async def on_ready():
    await bot.change_presence(game=Game(name="::commands"))
    print("Logged in as " + bot.user.name)

class Main_Commands():
    def __init__(self, bot):
        self.bot = bot

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

@bot.command(pass_context=True)
async def dice(ctx):
    await bot.say(randint(1,6))
    Info.counter+= 1
    
@bot.command(pass_context=True)
async def flip(context):
    possible_responses = [
        'Head',
        'Tails',
    ]
    await bot.say(random.choice(possible_responses) + ", " + context.message.author.mention)
    Info.counter+= 1
    
@bot.command(pass_context=True)
async def commands(ctx):
    await bot.say(" ::flip \n::dice \n::square \n::uptime  \n::musiccommands   ")   
    Info.counter+= 1

    
@bot.command(pass_context=True)
async def musiccommands(ctx):
    await bot.say("::play \n::volume \n::skip \n::stop \n::playing ")
    Info.counter+= 1

@bot.command()
async def uptime():
    """Displays how long the bot has been online for"""
    second = time.time() - start_time
    minute, second = divmod(second, 60)
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour, 24)
    week, day = divmod(day, 7)
    await bot.say("Bot is online for : %d week, %d day, %d hour, %d minute, %d seconds " % (week, day, hour, minute, second))
    Info.counter+= 1
    
@bot.command()
async def square(number):
    squared_value = int(number) * int(number)
    await bot.say(str(number) + " square is " + str(squared_value))
    Info.counter+= 1

@bot.command()
async def servers():
        print("Servers: ")
        for server in bot.servers:
            print(server.name + "\n")
        await asyncio.sleep(600)

@bot.command()
async def times():
    print(Info.counter)


bot.run("Bot's Token")
