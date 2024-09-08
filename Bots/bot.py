#!/usr/bin/python3

import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = "sudo ")
client.remove_command("help")

#------+------#
@client.event
async def on_ready():
    print("bot is online: ")

@client.command()
async def ping(ctx):
    await ctx.send("bot is online")

@client.event
async def on_member_join(member):
    channel = client.get_channel()
    await channel.send(f"Welcome: {member.mention} please read , also be sure to assign your self to begin, enjoy your stay!")
    role =  discord.utils.get(member.guild.roles, name="Member")  
    await member.add_roles(role)
    print(f"{member} was given {role}")



@client.command()
async def help (ctx):
     embed = discord.Embed(title = "Help Menu", colour = discord.Color.blue())

     embed.add_field(name="sudo help", value="View this message", inline=False)
     embed.add_field(name="sudo kick", value="Kicks a member out of the server", inline=False)
     embed.add_field(name="sudo ban", value="Bans a member out of the server", inline=False)
     embed.add_field(name="sudo clear", value="Clears messages", inline=False)
     embed.add_field(name="sudo version", value="Shows bot version", inline=False)
     embed.add_field(name="sudo shutdown", value="Shutsdown the bot", inline=False)
     embed.add_field(name="sudo intro", value="Bot gives a little intro :)", inline=False)
     embed.add_field(name="sudo mute", value="Mutes members", inline=False)
     embed.add_field(name="sudo unmute", value="Unmutes members", inline=False)

     await ctx.send(embed=embed)

@client.command()
async def intro(ctx):
    await ctx.send("Hello there  i was created to help automate this server!")


@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member : discord.Member):
    embed = discord.Embed(title = "Member mute ", colour = discord.Color.red())
    await member.add_roles(discord.utils.get(ctx.guild.roles, name="Muted"))
    await ctx.send(f"{member.mention} has been muted")

@client.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, member : discord.Member, *, reason=None):
    embed = discord.Embed(title = "Member Warn ", colour = discord.Color.red())
    embed.add_field(name="User: ", value=f"{member.mention}", inline=False)
    embed.add_field(name="Has been:", value="**Warned!**", inline=False)
    embed.add_field(name="reason:", value=f"{reason}", inline=False)
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member):
    embed = discord.Embed(title = "Member unmute ", colour = discord.Color.blue())
    await member.remove_roles(discord.utils.get(ctx.guild.roles, name="Muted"))
    await ctx.send(f"{member.mention} has been unmuted")

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    embed = discord.Embed(title = "Member kick ", colour = discord.Color.red())
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} has been kicked")
    await ctx.send(f"Reason: {reason}")

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    embed = discord.Embed(title = "Member ban ", colour = discord.Color.red())
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} has been banned")
    await ctx.send(f"Reason: {reason}")

client.run("")
