from distutils.command.config import config
import discord
from discord_slash import cog_ext
from core.cog_core import cogcore
from discord_slash.utils.manage_commands import create_option
import urllib.request as ur
import json
import os
from decouple import config

etherscan_api_key = config('etherscan_api_key')
class account(cogcore):
  @cog_ext.cog_slash(
  name="account",
  description="get the account info from the ETH address you enter",
  options=
  [
    create_option
    (
      name="eth_address",
      description="enter wallet address",
      option_type=3,
      required=True
    )
  ]
  )

  async def account_info(self, ctx, eth_address: str):
  # await ctx.send(content=f"{eth_address}")
    url1='https://api.polygonscan.com/api?module=account&action=balance&address='+eth_address+'&tag=latest&apikey='+etherscan_api_key #api url

    url2='https://api.polygonscan.com/api?module=account&action=tokenbalance&contractaddress=0x320f537da591da33Dd1A04dCB062434e3D176D3E&address='+eth_address+'&tag=latest&apikey='+etherscan_api_key

    site1 = ur.urlopen(url1)
    page1 = site1.read()
    contents1 = page1.decode()
    data1 = json.loads(contents1)

    bal_ori = data1['result']#eth balance
    eth_bal = int(bal_ori)/1000000000000000000

    site2 = ur.urlopen(url2)
    page2 = site2.read()
    contents2 = page2.decode()
    data2 = json.loads(contents2)

    punk_balance = data2['result']

    if(eth_bal != 0):
      embed=discord.Embed(title="[balance]", color=0xe8006f)
      embed.set_thumbnail(url="https://cdn.jsdelivr.net/gh/Xeift/image-hosting@main//a8eb74eaa4d1148c2b33db119edb9515.gif")
      embed.add_field(name="ETH balance" , value=str(eth_bal)[0:7]+"||"+str(eth_bal)[7:20]+"||"+" ETH", inline=False)
      await ctx.send(embed=embed)
    else:
        await ctx.send("no ETH in this address or you've entered the wrong address")

def setup(bot):
  bot.add_cog(account(bot))