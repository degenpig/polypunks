import discord
import asyncio
import os
from discord.ext import commands
from discord_slash import SlashCommand
import urllib.request as ur
import json
import keep_alive
from decouple import config

discord_token = config('discord_token')
etherscan_api_key = config('etherscan_api_key')

bot = commands.Bot(
	command_prefix="k!", #  bot prefix
	case_insensitive=True, #  case-sensitive
  intents=discord.Intents.all(), 
  help_command=None 
)
slash = SlashCommand(bot, sync_commands=True) 

@bot.event
async def on_ready():
  print("Ready!")
  while True:
    url1='https://api.polygonscan.com/api?module=stats&action=ethprice&apikey='+etherscan_api_key #api url

    site1 = ur.urlopen(url1)
    page1 = site1.read()
    contents1 = page1.decode()
    data1 = json.loads(contents1)

    ethusd = data1['result']['ethusd']
    #####
    url2='https://api.polygonscan.com/api?module=gastracker&action=gasoracle&apikey='+etherscan_api_key #api url

    site2 = ur.urlopen(url2)
    page2 = site2.read()
    contents2 = page2.decode()
    data2 = json.loads(contents2)

    SafeGasPrice = data2['result']['SafeGasPrice']
    ProposeGasPrice = data2['result']['ProposeGasPrice']
    FastGasPrice = data2['result']['FastGasPrice']

    presence_ctx1 = 'Ξ '+ethusd
    presence_ctx2 = '🚀'+FastGasPrice+'🚗'+ProposeGasPrice+'🚲'+SafeGasPrice

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=presence_ctx1))
    await asyncio.sleep(10)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=presence_ctx2))
    await asyncio.sleep(10)

#Load Cog
extensions = [
  'cogs.account',
	'cogs.help',
  'cogs.invite',
  'cogs.ping', 
  'cogs.project_nft',
  'cogs.project_realtime',
  'cogs.punk_rarity',
  'cogs.txn',
]

if __name__ == '__main__':
	for extension in extensions:
		bot.load_extension(extension)  

keep_alive.keep_alive()
discord_token = config('discord_token')
bot.run(discord_token)