import discord
import json
from discord.ext import commands

from checks import owner

with open("config.yaml") as f:
    config = json.load(f)


def load_exts(bot):
    try:
        for ext in bot.config["initial_extentions"]:
            bot.load_extension(f"cogs.{ext}")
    except Exception as e:
        print(e)


class yeeter(commands.AutoShardedBot):
    """
    the supreme fucker
    """

    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)
        self.owner_ids = []
        for i in config["owner_ids"]:
            if i not in self.owner_ids:
                self.owner_ids.append(i)
        self.config = config

    def get_config(self):
        with open("config.yaml") as ff:
            return json.load(f)




def get_config():
    with open("./config.json") as f:
        return json.load(f)


def get_prefix(bot, msg):
    cfg = get_config()  # type: dict
    if not msg.guild:
        return commands.when_mentioned_or(bot.default_prefix)(bot, msg)
    guild_id = str(msg.guild.id)
    if "prefix" not in cfg:
        cfg["prefix"] = {}
    prefixes = cfg["prefix"]
    if guild_id not in prefixes:
        return commands.when_mentioned_or(bot.default_prefix)(bot, msg)
    return commands.when_mentioned_or(prefixes[guild_id])(bot, msg)


bot = yeeter(command_prefix=get_prefix, case_insensitive=True)
bot.default_prefix = "-"

bot.add_check(owner)
load_exts(bot=bot)
if __name__ == "__main__":
    bot.run(bot.config["token"])
