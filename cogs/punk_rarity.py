import discord
from discord_slash.utils.manage_commands import create_option
import urllib.request as ur
import json
from discord_slash import cog_ext
from core.cog_core import cogcore
from decouple import config

class punk_rarity(cogcore):
  @cog_ext.cog_slash(name="punk_rarity",
  description="query your NFT rarity from the collection slug and token id you entered",
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

  async def punk_rarity(self,ctx,token_id):
    url0="https://api.opensea.io/api/v1/collection/"+config('collection_slug') #api url
    req = ur.Request(url=url0,headers={'User-Agent': 'Mozilla/5.0'})

    site0 = ur.urlopen(req)
    page0 = site0.read()
    contents0 = page0.decode()
    data0 = json.loads(contents0)

    contract_address = data0['collection']['primary_asset_contracts'][0]['address']

    total_supply = data0['collection']['stats']['total_supply']

    collection_trait = data0['collection']['traits']


    #
    file = open("traits.json", "r")
    data = json.load(file)



    for t_type in collection_trait:
      except_none = 0
      for t_name in collection_trait[t_type]:
        except_none += (collection_trait[t_type][t_name])
        data[t_type] = collection_trait[t_type]
        data[t_type][t_name] = round(total_supply / collection_trait[t_type][t_name],2)
        
      if (total_supply-except_none) != 0:
        data[t_type]["none"] = round(total_supply / (total_supply-except_none),2)
    with open('traits.json', 'w') as outfile:
      json.dump(data, outfile)
    file.close()

    #query nft traits from opensea and get rarity from traits.json

    file = open("traits.json", "r")
    data = json.load(file)


    url1='https://api.opensea.io/api/v1/asset/'+contract_address+'/'+token_id+'/?format=json' #api url
    req = ur.Request(url=url1,headers={'User-Agent': 'Mozilla/5.0'})

    site1 = ur.urlopen(req)
    page1 = site1.read()
    contents1 = page1.decode()
    data1 = json.loads(contents1)

    if data1['name'] == None:
      name = "no data"
    else:
      name = "PolyPunk #" + token_id

    if data1['image_original_url'] == None:
      image_original_url = "no data"
    else:
      image_original_url = "https://polypunks.app/punks/pic_bg/" + token_id + ".png"

    if data1['top_ownerships'][0]['owner']['user'] == None:
      top_ownerships = "no data"
    else:
      top_ownerships = str(data1['top_ownerships'][0]['owner']['user']['username'])

    if data1['permalink'] == None:
      permalink = "no data"
    else:
      permalink = "https://opensea.io/assets/matic/0x320f537da591da33dd1a04dcb062434e3d176d3e/" + token_id

    finaldata = {}
    totalrarity = 0.0
    total_traits_score = 0.0
    single_traitscount = 0
    for all_element in data:#all
      match = 0
      
      for element in data1['traits']:#nft
        if all_element == element['trait_type']:
          
          ev = element['value'].lower()


          finaldata[all_element] = {"1":element['value'],"2":data[all_element][ev]}
          match = 1
          single_traitscount += 1
          total_traits_score += float(data[all_element][ev])
      
        #finaldata[all_element] = {"1":element['value'],"2":data[all_element][ev] }
      if match != 1:
        finaldata[all_element] = {"1":'none',"2":data[all_element]['none']}
        total_traits_score += float(data[all_element]['none'])
    print(single_traitscount)

    with open('finaldata.json', 'w') as outfile:
      json.dump(finaldata, outfile)

    file = open("finaldata.json", "r")
    fdata = json.load(file)    

    ranks_file = open('ranks.json', 'r')
    rank = json.load(ranks_file)[int(token_id)][str(int(token_id))]

    embed=discord.Embed(title="["+name+"]", color=0xe8006f)
    embed.set_thumbnail(url=image_original_url)
    embed.add_field(name="token id" , value=token_id, inline=False) 
    # embed.add_field(name="owner" , value=top_ownerships, inline=False)
    embed.add_field(name="OpenSea" , value=permalink, inline=False)
    embed.add_field(name="traits count" , value=single_traitscount, inline=False)
    embed.add_field(name="rank" , value=rank, inline=False)
    embed.add_field(name="total traits score" , value=round(total_traits_score,2), inline=False)
    embed.add_field(name=" ㅤ" , value=" ㅤ", inline=False)
    for result in fdata:
      embed.add_field(name=result, value=str(fdata[result]['1'])+" "+str(fdata[result]['2']), inline=True)
      
      

    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(punk_rarity(bot))
