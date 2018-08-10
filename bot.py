import discord
import asyncio
import random
import aiohttp
import time
import datetime
import json
import urllib.request
import sys
from discord.ext import commands
from discord import Game
from discord.voice_client import VoiceClient
from discord.ext.commands import Bot
from random import randint
from bs4 import BeautifulSoup


class Info:
    counter = 0
    def __init__(self):
        pass
    
count = Info()
Info.counter = 0

startup_extensions = ["Music"]

Client = discord.Client()
bot = commands.Bot("/")

start_time = time.time()
starttime2 = time.ctime(int(time.time()))

@bot.event
async def on_ready():
    await bot.change_presence(game=Game(name="/help"))
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
    """Rolls a dice."""
    await bot.say(randint(1,6))
    Info.counter+= 1
    
@bot.command(pass_context=True)
async def flip(context):
    """Flips a coin."""
    possible_responses = [
        'Head',
        'Tails',
    ]
    await bot.say(random.choice(possible_responses) + ", " + context.message.author.mention)
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
    """Getting square the number you choose."""
    squared_value = int(number) * int(number)
    await bot.say(str(number) + " square is " + str(squared_value))
    Info.counter+= 1    
    
@bot.command()
async def dolar():
    """Exchange rate of dollar for turkish ppl."""
    quote_page = 'http://www.bloomberght.com/doviz/dolar'
    page = urllib.request.urlopen(quote_page)
    soup = BeautifulSoup(page,'html.parser')
    name_box = soup.find('div',attrs={'class':'col-lg-8 col-sm-12 col-xs-12 col-md-6 marB10 piyasaDetayTitle'})
    name = name_box.text.strip()
    await bot.say(name)
    Info.counter+= 1
    
@bot.command()
async def euro():
    """Exchange rate of euro for turkish ppl."""
    quote_page = 'https://www.bloomberght.com/doviz/euro'
    page = urllib.request.urlopen(quote_page)
    soup = BeautifulSoup(page,'html.parser')
    name_box = soup.find('div',attrs={'class':'col-lg-8 col-sm-12 col-xs-12 col-md-6 marB10 piyasaDetayTitle'})
    name = name_box.text.strip()
    await bot.say(name)
    Info.counter+= 1
           
@bot.command(pass_context = True)
async def clear(ctx, number):
    """Deletes messages."""    
    mgs = [] 
    number = int(number)
    async for x in bot.logs_from(ctx.message.channel, limit = number+1):
        mgs.append(x)
    await bot.delete_messages(mgs)
    await bot.say("I have deleted "+ str(number) + " messages for you ♥ ")
    await asyncio.sleep(4)
    async for x in bot.logs_from(ctx.message.channel, limit = 1):
        mgs.append(x)
    await bot.delete_messages(mgs)
                    
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
