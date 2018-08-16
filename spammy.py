import discord
import random 
import string
from discord.ext import commands

description = '''A discord bot that is made for spamming, dont use this for evil.'''
bot = commands.Bot(command_prefix='?', description=description)


@bot.event 
async def on_ready():
	print("Bot Online!")
	print("Name: {}".format(bot.user.name))
	print("ID: {}".format(bot.user.id))
	await bot.change_presence(game=discord.Game(name='?helpme'))

@bot.command()
async def spam(ctx : int, strin : str):
	for i in range(ctx):
		await bot.say(string)
		
	

@bot.command(pass_context = True)
async def dm(ctx, member : discord.Member, time: int ,content: str):
    if member.id == "239372371134251008":
        print("no")
    else:
        time = int(time)
        for i in range(time):
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
bot.run('')
