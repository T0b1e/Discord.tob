"""
Hello my name is Narongkorn kitrungrot,I made this code for entertaning and learning python,If this code doesn't work pls tell me at psuwit.narongkron.nk@gmail.com
Name TOBI version 9.0
python version
"""

import discord
from discord.ext import commands

with open('SECRET.txt') as f:
    info = f.readlines()

client = commands.Bot(command_prefix= info[0])

@client.event
async def on_ready():  # Event client ready
    await client.change_presence(status=discord.Status.idle,activity=discord.Game('=list'))
    print(f'{client.user.name} is online')  # Print TOBI is online
    print('='*50)


def spam(message):
    count = 1
    words = []

    for x in (message.content).split():
        if x in words:
            count += 1
            return True
        
        if x not in words:
            words.append(x)

def nitro(message):
    words = ['Discord Nitro', 'nitro', 'discord nitro', 'free discord nitro', 'free discord', 'free']
    if message.content in words:
        return True
    else:
        return False

@client.event
async def on_message(message):
    if spam(message) == True:
        await message.delete()
    
    if nitro(message) == True:
        await message.delete()


@client.command(description="Gets the bot's latency.")
async def Network(ctx): #Network
    
    latency = round(client.latency * 1000, 1)
    print(f'Network command activated by {ctx.author.name} status {latency} on server {ctx.author.guild.name}')
    await ctx.send(f"Network = {latency}ms")


@client.command()
async def deploy(ctx):
    embed = discord.Embed(title="Status 0.11.1 (2/11/2021)", description="last update 2/11/2021",colour=discord.Color.blue())
    embed.add_field(name="Add", value="Fix some bug math functions")
    embed.add_field(name="Add", value="Add Wikipedia ,weather , covid functions")
    embed.add_field(name="Source code", value="https://github.com/T0b1e/Discord.tob")

    await ctx.send(embed=embed)

@client.event 
async def on_member_join(member): # join
    role = discord.utils.get(member.server.roles,name = 'USERS') 
    await client.add_roles(member, role) #Give user USER role to new member
    print(f'{member} has joined the server.') #TODO


@client.event
async def on_member_remove(member): # remove
    print(f'{member} has removed the server.')


@client.command() # ping pong
async def ping(ctx):
    print(f'Ping command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}') 
    await ctx.send("pong")
    

@client.command() #Kick
async def kick(ctx, member :discord.Member, *,reason = "Kick because you don't follow the rules"):
    print(f'Kick command activated by {ctx.author.name} to {member} on channel {ctx.channel.name} server {ctx.author.guild.name}')
    await member.kick(reason=reason)


@client.command() #Ban
async def ban(ctx, member :discord.Member, *,reason = "Ban because you don't follow the rules"):
    print(f'Ban command activated by {ctx.author.name} to {member} on channel {ctx.channel.name} server {ctx.author.guild.name}')
    await member.ban(reason=reason)


@client.command(description="Mutes the specified user.") #Mute
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member,*, reason=None):
    print(f'Mute command activated by {ctx.author.name} to {member} on channel {ctx.channel.name} server {ctx.author.guild.name}')
    embed = discord.Embed(title = 'Mute command Embed !!!',description =f'We were Mute {member}',Color= discord.Color.red())
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=True, read_message_history=False, read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(embed=embed)


@client.command(description="Mutes the specified user.") #Mute
@commands.has_permissions(manage_messages=True)
async def mutetime(ctx, member: discord.Member,time:int):
    print(f'Mute time command activated by {ctx.author.name} to {member} on channel {ctx.channel.name} server {ctx.author.guild.name}')
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
    print(f'Unmute command activated by {ctx.author.name} to {member} on channel {ctx.channel.name} server {ctx.author.guild.name}')
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"You were unmuted in the server {ctx.guild.name}")


@client.command()  # git
async def git(ctx):
    print(f'Git command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}')
    em = discord.Embed(title = "Github repo", description = "Use '=git'",color = ctx.author.color)
    em.add_field(name = "Github",value="https://github.com/T0b1e/Discord.tob.git")
    await ctx.send(embed = em)

    
client.run(int(info[1], 2).to_bytes((int(info[1], 2).bit_length() + 7) // 8, 'big').decode())