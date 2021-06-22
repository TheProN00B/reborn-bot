import discord
from discord import colour
from discord.ext import commands
from discord.ext.commands.core import command

class Help(commands.Cog):

  def __init__(self, client):
    self.client = client
    
  #events
  @commands.Cog.listener()
  async def on_ready(self):
    print('Help Cog Loaded')

  @commands.group(invoke_without_command=True)
  async def help(self, ctx):
    embed = discord.Embed(title = '**Help**',
                          description = 'Prefix for the bot is `_`. \n Use _help <command> on an extend help on a command',
                          color = discord.Colour.greyple())

    embed.add_field(name = 'Moderation', value = '`clear/purge , kick , ban , unban`')
    embed.add_field(name = 'Bot', value = '`ping , aboutbot/botinfo`')
    embed.add_field(name = 'Server', value = '`hello , faq`')
    embed.add_field(name = 'Fun', value = '`8ball , avatar/pfp/av`')
    await ctx.send(embed=embed)

  @help.command(aliases = ['purge'])
  async def clear(self, ctx):
    embed = discord.Embed(title = '**Help**',
                          description = 'Clears messages from a channel.',
                          colour = discord.Colour.greyple())
    embed.add_field(name = 'Synatx' , value = '`_purge <number of messages>`')
    await ctx.send(embed=embed)

  @help.command()
  async def kick(self, ctx):
    embed = discord.Embed(title = '**Help**',
                          description = 'Kicks a member from the server.',
                          colour = discord.Colour.greyple())
    embed.add_field(name = 'Synatx' , value = '`_kick <@member> [reason]`')
    await ctx.send(embed=embed)

  @help.command()
  async def ban(self, ctx):
    embed = discord.Embed(title = '**Help**',
                          description = 'Bans a member from the server.',
                          colour = discord.Colour.greyple())
    embed.add_field(name = 'Synatx' , value = '`_ban <@member> [reason]`')
    await ctx.send(embed=embed)

  @help.command()
  async def unban(self, ctx):
    embed = discord.Embed(title = '**Help**',
                          description = 'Unbans a member from the server.',
                          colour = discord.Colour.greyple())
    embed.add_field(name = 'Synatx' , value = '`_unban <member#1234>`')
    await ctx.send(embed=embed)

  @help.command()
  async def ping(self, ctx):
    embed = discord.Embed(title = '**Help**',
                          description = 'Tells the bot latency.',
                          colour = discord.Colour.greyple())
    embed.add_field(name = 'Synatx' , value = '`_ping`')
    await ctx.send(embed=embed)

  @help.command(aliases=['botinfo'])
  async def aboutbot(self, ctx):
    embed = discord.Embed(title = '**Help**',
                          description = 'Shows information about the bot.',
                          colour = discord.Colour.greyple())
    embed.add_field(name = 'Synatx' , value = '`_aboutbot`')
    await ctx.send(embed=embed)

  @help.command()
  async def hello(self, ctx):
    embed = discord.Embed(title = '**Help**',
                          description = 'Basic hello command for new members.',
                          colour = discord.Colour.greyple())
    embed.add_field(name = 'Synatx' , value = '`_hello`')
    await ctx.send(embed=embed)

  @help.command()
  async def faq(self, ctx):
    embed = discord.Embed(title = '**Help**',
                          description = 'Shows some answered FAQs related to the game and development.',
                          colour = discord.Colour.greyple())
    embed.add_field(name = 'Synatx' , value = '`_faq`')
    await ctx.send(embed=embed)

  @help.command(name='8ball')
  async def eightball(self, ctx):
    embed = discord.Embed(title = '**Help**',
                          description = 'Just a fun 8ball command.',
                          colour = discord.Colour.greyple())
    embed.add_field(name = 'Synatx' , value = '`_8ball <question>`')
    await ctx.send(embed=embed)

  @help.command(aliases=['av','pfp'])
  async def avatar(self, ctx):
    embed = discord.Embed(title = '**Help**',
                          description = 'Gives user profile picture.',
                          colour = discord.Colour.greyple())
    embed.add_field(name = 'Synatx' , value = '`_av [@mention]`')
    await ctx.send(embed=embed)






def setup(client):
  client.add_cog(Help(client))