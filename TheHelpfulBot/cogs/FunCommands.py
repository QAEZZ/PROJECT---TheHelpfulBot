
import discord
import asyncio
import random
from discord.ext import commands
from random import choice

Coin_Flip = ['Heads', 'Tails']

class FunCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

# FUN COMMANDS

	@commands.command()
	async def whois(self, ctx, member : discord.Member):
		embed = discord.Embed(
		title = f"WhoIs Info:\n{member.name}" , description = f"{member.mention}" , color=discord.Colour.dark_theme()
  			)
		embed.add_field(name='User ID:', value=f"{member.id}", inline = True)
		embed.set_thumbnail(url=member.avatar_url)
		embed.add_field(name='Top Role: ', value=f"{member.top_role.mention}")
		embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
		await ctx.send(embed=embed)
		print(f'WhoIs {member} by, {ctx.author}')


	@commands.command()
	async def coinflip(self, ctx):
		embed: discord.Embed = discord.Embed(
				title="Flip a Coin!", description="--------------", color=discord.Color.dark_theme()
			)
		embed.set_author(name=" ")
		embed.set_thumbnail(url="https://i.ibb.co/cXhLLjP/coin-flip.gif")
		embed.add_field(name="Side:", value=f"{random.choice(Coin_Flip)}", inline=True)
		embed.set_footer(text="Made by Some Guy#2451")
	
		await ctx.send(embed=embed)
		print(f'Coin Flip, {ctx.author}')


	@commands.command(aliases=['pfp'])
	async def avatar(self, ctx, member : discord.Member):
		embed: discord.Embed = discord.Embed(color=discord.Color.dark_theme())
		embed.set_image(url=f"{member.avatar_url}")
		embed.set_footer(icon_url=f"{ctx.author.avatar_url}", text=f"Requested by {ctx.author}")
		await ctx.send(embed=embed)

# END OF FUN COMMANDS

def setup(bot):
	bot.add_cog(FunCommands(bot))
