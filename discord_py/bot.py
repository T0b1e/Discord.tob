"""
Hello my name is Narongkorn kitrungrot,I made this code for entertaning and learning python,If this code doesn't work pls tell me at psuwit.narongkron.nk@gmail.com
Name TOBI version 0.8.5
python version
"""

from asyncio.tasks import sleep
import discord
from discord import colour
from discord.colour import Color
from discord.ext import commands,tasks

from discord.player import FFmpegPCMAudio
from discord.utils import get
import asyncio #gacha
import youtube_dl #play url
import os #play os
import psutil

from datetime import datetime

#import datetime #set time
import time #Class,Count
import calendar #Class
import requests
import random #gacha prize
import math

import webbrowser
import json

from discord_components.client import DiscordComponents
from discord_components import *
client = commands.Bot(command_prefix= '=')


@client.event
async def on_ready(): #Event client ready
    channel = client.get_channel(880036878038990858) #Get channel id
    await channel.send('TOBI is on ready, Type "=list" to start')
    await client.change_presence(status=discord.Status.idle,activity=discord.Game('=help')) #Change status to =help
    print(f'{client.user.name} is online') #Print TOBI is online
    DiscordComponents(client) #Get lib name discord component

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
    "**bomb**           for delete message in channel\n")
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
    "**vote**           for vote member when Vote was started\n")
    embed.add_field(name= "Tobi",value=
    "**tobiinfo**       for TOBI information\n"
    "**git**            for GitHub\n"
    "**updateinfo**     for TOBI update command or function\n")
    await ctx.send(embed = embed)

@client.command(description="Gets the bot's latency.")
async def Network(ctx): #Network
    print(ctx)
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

@client.command() # ping pong
async def ping(ctx):
    await ctx.send("pong")

@client.command()
async def temp(ctx):
        CPULOARD= psutil.cpu_percent()
        await ctx.send(f"{CPULOARD} %")

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
async def weather(ctx,city:str):
    city = city
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
    
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C" 
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    await ctx.send(final_info)
    await ctx.send(final_data)

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
        sleep(1)
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

@client.command(invoke_without_command = True) #tobiinfo
async def tobiinfo(ctx):
    em = discord.Embed(title = "TOBI information.json", description = "Use '=tobiinfo'",color = ctx.author.color)
    em.add_field(name = "Info",value=
    "Build by Mr. Narongkorn kitrungrot\n"
    "Version 0.8.1 (25/8/2021)\n"
    "Born 12/7/2020\n"
    "Discordbot.js © TOB · Narongkorn,Hosted by TOB Raspberrypi, distributed under the PSUWIT license")
    em.add_field(name='Supporter',value='https://ko-fi.com/narongkorn')
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
async def button(ctx):
    await ctx.send(
        "Test Button",
        components =[
            Button(label='Click me',style=ButtonStyle.blue)
        ]
    )
    res = await client.wait_for('button_click', check=lambda i: i.component.label.startswith("Click"))
    await res.respond(content='button clicked')

@client.command()
async def voting(ctx):
    await ctx.send(
        f"Voting System Start",
        components =[
            Button(label= 'Agree' ,style=ButtonStyle.blue),
            Button(label= 'Disagree' ,style=ButtonStyle.red),
            Button(label= 'No vote' ,style=ButtonStyle.green)
        ]
    )
    res = await client.wait_for('button_click', check=lambda i: i.component.label.startswith("Click"))
    await res.respond(content='button clicked')
    res = await client.wait_for('button_click', check=lambda i: i.component.label.startswith("Click"))
    await res.respond(content='button clicked')
    res = await client.wait_for('button_click', check=lambda i: i.component.label.startswith("Click"))
    await res.respond(content='button clicked')
    
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

@client.command()
async def volume(ctx, volume: int):
    if volume < 0:
           print('To Low')

    if volume > 150:
            print('To High')
    msg = await ctx.send(f"Volume set to {volume:,}%")
    await msg.add_reaction('🔊')

@client.command() #play
async def play(ctx, url : str):
    embed_play = discord.Embed(title = f'Play {url}',description = 'Playing music in queue',color = ctx.author.color)
    msg = await ctx.send(embed = embed_play)
    await msg.add_reaction('🎶')
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
    embed_pause = discord.Embed(title = f'pause  song',description = 'Playing music in queue',color = ctx.author.color)
    msg = await ctx.send(embed = embed_pause)
    await msg.add_reaction('🔇')
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
        #await ctx.send("**pause**")
    else:
        await ctx.send("Currently no audio is playing.")

@client.command() #resume
async def resume(ctx):
    embed_resume = discord.Embed(title = f'Resume the song song',description = 'Playing music in queue',color = ctx.author.color)
    msg = await ctx.send(embed = embed_resume)
    await msg.add_reaction('🔉')
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
        #await ctx.send("**resume**")
    else:
        await ctx.send("The audio is not paused.")

@client.command() #stop
async def stop(ctx):
    embed_stop = discord.Embed(title = 'Stop song',description = 'Stop playing music in queue',color = ctx.author.color)
    msg = await ctx.send(embed = embed_stop)
    await msg.add_reaction('🔴')
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    
client.run('ODMzMjgwODM0MTYwOTUxMjk2.YHwDQA.ufiVDV9KSiUVpLswC4O9MuMbHro')
#ODMzMjgwODM0MTYwOTUxMjk2.YHwDQA.e0I1pWWRE3rUZwka7C8jPayiHgA