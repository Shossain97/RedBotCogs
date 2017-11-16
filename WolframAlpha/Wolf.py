try:#check if wolframalpha library exists
	import wolframalpha
	wolframAvailable=True
except:
	wolframAvailable=False

import discord
from discord.ext import commands

import aiohttp
API_Key=""

class Wolf:
	"""Everyone's favorite Homework Helper"""
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def wolfram(self, *, question : str):
		"""Ask wolfram for math help """

		try:
			client = wolframalpha.Client(API_Key)
			res=client.query(question)
			try:
				answer=next(res.results).text
				await self.bot.say(answer)
			except:
				await self.bot.say("That is an invalid question")
		except:
			await self.bot.say("API key is invalid please navigate to Wolf.py (cog) and input your API Key from developer.wolframalpha.com")

		

def setup(bot):
	if wolframAvailable:
		bot.add_cog(Wolf(bot))
	else:
		raise RuntimeError("You need to run `pip3 install wolframalpha`")
