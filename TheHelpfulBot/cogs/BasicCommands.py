
import discord
import asyncio
from discord.ext import commands


class BasicCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

# BASIC COMMANDS

	@commands.command()
	async def ping(self, ctx):
		await ctx.send(f'Pong: {round(self.bot.latency * 1000)}ms')


	@commands.command()
	async def help(self, ctx):
		embed: discord.Embed = discord.Embed(
				title="Help Menu:", description="---------------------------------------------------------------------", color=discord.Color.dark_theme()
			)
		embed.set_author(name="The Helpful Bot Commands")
		embed.set_thumbnail(url="https://i.ibb.co/6NxdKdT/image-removebg-preview-1.png")
		embed.add_field(name="Basic Commands", value="Info | Help", inline=False)
		embed.add_field(name="Fun Commands", value="CoinFlip | WhoIs [member] | Meme | Avatar [member]", inline=False)
		embed.add_field(name="Other Commands", value="Ping", inline=False)
		embed.add_field(name="For the Mods+", value="Clear [Value] | Kick/Ban | Unban (soon)", inline=False)
		embed.add_field(name="More Info:", value="Do `CMD- info  for more`", inline=False)
		embed.add_field(name="*Prefix is,* 'CMD-***[space]***'", value="---------------------------------------------------------------------", inline=False)
		embed.set_footer(text="Made by Some Guy#2451")
	
		await ctx.send(embed=embed)
		print(f'Help Menu, {ctx.author}')


	@commands.command()
	async def info(self, ctx):
		embed: discord.Embed = discord.Embed(
				title="Information Menu:", description="----------------------------------------------------", color=discord.Color.dark_theme()
			)
		embed.set_author(name="The Helpful Bot Information")
		embed.set_thumbnail(url="https://i.ibb.co/16YT11n/image-removebg-preview-3.png")
		embed.add_field(name="I am constintly working on this bot!", value="Check back soon for what has been released!", inline=False)
		embed.add_field(name="Release Notes:", value="All commands should be case insensitive, \n meaning you can write commands LiKe \n ThIs If YoU wAnT fOr SoMe ReAsOn...", inline=False)
		embed.add_field(name="*Prefix is,* 'CMD-***[space]***'", value="----------------------------------------------------", inline=False)
		embed.set_footer(text="Made by Some Guy#2451")

		await ctx.send(embed=embed)
		print(f'Info Menu, {ctx.author}')

# END OF BASIC COMMANDS

def setup(bot):
	bot.add_cog(BasicCommands(bot))
