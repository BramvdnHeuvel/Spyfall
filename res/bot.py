import requests
import discord
from discord import Webhook, RequestsWebhookAdapter

WEBHOOK_ID = '580367084626903041'
WEBHOOK_TOKEN = 'GVrI0izMWErHOkJpNXqkesdJmGyMVDf0b4uiKJL2HQoepGPAJNyMgiPaZphqImbH2Ppz'

def send_public_message(content):
    webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN,\
     adapter=RequestsWebhookAdapter())

    webhook.send(content)

if __name__ == "__main__":
    send_public_message(input())