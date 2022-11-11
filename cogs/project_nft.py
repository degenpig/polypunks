import discord
from discord_slash.utils.manage_commands import create_option
import urllib.request as ur
import json
from discord_slash import cog_ext
from core.cog_core import cogcore
from decouple import config

class project_nft(cogcore):
  @cog_ext.cog_slash(name="punk_nft",
  description="return some useful information about your NFT from the token id you entered",
  options=
  [
    create_option
    (
      name="token_id",
      description="enter the token id of your NFT",
      option_type=3,
      required=True
    )
  ],
  )

  async def nft(self,ctx,token_id):
    url1='https://api.nftport.xyz/v0/nfts/'+config('nft_contract_address')+'/'+token_id+'/?chain=polygon&refresh_metadata=true' #api url
    headers1 = {
          "Content-Type": "application/json",
          "Authorization": config('nft_apikey')
      }
    req = ur.Request(url=url1,headers=headers1)
    
    site1 = ur.urlopen(req)
    page1 = site1.read()
    contents1 = page1.decode()
    data1 = json.loads(contents1)    

    if data1['nft']['metadata']['name'] == None:
      name = "no data"
    else:
      name = str(data1['nft']['metadata']['name'])
      

    if data1['nft']['metadata']['image'] == None:
      image_original_url = "no data"
    else:
      image_original_url = str(data1['nft']['metadata']['image'])


    if data1['owner'] == None:
      top_ownerships = "no data"
    else:
      top_ownerships = str(data1['owner'])


    if data1['nft']['metadata']['description'] == None:
      description = "no data"
    else:
      description = str(data1['nft']['metadata']['description'])


    if data1['nft']['metadata']['external_url'] == None:
      external_link = "no data"
    else:
      external_link = str(data1['nft']['metadata']['external_url'])


    if data1['nft']['metadata']['attributes'][1]['value'] == None:
      schema_name = "no data"
    else:
      schema_name = str(data1['nft']['metadata']['attributes'][1]['value'])


    if data1['nft']['token_id'] == None:
      token_id1 = "no data"
    else:
      token_id1 = str(data1['nft']['token_id'])

    
    permalink = 'https://opensea.io/assets/matic/'+config('nft_contract_address')+'/'+token_id


    embed=discord.Embed(title="["+name+"]", color=0xe8006f)
    embed.set_thumbnail(url=image_original_url)
    embed.add_field(name="token id" , value=token_id1, inline=False) 
    embed.add_field(name="description" , value=description, inline=False)     
    embed.add_field(name="official website" , value=external_link, inline=False) 
    embed.add_field(name="token type" , value=schema_name, inline=False) 
    # embed.add_field(name="owner" , value=top_ownerships, inline=False)
    embed.add_field(name="OpenSea" , value=permalink, inline=False)
    embed.add_field(name="original resolution image" , value=image_original_url, inline=False)

    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(project_nft(bot))
