import datetime
from discord.ext import commands, tasks
import imgGen
import csv

utc = datetime.timezone.utc

# If no tzinfo is given then UTC is assumed.
time = datetime.time(hour=15, minute=0, tzinfo=utc)
#channelList = []

file = open("channelList.csv","r")
tempChannels = list(csv.reader(file,delimiter=","))
file.close()

channelList = [item for sublist in tempChannels for item in sublist]

print(channelList)

class taskCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_task.start()

    def cog_unload(self):
        self.my_task.cancel()

    @tasks.loop(time=time)
    async def my_task(self):
        url = imgGen.genImg()
        for chanID in channelList:
            channel = self.bot.get_channel(int(chanID))
            await channel.send(url)
        print("task successful!")
    @commands.command()
    async def setUp(self,ctx, channelID):
        channelList.append(channelID)
        print(channelList)
        with open('channelList.csv','w') as f:
            write = csv.writer(f)
            write.writerow(channelList)
        await ctx.send("successfully added channel to list!")
    @commands.command()
    async def forceWord(self,ctx):
        await ctx.send("Forcing new word of the day...")
        url = imgGen.genImg()
        for chanID in channelList:
            channel = self.bot.get_channel(int(chanID))
            await channel.send(url)
        print("word forcefully sent")
        await ctx.send("New word of the day sent!")