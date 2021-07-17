import discord
import random
import aiohttp
from discord.ext import commands

class Fun(commands.Cog):

  def __init__(self, client):
    self.client = client
    self.kekw_word = ['kekw', 'Kekw', 'KEKW']
    self.rip_word = ['rip', 'Rip', 'RIP']


  #events
  @commands.Cog.listener()
  async def on_ready(self):
    print('Fun Cog Loaded')


  @commands.Cog.listener()
  async def on_message(self, message):
   for word in self.kekw_word:
     if word in message.content:
      await message.add_reaction("<:KekwLaugh:842035311035023370>")
  
  @commands.Cog.listener()
  async def on_message(self, message):
   for word in self.rip_word:
     if word in message.content:
      await message.add_reaction("<:riplol:858925516312543233>")



  @commands.command(name='8ball')
  async def eightball(self, ctx, *, question):
    responses = ['Yes',
                 'no',
                 'maybe',
                 'Idk, man',
                 'Ask Jesus for it']
    embed = discord.Embed(title = '**8Ball**',
                        description = f'Question : {question}',
                        color = discord.Color.dark_green())
    embed.add_field (name = 'Answer' , value = f'{random.choice(responses)}')
    embed.set_footer(text=f'Requested by {ctx.author}', 
                icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

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

  @commands.command(aliases=['dank'])
  async def dankmeme(self, ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://www.reddit.com/r/dankmemes/hot.json') as r:
        res = await r.json()
      embed = discord.Embed(title="Here's your Dank Meme , lol", color=random.randint(0,0xffffff))
      embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
      embed.set_footer(text=f'Requested by {ctx.author}',
                      icon_url = ctx.author.avatar_url)
    await ctx.send(embed=embed, content=None)

  @commands.command()
  async def slap(self, ctx, target : discord.Member):
    embed = discord.Embed(title=f'{ctx.author} just slapped {target}, oof!',
                          description = f"All of a sudden {ctx.author.mention} just slapped {target.mention} , oof <:riplol:858925516312543233>",
                          color=random.randint(0,0xffffff))
    gifs = ["https://cdn.discordapp.com/attachments/862194198753050635/862194288192258048/tenor_4.gif",
            "https://cdn.discordapp.com/attachments/862194198753050635/862194307200188426/tenor_3.gif",
            "https://cdn.discordapp.com/attachments/862194198753050635/862194308727570452/tenor_1.gif",
            "https://cdn.discordapp.com/attachments/862194198753050635/862194317552779314/tenor_2.gif"]
    embed.set_image(url=random.choice(gifs))
    await ctx.send(embed = embed)

  @slap.error
  async def slap_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f"Please mention the user to slap!")
      return




def setup(client):
  client.add_cog(Fun(client))