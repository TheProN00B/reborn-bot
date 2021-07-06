import discord
import os
from discord.ext import commands, tasks
from itertools import cycle
from discord import Intents
from discord.ext import commands

intents = Intents.default()
intents.members = True

client = commands.Bot(command_prefix='_', intents=intents)
status = cycle(['type _help for help.', 'PROJECT REBORN'])


client.remove_command('help')



@client.event

async def on_ready():
    status_change.start()
    print ('The Bot is ready')
    print(f'Logged in as: {client.user.name} ID: {client.user.id}')
    print(f'Online in Guilds:')
    for server in client.guilds:
        print(f'Guild name: {server.name}')
    
@tasks.loop(seconds=15)
async def status_change():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command(name = 'ping')
async def ping(ctx):
	await ctx.send (f'Ping! {round(client.latency * 1000)} ms')


client.run('TOKEN_YEETS_HERE')
