import discord
import random 
import string
from discord.ext import commands
from xml.etree import ElementTree as et
spamming = False 
description = '''A discord bot that is made for spamming, dont use this for evil.'''
bot = commands.Bot(command_prefix='?', description=description)
whitelist = [] 

botinfofile = 'info.xml'
infofile = et.parse(botinfofile)
runnumber = infofile.find('timesran').text
prefix = infofile.find('prefix').text
numberran = int(runnumber) + int(1)
infofile.find('timesran').text = str(numberran)
infofile.write(botinfofile)
print("times ran " + str(numberran))

with open('Whitelist.txt', 'r') as f:
    whitelist = [line.strip() for line in f]


@bot.event 
async def on_ready():
	print("Bot Online!")
	print("Name: {}".format(bot.user.name))
	print("ID: {}".format(bot.user.id))
	await bot.change_presence(game=discord.Game(name=prefix))

@bot.command()
async def spam(ctx : int, strin : str):
	for i in range(ctx):
		await bot.say(string)   
	

@bot.command(pass_context = True)
async def dm(ctx, member : discord.Member, time: int ,content: str):
    timesran = 0
    if member.id in whitelist:
        print("no")
    else:
        await bot.send_message(member, content)
                
def randstring(length):
	global strings
	strings = (random.choice(string.ascii_letters))
	for x in range(length):
		strings += (random.choice(string.ascii_letters))
		
@bot.command(pass_context = True)
async def dmrand(ctx, member : discord.Member, time: int ,length: int):
	time = int(time)
	randstring(length)
	for i in range(time):
		await bot.send_message(member, strings)	
		
			


@bot.command(pass_context = True)
async def helpme(ctx):
    x = 'DM spammer command - ?dm user numberofmessages "texttospam"\n Channel Spam - ?spam number-of-messages "texttospam"\nRandom string spammer command - ?dmrand user numberofmessages length-of-string'
    embed = discord.Embed(title = "List of Commands", description = x, color = 0xFFFFF)
    return await bot.say(embed = embed)
while spamming == True: 
	print("Spamming") 
bot.run('')
