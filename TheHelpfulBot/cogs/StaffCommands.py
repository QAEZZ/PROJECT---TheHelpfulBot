
import discord
import asyncio
from discord.ext import commands

class StaffCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

# STAFF COMMANDS

	@commands.command()
	@commands.has_permissions(manage_messages=True)
	async def clear(self, ctx, amount : int):
		await ctx.channel.purge(limit=amount)
		await ctx.send(f'*Message(s) Removed By*  **{ctx.author}**')
		print(f'CLEARED, {amount}, {ctx.author}')

	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member: discord.Member, *, reason="None"):
			await member.ban(reason=reason)
			await ctx.send(f'__User {member.mention} has been BANNED by, {ctx.author.mention} for, {reason}__ \n https://tenor.com/view/troled-locked-away-forever-locked-away-forever-gif-19487068')
			print(f'BANNED {member} by, {ctx.author} for, {reason}')


	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member: discord.Member, *, reason="None"):
			await member.kick(reason=reason)
			await ctx.send(f'__User {member.mention} has been KICKED by, {ctx.author.mention} for, {reason}__ \n https://tenor.com/view/kick-rocks-kicked-out-boot-bye-felicia-go-gif-19829844')
			print(f'KICKED {member} by, {ctx.author} for, {reason}')



# END OF STAFF COMMANDS

def setup(bot):
	bot.add_cog(StaffCommands(bot))
