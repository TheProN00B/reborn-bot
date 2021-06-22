import discord
from discord.ext import commands
from discord.ext.commands.core import command

class Welcome(commands.Cog):

  def __init__(self, client):
    self.client = client
    self.welcomeMsg = "Hello there"

  #events
  @commands.Cog.listener()
  async def on_ready(self):
    print('Welcome Cog Loaded')

  @commands.Cog.listener()
  async def on_member_join(self, member):
    embed = discord.Embed(title='**Hello There!**',
                          description = f'Hi there {member.mention} , Welcome to {member.guild.name}. Make sure you have read <#834643663187083265> before chatting in the server. Also , for information related to the game , please head over to <#840909761322156042> and <#845152425739681843>. Thank you , enjoy your stay.',
                          color = discord.Colour.dark_gold())
    embed.set_image(url='https://cdn.discordapp.com/attachments/834643663187083266/855103653983682600/Logotype_blackbg.png')   
    await member.send(embed=embed)


def setup(client):
  client.add_cog(Welcome(client))