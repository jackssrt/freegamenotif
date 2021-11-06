from datetime import datetime
from discord import Webhook, RequestsWebhookAdapter, embeds
from classes import Game
import discord
import os
WEBHOOK_URL = os.getenv("FGN_DISCORD_URL", None)


def notify(game: Game):
    if WEBHOOK_URL is None:
        print("|   |   |   Wont run because env FGN_DISCORD_URL isnt set")
        return

    embed = discord.embeds.Embed()
    embed.title = game.title
    embed.description = game.desc
    if game.developer:
        embed.set_author(name=game.developer)
    else:
        embed.set_author(name="[freegamenotif] Unknown Developer")
    embed.url = game.link
    embed.color = discord.Color.from_rgb(255, 255, 0)
    embed.set_footer(text="freegamenotif")
    embed.timestamp = datetime.now()
    embed.set_thumbnail(url=game.image)
    webhook = Webhook.from_url(
        WEBHOOK_URL, adapter=RequestsWebhookAdapter())
    webhook.send("@everyone", embed=embed)
