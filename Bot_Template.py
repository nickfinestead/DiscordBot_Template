import discord
from discord.ext import commands

intent = discord.Intents.default()
intent.message_content = True
bot = commands.Bot(command_prefix = '.', intents=intent)

        
@bot.command() # Prints out the arguments entered after the command
async def print(ctx, *args):
	response = ""
	for arg in args:
		response = response + " " + arg
	await ctx.channel.send(response)
    
@bot.command() # Prints out "Hi <username>!"
async def hello(ctx):
    await ctx.channel.send(f"Hi {ctx.message.author.mention}!")
    
@bot.command() # Prints out "I am a bot created by @enders#1234 to do minor messages"
async def nick_bot(ctx):
    await ctx.channel.send("I am a bot created by <@!123252467671498752> to do minor messages");


    
bot.run('TOKEN')
