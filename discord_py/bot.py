"""
Hello my name is Narongkorn kitrungrot,I made this code for entertaning and learning python,If this code doesn't work pls tell me at psuwit.narongkron.nk@gmail.com
Name TOBI version 0.8.5
python version
"""

from asyncio.tasks import sleep
import discord
from discord import colour
from discord import user
from discord import message
from discord.colour import Color
from discord.embeds import Embed
from discord.ext import commands, tasks

from discord.player import FFmpegPCMAudio
from discord.utils import get
import asyncio  # gacha
import youtube_dl  # play url
import os  # play os
import psutil

from datetime import datetime

# import datetime #set time
import time  # Class,Count
import requests
import random  # gacha prize
import math

import numpy as np
from numpy import random
from numpy import *
import matplotlib.pyplot as plt

import json
import wikipedia

from discord_components.client import DiscordComponents
from discord_components import *


'''
!!! Module isn't working try 29/9
import Maths
import Admin
Maths()
Admin()
'''
with open('config.json') as c:
    data = c.read()

obj = json.loads(data)
key = obj['dict']
prefix = key['prefix']
token = key['token']

client = commands.Bot(command_prefix= str(prefix))
os.chdir('C:/Users/asus/Desktop/Udemy/Discord.tob/discord_py')


@client.event
async def on_ready():  # Event client ready
    await client.change_presence(status=discord.Status.idle,activity=discord.Game('=list')) #Change status to =help
    print("ID :" , client.user.id)
    print(f'Running on {len(client.guilds)} server')
    print(time.strftime("%a, %d %b %Y %H:%M:%S"))
    print(f'{client.user.name} is online')  # Print TOBI is online
    print('='*50)
    DiscordComponents(client)  # Get lib name discord component


@client.command()  # list commands
async def list(ctx):  # Contact list word
    embed = discord.Embed(title = "List commands", description = "Use '=list'",color = ctx.author.color)
    embed.add_field(name="Basic", value=
    "TOBI but in json file\n"
    "**Network**        for Check TOBI Network (.ms)\n"
    "**userinfo**       for Check user information (Join server, Role)\n"
    "**search**         for Search something on wikipedia)\n"
    "**gacha _ _**      for random number from fisrt to second\n"
    "**prize _ _**      for Give away prize from Admin by set time and prize\n"
    "**poll**           for vote Good or Bad (No limit user)\n"
    "**spawn**          for spawn TOBI to channel\n"
    "**weather**        for check weather today\n"
    "**covid**          for check daily covid\n"
    "**covid_stat**     for Covid stat in duration by Graph and total\n"
    "**bomb**           for delete message in channel\n")
    embed.add_field(name="Report", value=
    "**report**         for report User by Issue to Admin to discuss and Vote\n")
    embed.add_field(name="Math", value=
    "**plus _ _**       for plus the numbers\n"
    "**minus _ _**      for minus the numbers\n"
    "**multiplie _ _**  for multiplie the numbers\n"
    "**divide __**      for divide the numbers\n"
    "**sqrt __**        for Square root the numbers\n"
    "**expo __**        for exponent the numbers\n"
    "**fac __**        for factorial the numbers\n"
    "**Q = mcΔt**       for calculate the numbers\n")
    embed.add_field(name="Audio", value=
    "**play 'url'**     for play song\n"
    "**stop**           for stop song\n"
    "**pause**          for pause song\n"
    "**resume**         for resume song\n" )
    embed.add_field(name="ADMIN", value=
    "only Admin or mod can acess this permission\n"
    "**mute @___**      for muted someone\n"
    "**unmute @___**    for unmuted someone\n"
    "**kick @___**      for kick someone from the server\n"
    "**ban @___**       for ban someone from the server\n"
    "**vote**           for vote member when Vote was started\n")
    embed.add_field(name="Tobi", value=
    "**tobiinfo**       for TOBI information\n"
    "**git**            for GitHub\n"
    "**updateinfo**     for TOBI update command or function\n")
    await ctx.send(embed=embed)


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


@client.command() #userinfo
async def userinfo(ctx, member:discord.Member):
    print(f'Userinfo command activated by {ctx.author.name} on server {ctx.author.guild.name}')
    roles = [role for role in member.roles]
    embed = discord.Embed(title = f"Userinfo{member.name}",color = ctx.author.color)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")
    embed.add_field(name="Joined Server",value= member.joined_at.strftime('%d.%m.%y and %H hr.:%M m'))
    embed.add_field(name=f"Role({len(roles)})" ,value=" ".join([role.mention for role in roles]))
    await ctx.send(embed=embed)


@client.command() # ping pong
async def ping(ctx):
    print(f'Ping command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}') 
    await ctx.send("pong")


@client.command()
async def temp(ctx):
    print(f'Temp command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}') 
    CPULOARD= psutil.cpu_percent()
    await ctx.send(f"{CPULOARD} %")


@client.command() # plus _ _
async def plus(ctx,a : float ,b = 0):
    print(f'Plus command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}') 
    if a < 50000 and b < 50000:
        ans = a + b
        await ctx.send(f'Answer from {str(a)} + {str(b)} is {ans}')
    else:
        await ctx.send('To much Integer,Try less than 50,000')


@client.command() # minus _ _
async def minus(ctx,a: float,b = 0):
    print(f'Minus command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}') 
    if a < 50000 and b < 50000:
        ans = a - b
        await ctx.send(f'Answer from {str(a)} - {str(b)} is {ans}')
    else:
        await ctx.send('To much Integer,Try less than 50,000')


@client.command() # multiplie _ _
async def multiplie(ctx,a: float,b = 1):
    print(f'Multiplie command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}') 
    if a < 50000 and b < 50000:
        ans = a * b
        await ctx.send(f'Answer from {str(a)} * {str(b)} is {ans}')
    else:
        await ctx.send('To much Integer,Try less than 50,000')


@client.command() # multiplie _ _
async def divide(ctx,a: float,b = 1):
    print(f'Divide command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}') 
    if b == 0:
        await ctx.send('None')
    if a < 50000 and b < 50000:
        ans = a / b
        await ctx.send(f'Answer from {str(a)} / {str(b)} is {ans}')
    else:
        await ctx.send('To much Integer,Try less than 50,000')


@client.command() # sqrt
async def sqrt(ctx,a: float):
    print(f'Sqrt command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}') 
    if a < 50000:
        ans = math.sqrt(a)
        await ctx.send(f'Answer from sqrt{str(a)} is {ans}')
    else:
        await ctx.send('To much Integer,Try less than 50,000')


@client.command() # sqrt
async def expo(ctx,a: int,b = 1):
    print(f'Expo command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}')
    if  0 > a < 50000 and 0 > b < 50000:
        ans = a ** b
        await ctx.send(f'Answer from {str(a)} ^ {str(b)} is {ans}')
    else:
        await ctx.send('To much Integer,Try less than 50,000')


@client.command() # factorial
async def fac(ctx,a: int):
    print(f'Fac command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}')
    if a < 50000:
        ans = math.factorial(a)
        await ctx.send(f'Answer from factorial {str(a)} is {ans}')
    else:
        await ctx.send('To much Integer,Try less than 50,000')


@client.command()
async def matrix(ctx,a: int,b = 3):
    print(f'Matrix command activated by {ctx.author.name} on server {ctx.author.guild.name}')
    embed = discord.Embed(title = 'Random Matrix',description = 'Random quick math')
    matrix_01 = np.random.randint(1,10,size=(a,b))
    matrix_02 = np.random.randint(1,10,size=(a,b))
    if a > 0 and b > 0:
        embed.add_field(name='Matrix A',value=matrix_01)
        embed.add_field(name='Matrix B',value=matrix_02)
    else:
        await ctx.send('No matrix')
        
    await ctx.send(embed = embed)


@client.command()
async def search(ctx, text):
    print(type(text), text)
    embed = discord.Embed(title=f'Searching {text} from Wikipedia')
    try:
        searching = wikipedia.summary(str(text), sentences=1, chars=1000, auto_suggest=True, redirect=True)
        embed.add_field(name=f'Result {text} mean', value=searching)
    except NameError:
        try:
            suggest = wikipedia.search(str(text), sentences=1, chars=1000, auto_suggest=True, redirect=True)
            embed.add_field(name='Suggestion Keyword', value=suggest)
        except NameError:
            embed.add_field(name="Can't find this word")
    await ctx.send(embed=embed)


@client.command()
async def weather(ctx, city='Songkhla'):
    print(f'Weather command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}')
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
    embed = discord.Embed(title=f'Weather {city}', description='Today list', color=discord.Color.blue())

    if condition == 'Thunderstorm':
        embed.add_field(name=f'Today : {condition} ⛈', value=f'{str(temp)} °C')

    if condition == 'Drizzle':
        embed.add_field(name=f'Today : {condition} 🌧', value=f'{str(temp)} °C')

    if condition == 'Rain':
        
        embed.add_field(name=f'Today : {condition} 🌧',value=f'{str(temp)} °C')

    if condition == 'Snow':
        embed.add_field(name=f'Today : {condition} 🌨',value=f'{str(temp)} °C')

    if condition == 'Atmosphere':
        embed.add_field(name=f'Today : {condition} 🌬',value=f'{str(temp)} °C')

    if condition == 'Clear':
        embed = discord.Embed(title=f'Weather {city}',description='Today list',color = discord.Color.blue())
        embed.add_field(name=f'Today : {condition} ☁️',value=f'{str(temp)} °C')

    if condition == 'Clouds':
        embed = discord.Embed(title=f'Weather {city}',description='Today list',color = discord.Color.blue())
        embed.add_field(name=f'Today : {condition} ⛅️',value=f'{str(temp)} °C')

    embed.add_field(name='Min temp🌡 :',value=f'{str(min_temp)} °C')
    embed.add_field(name='Max temp💥 :',value=f'{str(max_temp)} °C')
    embed.add_field(name='Pressure✨ :',value=f'{str(pressure)} °C')
    embed.add_field(name='Humidity☄️ :',value=f'{str(humidity)} ')
    embed.add_field(name='Wind Speed🌫 :',value=f'{str(wind)} ')
    embed.add_field(name='Sunrise☀️ :',value=f'{str(sunrise)} pm')
    embed.add_field(name='Sunset🌤 :',value=f'{str(sunset)} pm')

    await ctx.send(embed = embed)

@client.command()
async def find_class(ctx):
    embed = discord.Embed(title = 'Class', description = 'Online class')
    print(f'Classes command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}')
    response = requests.get('http://127.0.0.1:8000')
    times = json.loads(response.text)
    hour = str(time.localtime()[3])
    today = 'Monday'

    async def find_date(date):

        global today

        if date == 0:
            today = 'Monday'
        elif date == 1:
            today = 'Tuesday'
        elif date == 2:
            today = 'Wednesday'
        elif date == 3:
            today = 'Thursday'
        elif date == 4:
            today = 'Friday'

        return today

    for keys, value in times[str(find_date(date = str(time.localtime()[6])))].items():
        hour_key = ''.join([list(keys)[0], list(keys)[1]])
        if hour_key == hour:
            embed.add_field(name= 'คาบ',value = value['class'])
            embed.add_field(name= 'ลิงค์', value= value['link'])
            print('คาบ :', value['class'], 'ลิงค์ :', value['link'])
            await ctx.send(embed = embed)
        else:
            pass

@client.command()
async def covid(ctx):
    print(f'Covid command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}')
    response = requests.get('https://covid19.ddc.moph.go.th/api/Cases/today-cases-all')
    data = json.loads(response.text)
    text = data[0]
    update = text['update_date']
    embed = discord.Embed(title = f'Covid {update} 🤮' ,description = 'Covid thailand',color = discord.Color.green())
    embed.add_field(name='New case 🦠',value= text['new_case'])
    embed.add_field(name='Total case 🧫',value= text['total_case'])
    embed.add_field(name='Total case excludeabroad 📜',value= text['total_case_excludeabroad'])
    embed.add_field(name='New death ☠️',value= text['new_death'])
    embed.add_field(name='Total death 😇',value= text['total_death'])
    embed.add_field(name='New recovered',value= text['new_recovered'])
    embed.add_field(name='Total recovered',value= text['total_recovered'])

    await ctx.send(embed = embed)

@client.command()
async def covid_stat(ctx, key=None):
    
    response = requests.get("https://covid19.ddc.moph.go.th/api/Cases/timeline-cases-all")
    data = response.json()

    case = []
    date = []
    for x in range(len(data)):
        date.append(data[x]["txn_date"])
        case.append(data[x]['new_case'])

    embed = discord.Embed(title= f'Covid-19 In duration {date[0]} to {date[len(data) - 1]}',color = discord.Color.blue())

    if key == None:
        plt.title(f'Covid-19 during {date[0]} to {date[len(data) - 1]}')
        fig = plt.figure()
        plt.plot(date,case)
        fig.savefig('covid.png', dpi = 100, facecolor = 'white')

        file = discord.File("covid.png", filename="covid.png")
        embed.set_image(url="attachment://covid.png")
        embed.add_field(name="Total case", value=data[len(data) - 1]['total_case'])
        embed.add_field(name="Total case excludeabroad", value=data[len(data) - 1]['total_case_excludeabroad'])
        embed.add_field(name="Total death", value=data[len(data) - 1]['total_death'])
        embed.add_field(name="Total recovered", value=data[len(data) - 1]['total_recovered'])
        embed.set_footer(text=f"Update Information {data[len(data) - 1]['update_date']}")

        #await ctx.send(file=discord.File('covid.png'))
        await ctx.send(file=file, embed=embed)
    
    else:

        await ctx.send('Not in a range')
        
        
@client.command()
async def code(ctx):
    r = requests.get('https://www.codewars.com/api/v1/users/{user}')
    print(r.text)


@client.command() #clear message count command text
async def bomb(ctx,Time = 10):#
    print(f'Bomb command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}')
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


@client.command()  # report requested
async def report(ctx, member:discord.Member, message,a :int):
    print(f'Report command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}')
    channel = client.get_channel(873029322288558150)
    em1 = discord.Embed(title = "Report requested", description =f"Admin will discuss about issue by {member} with {message}: level of problem {a}",color = discord.Color.red())
    em4 = discord.Embed(title = "I got Report requested", description =f"About issue made by {member} with {message}: level of problem {a}",color = discord.Color.blue())

    await ctx.send(embed = em1)
    await channel.send(embed = em4)

    # if report requested is more than 10 people and User vote is for vote for problem.


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
    #await ctx.send(f"Muted {member.mention} for reason {reason}")
    #await member.send(f"You were muted in the server {guild.name} for {reason}")


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
    print(f'Unmute command activated by {ctx.author.name} to {member} on channel {ctx.channel.name} server {ctx.author.guild.name}')
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"You were unmuted in the server {ctx.guild.name}")


@client.command(invoke_without_command = True) #tobiinfo
async def tobiinfo(ctx):
    print(f'Info command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}')
    em = discord.Embed(title = "TOBI information.json", description = "Use '=tobiinfo'",color = ctx.author.color)
    em.add_field(name = "Info",value=
    "Build by Mr. Narongkorn kitrungrot\n"
    "Version 0.11.1 (2/11/2021)\n"
    "Born 12/7/2020\n"
    "Discordbot.py © TOB · Narongkorn,Hosted by TOB Raspberrypi, distributed under the PSUWIT license")
    em.add_field(name='Github', value='https://github.com/T0b1e/Discord.tob.git')
    em.add_field(name='Supporter',value='https://ko-fi.com/narongkorn')
    em.add_field(name='Report reqest',value='https://forms.gle/2yhJfcPBpTbmWsFbA')
    await ctx.send(embed = em)


@client.command()  # git
async def git(ctx):
    print(f'Git command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}')
    em = discord.Embed(title = "Github repo", description = "Use '=git'",color = ctx.author.color)
    em.add_field(name = "Github",value="https://github.com/T0b1e/Discord.tob.git")
    await ctx.send(embed = em)


@client.command()  # poll
async def poll(ctx,*,message):
    print(f'Poll command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}')
    em = discord.Embed(title = "Vote", description = f"{message}",color = ctx.author.color)
    em.add_field(name = "Poll",value="I vote bote of them so it will count 1 first")
    msg = await ctx.channel.send(embed=em)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    x = len(message.reactions)
    print(x)


@client.command() #Vote
async def vote(ctx, member :discord.Member):
    print(f'Vote command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}')
    await ctx.send(f"Recieve Vote {member}")
    time.sleep(10)
    await ctx.channel.purge(limit=2)


@client.command()
async def button(ctx):
    print(f'Button command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}')
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
    print(f'Voting command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}')
    await ctx.send(
        f"Voting System Start",
        components =[
            Button(label= 'Agree', style=ButtonStyle.blue),
            Button(label= 'Disagree', style=ButtonStyle.red),
            Button(label= 'No vote', style=ButtonStyle.green)
        ]
    )
    res = await client.wait_for('button_click', check=lambda i: i.component.label.startswith("Click"))
    await res.respond(content='button clicked')
    res = await client.wait_for('button_click', check=lambda i: i.component.label.startswith("Click"))
    await res.respond(content='button clicked')
    res = await client.wait_for('button_click', check=lambda i: i.component.label.startswith("Click"))
    await res.respond(content='button clicked')


@client.command()  # gacha+time
async def prize(ctx, mins :int, *,prize :str):
    print(f'Prize command activated by {ctx.author.name} on channel {ctx.channel.name} server {ctx.author.guild.name}')
    embed = discord.Embed(title = "Gacha", description = f"{prize}",color = ctx.author.color)
    end = datetime.datetime.utcnow() + datetime.timedelta(seconds= mins * 60)
    embed.add_field(name=" End time :", value=f"{end} UTC")
    embed.set_footer(text=" Countdown {mins} minutes from now")
    msg = await ctx.send(embed = embed)
    await asyncio.sleep(mins*60)

    new_msg = await ctx.channel.fetch_message(msg.id)
    user = await new_msg.reaction[0].users().flatten()
    user.pop(user.index(client.user))
    winner = random.choice(user)
    await ctx.send(f"Congratulation to {winner.mention} won")


@client.command(pass_context = True)  # gacha number
async def gacha(ctx, num1: int, num2: int):
    print(f'Gacha command activated by {ctx.author.name} on server {ctx.author.guild.name}')
    if num1 < 100 and num2 < 100:
        embed = discord.Embed(title = "Gacha", description = (random.randint(num1,num2)),color = ctx.author.color)
        await ctx.send(embed = embed)
    else:
        await ctx.send('To much number,Try less than 100')


@client.command(pass_context = True)  # spawn
async def spawn(ctx):

    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        
        await channel.connect()
    else:
        await ctx.send("you're not in the voice channel")

    print(f'Spawn command activated by {ctx.author.name} at {channel} on server {ctx.author.guild.name}')


@client.command()
async def volume(ctx, volume: int):
    if volume < 0:
        print('To Low')

    if volume > 150:
        print('To High')
    msg = await ctx.send(f"Volume set to {volume:,}%")
    await msg.add_reaction('🔊')


@client.command()  # play
async def play(ctx, url):
    channel = ctx.message.author.voice.channel
    embed_play = discord.Embed(title = f'Play {url}',description = 'Playing music in queue',color = ctx.author.color) 
    msg = await ctx.send(embed = embed_play) 
    await msg.add_reaction('🎶')
    print(f'Play command activated by {ctx.author.name} play {url} at {channel} on server {ctx.author.guild.name}')
    song_there = os.path.isfile("song.mp3")

    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return
    
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


@client.command()  # leave
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)   
    print(f'Leave command activated by {ctx.author.name} on server {ctx.author.guild.name}')
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()  # pause
async def pause(ctx):
    embed_pause = discord.Embed(title = f'pause  song',description = 'Playing music in queue',color = ctx.author.color)
    print(f'Pause command activated by {ctx.author.name} on server {ctx.author.guild.name}')
    msg = await ctx.send(embed = embed_pause)
    await msg.add_reaction('🔇')
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()  # resume
async def resume(ctx):
    embed_resume = discord.Embed(title = f'Resume the song song',description = 'Playing music in queue',color = ctx.author.color)
    print(f'Resume command activated by {ctx.author.name} on server {ctx.author.guild.name}')
    msg = await ctx.send(embed = embed_resume)
    await msg.add_reaction('🔉')
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()  # stop
async def stop(ctx):
    embed_stop = discord.Embed(title = 'Stop song',description = 'Stop playing music in queue',color = ctx.author.color)
    print(f'Stop command activated by {ctx.author.name} on server {ctx.author.guild.name}')
    msg = await ctx.send(embed = embed_stop)
    await msg.add_reaction('🔴')
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    
client.run(token)