import datetime
from discord.ext import commands, tasks
import imgGen
utc = datetime.timezone.utc

# If no tzinfo is given then UTC is assumed.
time = datetime.time(hour=3, minute=0, tzinfo=utc)
channelList = []
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
        await ctx.send("successfully added channel to list!")





