import logging
from discord import Webhook, RequestsWebhookAdapter


LOG_FORMAT = "%(asctime)s [%(levelname)s] - %(message)s"
logging.basicConfig(filename="debug.log", level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger()


def discordlog(string: str):
    from modules.env import env

    webhook = Webhook.from_url(env.FGN_DISCORD_LOG, adapter=RequestsWebhookAdapter())
    webhook.send(string)
