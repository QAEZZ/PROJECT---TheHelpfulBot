# IMPORTS AND SETUP

import discord
import random
import sys
import os
import asyncio
import praw
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle
from random import choice

reddit = praw.Reddit(client_id="idhere",
					 client_secret = "secrethere",
					 username = "usernamehere",
					 password = "passowrdhere",
					 user_agent = "testing",
					 check_for_async=False)


client = commands.Bot(command_prefix = 'CMD- ', case_insensitive=True)
status = cycle(['Prefix', 'is', 'CMD- '])
client.remove_command('help')

@tasks.loop(seconds=3)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_ready():
	change_status.start()
	print('Logged in as {0} ({0.id})'.format(client.user))
	print("----------------------------------------------------------")
	print("Data:\n")
	print(f'discord.py == {discord.__version__}')
	print(f'python == {sys.version}\n')

@client.command()
async def meme(ctx):

	subreddit=reddit.subreddit("memes")
	all_subs=[]

	new=subreddit.new(limit=50)

	for submission in new:
		all_subs.append(submission)

	random_sub=random.choice(all_subs)

	name=random_sub.title
	url=random_sub.url
	embed=discord.Embed(title=name, color=discord.Colour.dark_theme())
	embed.set_image(url=url)
	await ctx.send(embed=embed)



# END OF  IMPORTS AND SETUP 
# -------------------------------------------------------------------------------------------- #
# LOAD | UNLOAD

@client.command()
@commands.has_role('BotKill (DO NOT DELETE FOR ANY REASON WITHOUT ASKING SOME GUY)')
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')
	message = await ctx.send(f'__Loading:__ ``cogs.{extension}``')
	await asyncio.sleep(1)
	await message.edit(content=f'``cogs.{extension}`` __Was Successfully Loaded__')
	print(f'Loaded cogs.{extension}, {ctx.author}')


@client.command()
@commands.has_role('BotKill (DO NOT DELETE FOR ANY REASON WITHOUT ASKING SOME GUY)')
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	message = await ctx.send(f'__Unloading:__ ``cogs.{extension}``')
	await asyncio.sleep(1)
	await message.edit(content=f'``cogs.{extension}`` __Was Successfully Unloaded__')
	print(f'Unloaded cogs.{extension}, {ctx.author}')

@client.command()
@commands.has_role('BotKill (DO NOT DELETE FOR ANY REASON WITHOUT ASKING SOME GUY)')
async def reload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	message = await ctx.send(f'__Reloading:__ ``cogs.{extension}``')
	client.load_extension(f'cogs.{extension}')
	await asyncio.sleep(1)
	await message.edit(content=f'``cogs.{extension}`` __Was Successfully Reloaded__')
	print(f'Reloaded cogs.{extension}, {ctx.author}')

# END OF LOAD | UNLOAD
# -------------------------------------------------------------------------------------------- #
# BOTTOM THINGS

def exit_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)

@client.command()
@commands.has_role('ROLE NAME HERE')
async def kill(ctx):
	await ctx.send(f"**Killing Bot...**\n")
	await asyncio.sleep(1)
	await ctx.send("__Bot Dead, Restart Requested.__ \n ||<@755115465038233630>||")
	print(f'----------KILLED by, {ctx.author}----------')
	exit_program()

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
@commands.has_role('ROLE NAME HERE')
async def displayfile_cogs(ctx):
	for filename in os.listdir('./cogs'):
			await ctx.send(f'``./{filename}``')

@client.command()
@commands.has_role('ROLE NAME HERE')
async def displaydir(ctx):
	for filename in os.listdir('./'):
			await ctx.send(f'``./{filename}``')


client.run("TOKEN HERE")

# END OF BOTTOM THINGS
