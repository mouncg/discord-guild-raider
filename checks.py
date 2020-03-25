import json

with open('config.json') as f:
    config = json.load(f)


def owner(ctx):
    return ctx.author.id in config["owner_ids"]
