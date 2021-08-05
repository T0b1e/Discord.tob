import discord
from discord import channel
from discord import member
from discord.ext import commands
from discord.player import FFmpegPCMAudio #audio
from discord.utils import get
import youtube_dl #play
import os #play
import datetime #gacha,userinfo
import asyncio #gacha
import random #gacha


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

@client.command()
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

@client.command()
async def kick(ctx, member :discord.Member, *,reason = "Kick because you don't follow the rules"):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member :discord.Member, *,reason = "Ban because you don't follow the rules"):
    await member.ban(reason=reason)

@client.command(invoke_without_command = True) #tobiinfo
async def tobiinfo(ctx):
    em = discord.Embed(title = "TOBI information.json", description = "Use '=tobiinfo'",color = ctx.author.color)
    em.add_field(name = "Info",value=
    "Build by Mr. Narongkorn kitrungrot\n"
    "Version 0.5.1 (5/8/2021)\n"
    "Born 12/7/2020\n"
    "Discordbot.js © TOB · Narongkorn,Hosted by TOB Raspberrypi, distributed under the PSUWIT license")
    await ctx.send(embed = em)

@client.command(invoke_without_command = True) #updateinfo
async def updateinfo(ctx):
    em = discord.Embed(title = "TOBI Update information", description = "Use '=updateinfo'",color = ctx.author.color)
    em.add_field(name = "Info",value=
    "**Prefix change from / to = **\n"
    "**Music command** = play,stop,pause,resume\n"
    "**Calculater Mode** = plus,minus,multiplie,divide\n"
    "**Member cout**\n"
    "**UserInfo**\n"
    "**Voting, Poll** \n"
    "**Gacha** = number,member\n"
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

@client.command() #githup repo
async def git(ctx):
    em = discord.Embed(title = "Github repo", description = "Use '=git'",color = ctx.author.color)
    em.add_field(name = "Github",value="https://github.com/T0b1e/Discord.tob.git")
    await ctx.send(embed = em)

@client.command() #poll
async def poll(ctx,*,message):
    em = discord.Embed(title = "Vote", description = f"{message}",color = ctx.author.color)
    em.add_field(name = "Democracy",value="for justice")
    msg = await ctx.channel.send(embed=em)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')

@client.command() #vote for ban member
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

@client.command() #play
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name= "ห้องเมียแขกและเกาหลี")
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
client.run('ODMzMjgwODM0MTYwOTUxMjk2.YHwDQA.6yR2YXO4fI3HoLdYTeC18J8NYE8')
