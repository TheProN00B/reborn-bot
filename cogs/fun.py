import discord
import random
import aiohttp
from discord.colour import Color
from discord.ext import commands
from discord.ext.commands.core import command
from aiohttp.helpers import TimeoutHandle

class Fun(commands.Cog):

  def __init__(self, client):
    self.client = client


  #events
  @commands.Cog.listener()
  async def on_ready(self):
    print('Fun Cog Loaded')

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.content == 'rip' or message.content == 'RIP':
      await message.add_reaction("<:riplol:858925516312543233>")

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.content == 'KEKW' or message.content == 'kekw':
      await message.add_reaction("<:KekwLaugh:842035311035023370>")

  @commands.command(name='8ball')
  async def eightball(self, ctx, *, question):
    responses = ['Yes',
                 'no',
                 'maybe',
                 'Idk, man',
                 'Ask Jesus for it']
    em = discord.Embed(title = '**8Ball**',
                        description = f'Question : {question}',
                        color = discord.Color.dark_green())
    em.add_field (name = 'Answer' , value = f'{random.choice(responses)}')
    em.set_footer(text=f'Requested by {ctx.author}', 
                icon_url=ctx.author.avatar_url)
    await ctx.send(embed=em)

  @eightball.error
  async def eightball_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f"Please enter all the required value.")
      return

  @commands.command(aliases=['av','pfp'])
  async def avatar(self, ctx, target : discord.Member = None):
      if target is None:
          target = ctx.message.author
      embed = discord.Embed(title = 'Avatar', colour = random.randint(0,0xffffff))
      embed.set_image(url=target.avatar_url)
      embed.set_footer(text = f'Requested by {ctx.author}',
                        icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)

  @commands.command(aliases=['memes'])
  async def meme(self, ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://www.reddit.com/r/memes/hot.json') as r:
        res = await r.json()
      embed = discord.Embed(title="Here's your Meme , kek", color=random.randint(0,0xffffff))
      embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
      embed.set_footer(text=f'Requested by {ctx.author}',
                      icon_url = ctx.author.avatar_url)
    await ctx.send(embed=embed, content=None)




def setup(client):
  client.add_cog(Fun(client))
