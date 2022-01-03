import os
from discord import Client, Intents, Embed
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
from ClusterInformer import *
from ClusterController import *
from Utils import *

discord_token = os.getenv('DISCORD_TOKEN')
guild_id = int(os.getenv('DISCORD_GUILD_ID'))
channel_id = int(os.getenv('DISCORD_CHANNEL_ID'))

bot = commands.Bot(command_prefix="!", intents=Intents.default())
slash = SlashCommand(bot, sync_commands=True)
clusterInformer = ClusterInformer()
clusterController = ClusterController()

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@slash.slash(
    name="status",
    description="Show Pi cluster's status",
    guild_ids=[guild_id]
)
async def status(ctx: SlashContext):
    if ctx.channel_id != channel_id:
        return 
    embeds = clusterInformer.get_nodes_embeds()
    await ctx.send(embeds=embeds)

@slash.slash(
    name="reboot",
    description="Reboot Pi cluster or node",
    guild_ids=[guild_id],
    options=[
        create_option(
            name="target",
            description="Select a target to reboot",
            option_type=3,
            required=True,
            choices=get_discord_choices()
            )
        ])
async def reboot(ctx: SlashContext, target: str):
    if ctx.channel_id != channel_id:
        return
    embed = Embed(title=target, description="Sucessfully triggered reboot" ,color=0xE89332)
    await ctx.send(embeds=[embed])
    clusterController.reboot(target)

@slash.slash(
    name="shutdown",
    description="Shudown Pi cluster or node",
    guild_ids=[guild_id],
    options=[
        create_option(
            name="target",
            description="Select a target to shutdown",
            option_type=3,
            required=True,
            choices=get_discord_choices()
            )
        ])
async def shutdown(ctx: SlashContext, target: str):
    if ctx.channel_id != channel_id:
        return
    embed = Embed(title=target, description="Sucessfully triggered shutdown" ,color=0xE89332)
    await ctx.send(embeds=[embed])
    clusterController.shutdown(target)


if __name__ == "__main__":
    bot.run(discord_token)
