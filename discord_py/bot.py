"""
Hello my name is Narongkorn kitrungrot,I made this code for entertaning and learning python,If this code doesn't work pls tell me at psuwit.narongkron.nk@gmail.com
Name TOBI version 0.8.1
python version
"""

import discord
from discord.ext import commands,tasks

from discord.player import FFmpegPCMAudio
from discord.utils import get
import asyncio #gacha
import youtube_dl #play url
import os #play os

from datetime import datetime
import datetime as dt
#import datetime #set time
import time #Class,Count
from time import sleep
import calendar #Class

import random #gacha prize
import math

import webbrowser
import json

from discord_components.client import DiscordComponents
from discord_components import *

client = commands.Bot(command_prefix= '=')
DiscordComponents(client) #Get lib name discord component

@client.event
async def on_ready(): #Event client ready
    channel = client.get_channel(880036878038990858) #Get channel id
    await channel.send('TOBI is on ready, Type "=list" to start')
    await client.change_presence(status=discord.Status.idle,activity=discord.Game('=help')) #Change status to =help
    print(f'{client.user.name} is online') #Print TOBI is online
   

@client.command() #list commands
async def list(ctx): #Contact list word
    embed = discord.Embed(title = "List commands", description = "Use '=list'",color = ctx.author.color)
    embed.add_field(name = "Basic",value=
    "TOBI but in json file\n"
    "**Network**        for Check TOBI Network (.ms)\n"
    "**userinfo**       for Check user information (Join server, Role)\n"
    "**gacha _ _**      for random number from fisrt to second\n"
    "**prize _ _**      for Give away prize from Admin by set time and prize\n"
    "**poll**           for vote Good or Bad (No limit user)\n"
    "**spawn**          for spawn TOBI to channel\n"
    "**bomb**           for delete message in channel\n"
    "**attack**          for attack someone by disconnect,move member\n")
    embed.add_field(name= "Report",value=
    "**report**         for report User by Issue to Admin to discuss and Vote\n")
    embed.add_field(name= "Math",value=
    "**plus _ _**       for plus the numbers\n"
    "**minus _ _**      for minus the numbers\n"
    "**multiplie _ _**  for multiplie the numbers\n"
    "**divide __**      for divide the numbers\n"
    "**sqrt __**        for Square root the numbers\n"
    "**expo __**        for exponent the numbers\n"
    "**fac __**        for factorial the numbers\n"
    "**Q = mcΔt**       for calculate the numbers\n")
    embed.add_field(name= "Audio",value=
    "**play 'url'**     for play song\n"
    "**stop**           for stop song\n"
    "**pause**          for pause song\n"
    "**resume**         for resume song\n" )
    embed.add_field(name= "ADMIN",value=
    "only Admin or mod can acess this permission\n"
    "**mute @___**      for muted someone\n"
    "**unmute @___**    for unmuted someone\n"
    "**kick @___**      for kick someone from the server\n"
    "**ban @___**       for ban someone from the server\n"
    "**banvote**        for ban Someone but use Vote from Admin\n"
    "**mutevote**       for mute Someone but use Vote from Admin\n"
    "**kickvote**       for kick Someone but use Vote from Admin\n"
    "**vote**           for vote member when Vote was started\n")
    embed.add_field(name= "Tobi",value=
    "**tobiinfo**       for TOBI information\n"
    "**git**            for GitHub\n"
    "**updateinfo**     for TOBI update command or function\n")
    await ctx.send(embed = embed)

@client.command(description="Gets the bot's latency.")
async def Network(ctx): #Network
    latency = round(client.latency * 1000, 1)
    await ctx.send(f"Network = {latency}ms")

@client.event 
async def on_member_join(member): # join
    role = discord.utils.get(member.server.roles,name = 'USERS') 
    await client.add_roles(member, role) #Give user USER role to new member
    print(f'{member} has joined the server.') #TODO
   
@client.event
async def on_member_remove(member): # remove
    print(f'{member} has removed the server.')

client.event
async def on_message(message):
    with open('users.json','r') as f:
        users = json.load(f)

    await update_data(users, message.author)
    await add_experience(users,  message.author, 5)
    await level_up(users,  message.author, message.channel)

    with open('users.json','w') as f:
        json.dump(users, f)

async def update_data(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]["experience"] = 0
        users[user.id]["level"] = 1

async def add_experience(users, user, exp):
        users[user.id]["experience"] += exp

async def level_up(users, user, channel):
        experience = users[user.id]["experience"]
        level_start = users[user.id]['level']
        level_End = int(experience ** 1/4)

        if level_start < level_End:
            await client.send_message(channel, '{} has leveled up to {} '.format(user.mention,level_End))
            await client.send_message('Congratulation Mr.{user.mention}')
            users[user.id]["level"] = level_End

@client.command() #userinfo
async def userinfo(ctx, member:discord.Member):
    roles = [role for role in member.roles]
    embed = discord.Embed(title = f"Userinfo{member.name}",color = ctx.author.color)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")
    embed.add_field(name="Joined Server",value= member.joined_at.strftime('%d.%m.%y and %H hr.:%M m'))
    embed.add_field(name=f"Role({len(roles)})" ,value=" ".join([role.mention for role in roles]))
    await ctx.send(embed=embed)

@tasks.loop(seconds=2)
async def change_status():
    channel = client.get_channel(875074992902131772)
    await channel.send('here')

@client.command() # ping pong
async def ping(ctx):
    await ctx.send("pong")
 
@client.command() # plus _ _
async def plus(ctx,a: float,b: float):
    if a < 50000 and b < 50000:
        ans = a + b
        await ctx.send(f'Answer from {str(a)} + {str(b)} is {ans}')
    else:
        await ctx.send('To much Integer,Try less than 50,000')
@client.command() # minus _ _
async def minus(ctx,a: float,b: float):
    if a < 50000 and b < 50000:
        ans = a - b
        await ctx.send(f'Answer from {str(a)} - {str(b)} is {ans}')
    else:
        await ctx.send('To much Integer,Try less than 50,000')

@client.command() # multiplie _ _
async def multiplie(ctx,a: float,b: float):
    if a < 50000 and b < 50000:
        ans = a * b
        await ctx.send(f'Answer from {str(a)} * {str(b)} is {ans}')
    else:
        await ctx.send('To much Integer,Try less than 50,000')

@client.command() # multiplie _ _
async def divide(ctx,a: float,b: float):
    if b == 0:
        await ctx.send('None')
    if a < 50000 and b < 50000:
        ans = a / b
        await ctx.send(f'Answer from {str(a)} / {str(b)} is {ans}')
    else:
        await ctx.send('To much Integer,Try less than 50,000')

@client.command() # sqrt
async def sqrt(ctx,a: float):
    if a < 50000:
        ans = math.sqrt(a)
        await ctx.send(f'Answer from sqrt{str(a)} is {ans}')
    else:
        await ctx.send('To much Integer,Try less than 50,000')

@client.command() # sqrt
async def expo(ctx,a: int,b: int):
    if  0 > a < 50000 and 0 > b < 50000:
        ans = a ** b
        await ctx.send(f'Answer from {str(a)} ^ {str(b)} is {ans}')
    else:
        await ctx.send('To much Integer,Try less than 50,000')

@client.command() # factorial
async def fac(ctx,a: int):
    if a < 50000:
        ans = math.factorial(a)
        await ctx.send(f'Answer from factorail{str(a)} is {ans}')
    else:
        await ctx.send('To much Integer,Try less than 50,000')
  

@client.command() #Q = mcΔt
async def Q(ctx,m: float,c: float,t1: float,t2: float):
        await ctx.send(m*c*(t2-t1))

@client.command()
async def attack(ctx, member:discord.Member):
    
    skill = ["mute","ban","bomb"]
    finalskill = random.choice(skill)
    if finalskill == "mute":
        mute()
        await ctx.send("muted commnad")
    elif finalskill == "ban":
        ban()
        await ctx.send("ban commnad")
    else:
         await ctx.send("U Miss lol")

@client.command() #clear message count command text
async def bomb(ctx,Time:int):#
    x = Time
    if Time > 120:
        await ctx.send('Calm down bro Limit of bomb is 120')
    elif Time <= 1:
        await ctx.send('Just 1 more')
    for y in range(Time):
        time.sleep(1)
        timer = y + 1
        await ctx.send(timer) 
        if timer == Time:
            await ctx.channel.purge(limit= (x ** 2) + 10)

@client.command() #report requested
async def report(ctx, member:discord.Member, message,a :int):
    channel = client.get_channel(873029322288558150)
    em1 = discord.Embed(title = "Report requested", description =f"Admin will discuss about issue by {member} with {message}: level of problem {a}",color = discord.Color.red())
    em4 = discord.Embed(title = "I got Report requested", description =f"About issue made by {member} with {message}: level of problem {a}",color = discord.Color.blue())

    await ctx.send(embed = em1)
    await channel.send(embed = em4)

    #if report requested is more than 10 people and User vote is for vote for problem.

@client.command() #Kick
async def kick(ctx, member :discord.Member, *,reason = "Kick because you don't follow the rules"):
    await member.kick(reason=reason)

@client.command() #Ban
async def ban(ctx, member :discord.Member, *,reason = "Ban because you don't follow the rules"):
    await member.ban(reason=reason)

@client.command(description="Mutes the specified user.") #Mute
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member,*, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=True, read_message_history=False, read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Muted {member.mention} for reason {reason}")
    await member.send(f"You were muted in the server {guild.name} for {reason}")

@client.command(description="Unmutes a specified user.") #Unmute
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"You were unmuted in the server {ctx.guild.name}")

@client.command(invoke_without_command = True) #tobiinfo
async def tobiinfo(ctx):
    em = discord.Embed(title = "TOBI information.json", description = "Use '=tobiinfo'",color = ctx.author.color)
    em.add_field(name = "Info",value=
    "Build by Mr. Narongkorn kitrungrot\n"
    "Version 0.8.1 (25/8/2021)\n"
    "Born 12/7/2020\n"
    "Discordbot.js © TOB · Narongkorn,Hosted by TOB Raspberrypi, distributed under the PSUWIT license")
    em.add_field(name='Report reqest',value='https://forms.gle/2yhJfcPBpTbmWsFbA')
    await ctx.send(embed = em)

@client.command() #git
async def git(ctx):
    em = discord.Embed(title = "Github repo", description = "Use '=git'",color = ctx.author.color)
    em.add_field(name = "Github",value="https://github.com/T0b1e/Discord.tob.git")
    await ctx.send(embed = em)

@client.command() #poll
async def poll(ctx,*,message):
    em = discord.Embed(title = "Vote", description = f"{message}",color = ctx.author.color)
    em.add_field(name = "Poll",value="I vote bote of them so it will count 1 first")
    msg = await ctx.channel.send(embed=em)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    x = len(message.reactions)
    print(x)

@client.command() #Vote
async def vote(ctx, member :discord.Member):
    await ctx.send(f"Recieve Vote {member}")
    time.sleep(10)
    await ctx.channel.purge(limit=2)

@client.command()
async def butt(self,ctx):
    await ctx.channel.send(
        "Test Button",
        component=[
            Button(style=ButtonStyle.blue,label=['Click me'])
        ]
    )
    res = await self.client.wait_for('Button_click')
    if res.channel == ctx.channel:
        await res.respond(
            type=InteractionType.ChannelMessageWithSource,
            content=f'{res.component.label}clicked'
        )

@client.command() #gacha+time
async def prize(ctx, mins :int, *,prize :str):
      embed = discord.Embed(title = "Gacha", description = f"{prize}",color = ctx.author.color)
      end = datetime.datetime.utcnow() + datetime.timedelta(seconds= mins * 60)
      embed.add_field(name=" End time :",value= f"{end} UTC")
      embed.set_footer(text=" Countdown {mins} minutes from now")
      msg = await ctx.send(embed = embed)
      await asyncio.sleep(mins*60)

      new_msg = await ctx.channel.fetch_message(msg.id)
      user = await new_msg.reaction[0].users().flatten()
      user.pop(user.index(client.user))
      winner = random.choice(user)
      await ctx.send(f"Congratulation to {winner.mention} won")

@client.command(pass_context = True) #gacha number
async def gacha(ctx, num1:int ,num2:int):
    if num1 < 100 and num2 <100:
        embed = discord.Embed(title = "Gacha", description = (random.randint(num1,num2)),color = ctx.author.color)
        await ctx.send(embed = embed)
    else:
        await ctx.send('To much number,Try less than 100')

@client.command() #Special command
async def gacha_group(ctx):
    person = ["Tob","Petch","Spy","PP","John","Paul","Pooh"]
    x = 0
    for x in range (10):
        lucky = random.choice(person)
    await ctx.send(f'lucky person is {lucky}')

@client.command(pass_context = True) #spawn
async def spawn(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("you're not in the voice channel")

@client.command() #play
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return
        
    channel = ctx.message.author.voice.channel
    print(channel)
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name= str(channel))#Finish
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@client.command() #leave
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command() #pause
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
        #await ctx.send("**pause**")
    else:
        await ctx.send("Currently no audio is playing.")

@client.command() #resume
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
        #await ctx.send("**resume**")
    else:
        await ctx.send("The audio is not paused.")

@client.command() #stop
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    #await ctx.send("**stop**") 
client.run('ODMzMjgwODM0MTYwOTUxMjk2.YHwDQA.ufiVDV9KSiUVpLswC4O9MuMbHro')
#ODMzMjgwODM0MTYwOTUxMjk2.YHwDQA.e0I1pWWRE3rUZwka7C8jPayiHgA