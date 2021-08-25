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

os.chdir(r'C:\Users\asus\Desktop\Udemy\Discord.tob\discord_py') #BUG
client = commands.Bot(command_prefix= '=')
client.remove_command("help")

#Cogs
""" @client.command()
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}') #cut .py 3 char """


@client.event
async def on_ready(): #Event client ready
    channel = client.get_channel(843680768835190796) #Get channel id
    await channel.send('TOBI is on ready, Type "=list" to start')
    """now = dt.datetime.now()
    birthday = dt.datetime(year=2022, month=1, day=12,)
    count = birthday - now
    await client.change_presence(status=discord.Status.idle,activity=discord.Game(f'Count down {count}'))"""
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
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, member) 

    with open('users.json', 'w') as f:
        json.dump(users, f)

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
async def plus(ctx, a: float, b: float):
    await ctx.send(a + b)

@client.command() # minus _ _
async def minus(ctx, a: float, b: float):
    await ctx.send(a - b)

@client.command() # multiplie _ _
async def multiplie(ctx,a: float,b: float):
    await ctx.send(a * b)

@client.command() # multiplie _ _
async def divide(ctx,a: float,b: float):
    await ctx.send(a / b)

@client.command() # sqrt
async def sqrt(ctx,a: float):
        await ctx.send(math.sqrt(a))

@client.command() # sqrt
async def expo(ctx,a: int,b: int):
        await ctx.send(a**b)

@client.command() # factorial
async def fac(ctx,a: int):
        await ctx.send(math.factorial(a))

@client.command() #Q = mcΔt
async def Q(ctx,m: float,c: float,t1: float,t2: float):
        await ctx.send(m*c*(t2-t1))

@client.command() #Q = mcΔt
async def typeof(ctx,message):
        x = typeof(message)
        await ctx.send(x)


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
    #await ctx.send(finalskill)
    #await ctx.send(f'attacked {member.mention} by {skill} ')

@client.command() #clear message count command text
async def bomb(ctx,Time:int):#
    x = Time
    while Time > 0:
        m, s = divmod(Time,60)
        h, m = divmod(m, 60)
        timeleft = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
        await ctx.send(timeleft)#+ "\r", end=""
        time.sleep(1)
        Time -= 1
        text = 10 + int(s)
        if(timeleft == "00:00:01"):
           await ctx.channel.purge(limit=(x + 1)*2)#channel.purge(limit=amount)

@client.command() #disconnect user
async def shoot(ctx,member:discord.Member):
    if member.is_connected():
        await member.disconnect()
    else:
        await ctx.send("This guys not in channel")

@client.command() #report requested
async def report(ctx, member:discord.Member, message,a :int):
    channel = client.get_channel(873029322288558150)
    em1 = discord.Embed(title = "Report requested", description =f"Admin will discuss about issue by {member} with {message}: level of problem {a}",color = discord.Color.red())
    em4 = discord.Embed(title = "I got Report requested", description =f"About issue made by {member} with {message}: level of problem {a}",color = discord.Color.blue())

    await ctx.send(embed = em1)
    await channel.send(embed = em4)

    #if report requested is more than 10 people and User vote is for vote for problem.

#def reportrequest():
@client.command()
async def jsons(ctx):
    with open('report.json') as f:
        await ctx.send("pass")

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
    "Version 0.5.1 (5/8/2021)\n"
    "Born 12/7/2020\n"
    "Discordbot.js © TOB · Narongkorn,Hosted by TOB Raspberrypi, distributed under the PSUWIT license")
    em.add_field(name='Report reqest',value='https://forms.gle/2yhJfcPBpTbmWsFbA')
    await ctx.send(embed = em)

@client.command(invoke_without_command = True) #updateinfo
async def updateinfo(ctx):
    em = discord.Embed(title = "TOBI Update information", description = "Use '=updateinfo'",color = ctx.author.color)
    em.add_field(name = "Info",value=
    "**Prefix change from / to = **\n"
    "**Spawn**\n"
    "**Music command** = play,stop,pause,resume\n"
    "**Calculater Mode** = plus,minus,multiplie,divide\n"
    "**Member cout**\n"
    "**UserInfo**\n"
    "**Voting, Poll** \n"
    "**Gacha** = number,member\n"
    "**Mute** = mute,unmute\n"
    "**Coming soon** function = queue, skip, Homework notification, Uptime Classroom")
    em.set_footer(text="Version 0.5.1 (5/8/2021)")
    await ctx.send(embed = em)

@client.group(invoke_without_command = True) #help
async def command(ctx):
    em = discord.Embed(title = "Help", description = "Use '=help <command>'",color = ctx.author.color)
    em.add_field(name = "Calculator",value="plus, minus, multiplie,divide")
    em.add_field(name = "Music",value="play, stop, pause, resume, leave")
    em.add_field(name = "Gacha",value= "Gacha _ _, Gacham")
    em.add_field(name = "Basic Command",value= "userinfo")
    em.add_field(name = "Bot", value= "tobiinfo, updateinfo")
    await ctx.send(embed = em)

@client.command() #helpplus
async def helpplus(ctx):
    em = discord.Embed(title = "plus", description = "Use '=plus <Number>_<Number>'",color = ctx.author.color)
    await ctx.send(embed = em)

@client.command() #git
async def git(ctx):
    em = discord.Embed(title = "Github repo", description = "Use '=git'",color = ctx.author.color)
    em.add_field(name = "Github",value="https://github.com/T0b1e/Discord.tob.git")
    await ctx.send(embed = em)

@client.command() # Knock Knock
async def knock(ctx,knock:str):
    await ctx.send("who r u?")

@client.command() #poll
async def poll(ctx,*,message):
    em = discord.Embed(title = "Vote", description = f"{message}",color = ctx.author.color)
    em.add_field(name = "Poll",value="I vote bote of them so it will count 1 first")
    msg = await ctx.channel.send(embed=em)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    x = len(message.reactions)
    print(x)
    
@client.command() #Vote for ban
async def mutevote(ctx, member :discord.Member):
    Yes =   '👍'
    No =    '👎'
    embed = discord.Embed(title = f"Vote for mute {member} ", description = f"If vote has like more than 10 TOBI will mute {member} forever",color = ctx.author.color)
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    print(len(Yes)) #BUG

@client.command() #Vote
async def vote(ctx, member :discord.Member):
    await ctx.send(f"Recieve Vote {member}")
    time.sleep(10)
    await ctx.channel.purge(limit=2)

@client.command() #Vote for ban
async def banvote(ctx, member :discord.Member,message):
    Yes = True
    No = False
    embed = discord.Embed(title = "Vote for ban", description = f"{message}",color = ctx.author.color)
    embed.add_field(name = "Vote (Majority vote)",value="for justice")
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction(Yes)
    await msg.add_reaction(No)
    if Yes > 10:
        await member.ban
    if No > Yes:
         await ctx.send("You're free now")

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
    embed = discord.Embed(title = "Gacha", description = (random.randint(num1,num2)),color = ctx.author.color)
    await ctx.send(embed = embed)

@client.command() #Special command
async def gacha_group(ctx):
    person = ["Tob","Petch","Spy","PP","John","Paul","Pooh"]
    x = 0
    for x in range (10):
        lucky = random.choice(person)
    #final = len(lucky) > person/2
    #final = split(lucky)
    await ctx.send(f'lucky person is {lucky}')
    #print(lucky)

@client.command(pass_context = True) #spawn
async def spawn(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("you're not in the voice channel")
        
@client.command(pass_context = True) #join
async def lofi(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('samurai-japanese-lofi-hiphop-mix.mp3')
        player = voice.play(source)
    else:
        await ctx.send("you're not in the voice channel")

#Chem Bio Phy Math Maths Math+ Socio His Thai Eng Empty Tcas Ondemand Gym
@client.command() #join
async def time(ctx):
    Now = dt.datetime.now()
    day = Now.strftime('%A')
    hour = Now.strftime('%H')
    minutes = Now.strftime('%M')
    seconds = Now.strftime('%S')
    today = day,hour,minutes,seconds
    await ctx.send(today)

@client.command() #play
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    """if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("you're not in the voice channel")"""
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