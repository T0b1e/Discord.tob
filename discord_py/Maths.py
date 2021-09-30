import discord
from discord.ext import commands,tasks
import math
import numpy as np
import os
import json

with open('config.json', 'r') as c:
    data=c.read()

obj = json.loads(data)
key = obj['dict']
prefix = key['prefix']
token = key['token']
client = commands.Bot(command_prefix= prefix)#d['prefix']
#os.chdir('C:/Users/asus/Desktop/Udemy/Discord.tob/discord_py')

@client.event
async def on_ready(): #Event client ready
    channel = client.get_channel(880036878038990858) #Get channel id
    await channel.send('TOBI is on ready, Type "=list" to start')
    await client.change_presence(status=discord.Status.idle,activity=discord.Game('=list')) #Change status to =help
    print(f'{client.user.name} is online') #Print TOBI is online

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
        await ctx.send(f'Answer from factorial {str(a)} is {ans}')
    else:
        await ctx.send('To much Integer,Try less than 50,000')
  

@client.command() #Q = mcΔt
async def Q(ctx,m: float,c: float,t1: float,t2: float):
        await ctx.send(m*c*(t2-t1))

@client.command()
async def matrix(ctx,a: int,b: int):
    embed = discord.Embed(title = 'Random Matrix',description = 'Random quick math')
    matrix_01 = np.random.randint(1,10,size=(a,b))
    matrix_02 = np.random.randint(1,10,size=(a,b))
    if a > 0 and b > 0:
        embed.add_field(name='Matrix A',value=matrix_01)
        embed.add_field(name='Matrix B',value=matrix_02)
    else:
        await ctx.send('No matrix')
        
    await ctx.send(embed = embed)


client.run(str(token))