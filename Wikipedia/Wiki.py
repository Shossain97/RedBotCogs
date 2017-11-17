import discord
from discord.ext import commands



class Wiki:
    """search wikipedia"""


    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def wiki(self, *, request : str):
        """Search Wikipedia's massive database"""

        #insert wikipedia connection code

def setup(bot)
    bot.add_cog(Wiki(bot))
