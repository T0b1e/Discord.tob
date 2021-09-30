import discord
from discord.ext import commands,tasks
import time
import os
import json

with open('config.json', 'r') as c:
    data=c.read()

obj = json.loads(data)
key = obj['dict']
prefix = key['prefix']
token = key['token']
client = commands.Bot(command_prefix= str(prefix))#d['prefix']
#os.chdir('C:/Users/asus/Desktop/Udemy/Discord.tob/discord_py')

@client.event
async def on_ready(): #Event client ready
    channel = client.get_channel(880036878038990858) #Get channel id
    await channel.send('TOBI is on ready, Type "=list" to start')
    await client.change_presence(status=discord.Status.idle,activity=discord.Game('=list')) #Change status to =help
    print(f'{client.user.name} is online') #Print TOBI is online

@client.command() #report requested
async def report(ctx, member:discord.Member, message,a :int):
    channel = client.get_channel(873029322288558150)
    em1 = discord.Embed(title = "Report requested", description =f"Admin will discuss about issue by {member} with {message}: level of problem {a}",color = discord.Color.red())
    em4 = discord.Embed(title = "I got Report requested", description =f"About issue made by {member} with {message}: level of problem {a}",color = discord.Color.blue())

    await ctx.send(embed = em1)
    await channel.send(embed = em4)


@client.command() #Kick
async def kick(ctx, member :discord.Member, *,reason = "Kick because you don't follow the rules"):
    await member.kick(reason=reason)

@client.command() #Ban
async def ban(ctx, member :discord.Member, *,reason = "Ban because you don't follow the rules"):
    await member.ban(reason=reason)

@client.command(description="Mutes the specified user.") #Mute
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member,*, reason=None):
    embed = discord.Embed(title = 'Mute command Embed !!!',description =f'We were Mute {member}',Color= discord.Color.red())
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=True, read_message_history=False, read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(embed=embed)
    #await ctx.send(f"Muted {member.mention} for reason {reason}")
    await member.send(f"You were muted in the server {guild.name} for {reason}")

@client.command(description="Mutes the specified user.") #Mute
@commands.has_permissions(manage_messages=True)
async def mutetime(ctx, member: discord.Member,time:int):
    embed = discord.Embed(title = 'Mute command Embed !!!',description =f'We were Mute {member} for {time}',Color= discord.Color.red())
    embed1 = discord.Embed(title = 'Mute command Embed !!!',description =f'We were unMute {member}',Color= discord.Color.green())
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    
    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=True, read_message_history=False, read_messages=False)

    await member.add_roles(mutedRole)
    x = time
    y = 0
    timer = 1
    for y in range(time):
        print(timer)
        time.sleep(1)
        timer = y + 1
        if timer == x - 1 :
            await member.remove_roles(mutedRole)
            await ctx.send(f"Unmuted {member.mention}")
            await member.send(f"You were unmuted in the server {guild.name} for {time}")
            await ctx.send(embed = embed1)
    await ctx.send(embed=embed)
    await member.send(f"You were muted in the server {guild.name} for {time}")

@client.command(description="Unmutes a specified user.") #Unmute
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"You were unmuted in the server {ctx.guild.name}")

client.run(str(token))