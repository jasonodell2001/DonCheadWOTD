import discord
import imgGen
import datetime
import taskcog
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
utc = datetime.timezone.utc

bot = commands.Bot(command_prefix='?', description='', intents=intents)


@bot.event
async def on_ready():
    await bot.add_cog(taskcog.taskCog(bot))


@bot.command()
async def changePref(ctx, pref: str):
    bot.command_prefix = pref
    await ctx.send('Succesfully updated prefix to ' + pref)

@bot.command()
async def hello(ctx):
    await ctx.send("https://i.imgflip.com/7tcf74.jpg")

bot.run('INSERT TOKEN HERE')
