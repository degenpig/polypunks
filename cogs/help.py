import discord
import asyncio 
from discord_slash import cog_ext
from core.cog_core import cogcore

class help(cogcore):
  @cog_ext.cog_slash(name="help",description="display help message")
  async def help(self,ctx):
    BUTTONS = ["◀️","0️⃣","1️⃣","2️⃣","3️⃣","4️⃣"]
    embed=discord.Embed(title="**/help**", description="command list\npress the emoji to select page ", color=0xe8006f)

    embed.add_field(name="[back]", value="◀️", inline=True)
    embed.add_field(name="[bot information]", value="0️⃣", inline=True)
    embed.add_field(name="ㅤ", value="ㅤ", inline=True)
    embed.add_field(name="[system]", value="1️⃣", inline=True)
    embed.add_field(name="[NFT]", value="2️⃣", inline=True)
    embed.add_field(name="[3(in development)]", value="3️⃣", inline=True)
    embed.add_field(name="[4(in development)]", value="4️⃣", inline=True)
    embed.add_field(name="options", value="some commands must input option(s)\ne.g. /punk-nft token_id: 824 \n`824`is the option of this command.If there are more than 2 options, after entered the first one, you can press `tab` on the keyboard to switch to the next option.", inline=False)
    embed.set_footer(text="last update:\n2022.03.16 04:01 p.m.")
    msg = await ctx.send(embed=embed)
    embed0=discord.Embed(title="**[bot information]**", description="information about this bot", color=0xe8006f)
    embed0.add_field(name="bot name", value="PolyPunkBot", inline=False)
    embed0.add_field(name="developer", value="Jacky", inline=False)
    embed0.add_field(name="bot avatar illustrator", value="Kevin", inline=False)
    embed0.add_field(name="programming language", value="Python", inline=False)
    embed0.add_field(name="Project Name", value="PolyPunks", inline=False)
    embed0.add_field(name="NFT Name", value="Polypunks", inline=False)
    embed0.add_field(name="Contract Address", value="0x320f537da591da33Dd1A04dCB062434e3D176D3E", inline=False)
    embed0.add_field(name="Collection Slug", value="polypunks", inline=False)
    embed0.add_field(name="GitHub", value="https://github.com", inline=False)
    embed0.add_field(name="contact information", value="Jacky: CryptoJacky#1696\n", inline=False)
    embed0.add_field(name="note", value="transaction record function calls Etherscan API, OpenSea, Lootex related functions calls OpenSea API, Lootex API.", inline=False)

    embed1=discord.Embed(title="**[system]**", description="system commands", color=0xe8006f)
    embed1.add_field(name="/help", value="display help message.", inline=False)
    embed1.add_field(name="/invite", value="get bot invite link, invite bot to your server. `admin permission is required in the server you invite to`", inline=False)
    embed1.add_field(name="/ping", value="return bot latency.", inline=False)

    embed2=discord.Embed(title="**[NFT]**", description="search information of NFT project.", color=0xe8006f)
    embed2.add_field(name="/punk_realtime", value="display real-time price of specific project.", inline=False)
    embed2.add_field(name="/project-history", value="display history price of specific project. option:`project_name`", inline=False)
    embed2.add_field(name="/punk_nft", value="search the NFT of a specific item and a specific number. option:`token_id`", inline=False)
    embed2.add_field(name="/txn", value="enter the address and display the transaction record. option: `eth_address`", inline=False)
    embed2.add_field(name="/account", value="enter the address to display ETH balance and Punk NFT balance. option: `eth_address`", inline=False)

    embed3=discord.Embed(title="**[3]**", description="3", color=0xe8006f)
    embed3.add_field(name="3", value="3", inline=False)

    embed4=discord.Embed(title="**[4]**", description="4", color=0xe8006f)
    embed4.add_field(name="4", value="4", inline=False)

    for b in BUTTONS:
      await msg.add_reaction(b)
    
    while True:
      try:
        react, user = await self.bot.wait_for("reaction_add", timeout=60.0, check=lambda r, u: r.message.id == msg.id and u.id == ctx.author.id and r.emoji in BUTTONS)
        await msg.remove_reaction(react.emoji, user)
      
      except asyncio.TimeoutError:
        pass

      else:
        if react.emoji == BUTTONS[0]:
          await msg.edit(embed=embed)
        if react.emoji == BUTTONS[1]:
          await msg.edit(embed=embed0)
        elif react.emoji == BUTTONS[2]:
          await msg.edit(embed=embed1)
        elif react.emoji == BUTTONS[3]:
          await msg.edit(embed=embed2)
        elif react.emoji == BUTTONS[4]:
          await msg.edit(embed=embed3)
        elif react.emoji == BUTTONS[5]:
          await msg.edit(embed=embed4)
def setup(bot):
  bot.add_cog(help(bot))