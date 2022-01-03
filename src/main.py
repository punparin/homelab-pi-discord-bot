import os
from discord import Client, Intents, Embed
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from ClusterInformer import *

discord_token = os.getenv('DISCORD_TOKEN')
guild_id = int(os.getenv('DISCORD_GUILD_ID'))

bot = commands.Bot(command_prefix="!", intents=Intents.default())
slash = SlashCommand(bot, sync_commands=True)
clusterInformer = ClusterInformer()

@slash.slash(
    name="status",
    description="Show Pi cluster's status",
    guild_ids=[guild_id]
)
async def _test(ctx: SlashContext):
    embeds = clusterInformer.get_nodes_embeds()
    await ctx.send(embeds=embeds)

bot.run(discord_token)