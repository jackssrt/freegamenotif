from datetime import datetime
from discord import Webhook, RequestsWebhookAdapter, embeds
from modules.classes import Game
from modules.env import env
import discord
import os


def notify(game: Game):
    if env.FGN_DISCORD_URL is None:
        print("|   |   |   Wont run because env FGN_DISCORD_URL isnt set")
        return

    embed = discord.embeds.Embed()
    embed.title = game.title
    embed.description = game.desc
    embed.set_author(
        name=game.developer if game.developer else "[FGN] Unknown Developer"
    )
    embed.url = game.link
    embed.color = discord.Color.from_rgb(255, 255, 0)
    embed.set_footer(text=f"freegamenotif • ID: {game.id}")
    embed.timestamp = datetime.utcnow()
    embed.set_thumbnail(url=game.image)
    webhook = Webhook.from_url(env.FGN_DISCORD_URL, adapter=RequestsWebhookAdapter())
    webhook.send("@everyone", embed=embed)
