
import discord
import random 
import asyncio
import time
import os
import sys
import json
from webs import keep_alive

from datetime import datetime
from discord.ext import commands
from discord.ext import tasks
intents = discord.Intents.default()
intents.members = True
bot1 = commands.Bot("1.", intents = intents)
bot2 = commands.Bot("2.", intents = intents)
bot3 = commands.Bot("3.", intents = intents)


async def check():
  while True: 
   #print("check")
   await asyncio.sleep(1) 
  


global userx
userx=int(os.environ.get("userx"))





 
@bot1.event
async def on_ready():
    bot1.loop.create_task(check())
  
   
    print("Bot 1 Systems Booted")
  
    user=await bot1.fetch_user(userx)

    #await channel.send("https://media.discordapp.net/attachments/759148528281845831/801478537567272990/Iron_Legion_Protect_Scene_-_AvengersAge_Of_Ultron_2015_Movie_CLIP_HD.gif")
    await user.send("Legionaire 1 Systems Booted")

@bot3.event
async def on_ready():
    bot3.loop.create_task(check())
  
   
    print("Bot 3 Systems Booted")
  
    user=await bot3.fetch_user(userx)

    
    await user.send("Legionaire 3 Systems Booted")

@bot1.command()
async def ping(ctx):

    await ctx.send((str((bot1.latency*1000))) + "ms")
@bot2.command()
async def ping(ctx):
    await ctx.send((str((bot2.latency*1000))) + "ms")
@bot3.command()
async def ping(ctx):
    await ctx.send((str((bot3.latency*1000))) + "ms")

  


keep_alive()
loop = asyncio.get_event_loop()


TOKEN1=os.environ.get("DISCORD_BOT_SECRET1")
loop.create_task(bot1.start(TOKEN1))
TOKEN2=os.environ.get("DISCORD_BOT_SECRET2")
loop.create_task(bot2.start(TOKEN2))
TOKEN3=os.environ.get("DISCORD_BOT_SECRET3")
loop.create_task(bot3.start(TOKEN3))
loop.run_forever()
