import discord
from discord import colour
from discord.embeds import Embed
from discord.enums import UserContentFilter
from discord.ext import commands
from discord.ext.commands.core import command

class Server(commands.Cog):

  def __init__(self, client):
    self.client = client


  #events
  @commands.Cog.listener()
  async def on_ready(self):
    print('Server Cog Loaded')
  
  #commands

  @commands.command(aliases=['botinfo'])
  async def aboutbot(self, ctx):
    embed = discord.Embed(title ='About the Bot!' , 
    description ='This bot is developed by TheProN00B and is completely Open-Source. You can get the Source-Code on GitHub',
    color = discord.Colour.gold())
    embed.add_field(name='GitHub', value='https://github.com/TheProN00B/reborn-bot')
    await ctx.send(embed=embed)

  @commands.command()
  async def hello(self, ctx):
    embed = discord.Embed(title = f'Hello {ctx.author}', 
    description = "In case you are a new member , don't forget to check out <#845152425739681843> and <#840909761322156042> for information related to the game and development.", 
    color = discord.Colour.green())
    embed.add_field(name="...", value="Also , enjoy your stay in this server.", inline=False)
    await ctx.send(embed=embed)

  @commands.command()
  async def faq(self, ctx):
    embed = discord.Embed(title='**FAQs**',
                          description='Here are some answered FAQs',
                          color=discord.Colour.gold())
    embed.add_field(name='What is PROJECT REBORN?',
                    value="PROJECT REBORN is a free-to-play battle royale game that can be played on low specification computers. The Battle Royale game allows players to join in a game with a maximum of 100 players for survival. Players can gather weapons, vehicles and supplies strategically to outwit opponents to become the last person standing.")
    embed.add_field(name="What's the release date?",
                    value="There's not a release date yet. Projects like this takes a lot of time to be released, even for large gaming companies - we are just a group of fans that want the PROJECT REBORN experience back. 2023 is the late release date, for sure we want to release as soon as possible, but things needs to be well made.")
    embed.add_field(name='Will it meet the same system requirements as PROJECT REBORN?',
                    value="The idea is to keep the same system requirements as PROJECT REBORN By the moment, alpha-builds doesn't meet those requirements, game will be optimized in further releases.")
    embed.add_field(name='Where can I download the alpha-build?',
                    value="<#834643182906114058> is the way to go. Be sure your graphics drivers are up-to-date. You don't need UE4. Note that this is just an open alpha-build, so people can see how it is going. It does not represent the final product or experience.")
    embed.set_image(url='https://cdn.discordapp.com/attachments/834643663187083266/855289056644300820/Logotype_blackbg.png')
    embed.set_footer(text=f'Requested by {ctx.author}',
                    icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


def setup(client):
  client.add_cog(Server(client))