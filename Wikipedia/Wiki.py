import discord
from discord.ext import commands

try:
    import wikipedia
    exists=True
except:
    exists=False



class Wiki:
    """search wikipedia"""


    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def wiki(self, *, request : str):
        """Search Wikipedia's massive database"""
        try:
            answer=wikipedia.summary(request)
            await self.bot.say(answer)
        except:
            await self.bot.say("no results")
        #insert wikipedia connection code

def setup(bot):
    if exists:
        bot.add_cog(Wiki(bot))
    else:
        raise RuntimeError("You need to run `pip3 install wikipedia`")
