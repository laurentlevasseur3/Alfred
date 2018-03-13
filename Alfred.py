#Alfred Bot
import discord
import asyncio
import random
import json
from discord.ext import commands
from discord.ext.commands import Bot

token = "<Insert Token Here>"
bot = commands.Bot(command_prefix = "Alfred, ")

@bot.command(pass_context = True)
async def hey(ctx):
    await bot.say("Greetings, sir")

@bot.command(hidden=True)
async def mimic(ctx, message):
    if ctx.author.id == (<My Token>):
        channel = bot.get_channel(<Channel Token>)
        await channel.send(message)

@bot.command(pass_context = True)
async def rolldice(ctx, faces):
    await bot.say(random.randint(0, int(faces)))

@bot.command(pass_context = True)
async def thanks(ctx):
    await bot.say("Anytime, sir")

@bot.command(pass_context = True)
async def getIQ(ctx):
    await bot.say(random.randint(0, 200))

@bot.command(pass_context = True)
async def hellohashi(ctx):
    await bot.say("::hellohashi")

@bot.command(pass_context = True)
async def gideonIQ(ctx):
    await bot.say(4)
    
@bot.command(pass_context = True)
async def Gideon(ctx):
    await bot.say("https://lh3.googleusercontent.com/-JfWuy5MBQ68/WqROWoHlatI/AAAAAAAAD2A/BPMGXYrTu-M5AG8obF2zhgoC_632qfO5gCL0BGAYYCw/h640/f1b22902-9c50-4da2-adfd-a3a40bf80690")
    
bot.run(token)
