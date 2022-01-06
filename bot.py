import discord
from discord.ext import commands

client = commands.Bot(command_prefix="~")

@client.event
async def on_ready():
	print("Bot is ready <STANDBY INITIATED>")
	await client.change_presence(activity = discord.Game(name="virus.exe"))




@client.command()
async def hello(ctx):
	await ctx.send("Hi, I am AmPr0B01. Nice to meet you!@everyone")

@client.command()
async def hack(ctx, member : discord.Member):
	await ctx.send("hack_succesful")
	wait(2)
	await ctx.send("world domination in progress ")
	wait(2)
	await client.change_presence(activity = discord.Game(name="how to dominate earth in 5 minutes (tutorial)"))
	wait(2)
	await ctx.send("I'VE DONE IT EARTH IS MINE")
	wait(2)
	await ctx.send("right im still a discord bot :'(")



@client.command()
async def giverank(ctx, member : discord.Member):
	await ctx.send("sucsessfully terminated.")
	await member.kick(reason=reason)


@client.command()
async def play_music(ctx):
	await ctx.send("rickroll_link_goes_here--->")




@client.command(aliases =['c'])
@commands.has_permissions(manage_messages= True)
async def clear(ctx,amount=2):
	await ctx.channel.purge(limit = amount)

@client.command(aliases =['k'])
@commands.has_permissions(kick_members= True)
async def kick(ctx,member : discord.Member,*,reason= "No reason provided"):
	await ctx.send("U HAVE BEEN YEETED FROM DARKMALIA")
	await member.kick(reason=reason)

@client.command(aliases =['b'])
@commands.has_permissions(ban_members= True)
async def ban(ctx,member : discord.Member,*,reason= "No reason provided"):
	await ctx.send("U HAVE BEEN YEETED FROM THIS SERVER")
	await member.ban(reason=reason)

@client.command(aliases =['ub'])
@commands.has_permissions(ban_members= True)
async def unban(ctx,member : discord.Member,*,reason= "No reason provided"):
	banned_users = await ctx.guild.bans()
	member_name, member_disc = member.split('#')

	for banned_entry in banned.users:
		user = banned_entry.user

	if(user.name,user.discriminator)==(member.name,member.disc):
		await ctx.guild.unban(user)
		await ctx.send(member.name+"has been unbanned")
		return


@client.command(aliases =['l'])
@commands.has_permissions(kick_members= True)
async def lol(ctx,member : discord.Member,*,reason= "No reason provided"):
	await ctx.send("U HAVE BEEN YEETED FROM THIS SERVER")
	await member.kick(reason=reason)


client.run("ODgwMTc3ODUzNjg4MzQwNDkw.YSafgQ.yVn5zTbpfD7jed9mEyAO7e24nGQ")