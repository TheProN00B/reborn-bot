import discord
import random
from discord.colour import Color
from discord.ext import commands
from discord.ext.commands.core import command

class Fun(commands.Cog):

  def __init__(self, client):
    self.client = client


  #events
  @commands.Cog.listener()
  async def on_ready(self):
    print('Fun Cog Loaded')

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





def setup(client):
  client.add_cog(Fun(client))