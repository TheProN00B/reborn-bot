import discord
from discord.ext import commands
from discord.ext.commands.core import command


class Mod(commands.Cog):

  def __init__(self, client):
    self.client = client
    self.filtered_words = ["fuck", "nigga", "faggot", "asshole", "bastard"]



  #events
  @commands.Cog.listener()
  async def on_ready(self):
    print('Mod Cog Loaded')




  @commands.Cog.listener()
  async def on_message(self, message):
    for word in self.filtered_words:
     if word in message.content:
       if message.author.guild_permissions.administrator == True:
        return
       elif message.author.guild_permissions.administrator == False:
        await message.channel.send(f"Watch your language {message.author.mention}")
        await message.delete()
  
  #commands

  
  @commands.command(name='clear', aliases = ['purge'])
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx, amount : int):
    await ctx.channel.purge(limit=amount + 1)
    embed = discord.Embed(title = '**Purged!**' ,
                        description = f'Purged {amount} messages',
                        color = discord.Color.green())
    embed.set_footer(text=f"Requested by {ctx.author}",
                    icon_url= ctx.author.avatar_url)
    await ctx.send (embed=embed)


  @clear.error
  async def clear_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send(f"You don't have the permissions to run this command")
      return
    elif isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f"Please enter the number of messages to be deleted.")
      return


  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed = discord.Embed(title = '**Kicked!**',
                         description = f'Kicked {member.mention}. Reason : {reason}',
                         color = discord.Colour.orange())
    embed.set_footer(text=f"Requested by {ctx.author}",
                    icon_url= ctx.author.avatar_url)
    await ctx.send (embed=embed)

  @kick.error
  async def kick_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send(f"You don't have the permissions to run this command")
      return
    elif isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f"Please mention the user to be kicked.")
      return

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(title = '**Banned!**',
                     description = f'Banned {member.mention}. Reason : {reason}',
                     color = discord.Colour.red())
    embed.set_footer(text=f"Requested by {ctx.author}",
                    icon_url= ctx.author.avatar_url)
    await ctx.send (embed=embed)

  @ban.error
  async def ban_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send(f"You don't have the permissions to run this command")
      return
    elif isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f"Please mention the user to be banned.")
      return

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name , member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embed = discord.Embed(title = '**Unbanned!**',
                     description = f'Unbanned {user.name}#{user.discriminator}',
                     color = discord.Colour.green())
            embed.set_footer(text=f"Requested by {ctx.author}",
                    icon_url= ctx.author.avatar_url)
            await ctx.send (embed=embed)
            return

  @unban.error
  async def unban_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send(f"You don't have the permissions to run this command")
      return
    elif isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f"Please type the name of the user to be unbanned.")
      return




def setup(client):
  client.add_cog(Mod(client))