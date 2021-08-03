import discord
from discord import channel
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os

client = commands.Bot(command_prefix='=')
client.remove_command("help")

@client.event
async def on_ready(): 
    await client.change_presence(status=discord.Status.idle,activity=discord.Game('/help'))
    print('Bot is now ready')

@client.event
async def on_member_join(member): # join
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member): # remove
    print(f'{member} has removed the server.')

@client.command() # ping pong
async def ping(ctx):
    await ctx.send("pong")

@client.command() # plus _ _
async def plus(ctx, a: int, b: int):
    await ctx.send(a + b)

@client.command() # minus _ _
async def minus(ctx, a: int, b: int):
    await ctx.send(a - b)

@client.command() # multiplie _ _
async def multiplie(ctx,a: int,b: int):
    await ctx.send(a * b)

@client.command(invoke_without_command = True) #tobiinfo
async def tobiinfo(ctx):
    em = discord.Embed(title = "TOBI information.json", description = "Use '=tobiinfo'",color = ctx.author.color)
    em.add_field(name = "Info",value=
    "Build by Mr. Narongkorn kitrungrot\n"
    "Version 0.4.1 (3/8/2021)\n"
    "Born 12/7/2020\n"
    "Discordbot.js © TOB · Narongkorn,Hosted by TOB Raspberrypi, distributed under the PSUWIT license")
    await ctx.send(embed = em)

@client.command(invoke_without_command = True) #updateinfo
async def updateinfo(ctx):
    em = discord.Embed(title = "TOBI Update information", description = "Use '=updateinfo'",color = ctx.author.color)
    em.add_field(name = "Info",value=
    "Prefix change from / to = \n"
    "Music command = play,stop,pause,resume\n"
    "Calculater Mode = plus,minus,multiplie\n"
    "Member cout\n"
    "Coming soon function = queue, skip, Homework notification, Uptime Classroom")
    await ctx.send(embed = em)

@client.group(invoke_without_command = True) #help
async def help(ctx):
    em = discord.Embed(title = "Help", description = "Use '=help <command>'",color = ctx.author.color)
    em.add_field(name = "Basic command",value="plus, minus, multiplie")
    em.add_field(name = "Music",value="play, stop, pause, resume")
    await ctx.send(embed = em)

@client.command() #helpplus
async def helpplus(ctx):
    em = discord.Embed(title = "plus", description = "Use '=plus <Number>_<Number>'",color = ctx.author.color)
    await ctx.send(embed = em)

@client.command() #git
async def git(ctx):
    em = discord.Embed(title = "Github repo", description = "Use '=git'",color = ctx.author.color)
    em.add_field(name = "Github",value="plus, minus, multiplie")
    await ctx.send(embed = em)

@client.command() #play
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='คนมีความฝัน')
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
    else:
        await ctx.send("Currently no audio is playing.")

@client.command() #resume
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")

@client.command() #stop
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

client.run('ODMzMjgwODM0MTYwOTUxMjk2.YHwDQA.6yR2YXO4fI3HoLdYTeC18J8NYE8')
