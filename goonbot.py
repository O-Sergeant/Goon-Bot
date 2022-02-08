# bot.py
import os

import discord
from dotenv import load_dotenv

import crypto

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(self, message):
    items = message.content.split()
    print(items)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!huge'):
        response = '<:cone:913911268522491934>'
        await message.channel.send(response)

    #if message.content.startswith('G BTC'):
     #   response = f'${round(crypto.price(),2)} USD'
      #  await message.channel.send(response)

    if message.content.startswith('g magic'):
        response = 'fuck you Tei'
        await message.channel.send(response)

    if message.content.startswith('!kripp'):
        response = 'HEYGUYSHOWSITGOINGKRIPPARRIANHERE'
        await message.channel.send(response)

    if message.content.startswith('Hey Ned'):
        response = 'Howdily-doodily, neighborino'
        await message.channel.send(response)

    if message.content.lower().startswith('g '):
        symbol = message.content.lower().replace('g ','')
        coin_list = crypto.coin_list(symbol)
        id = coin_list['data'][0]['id']
        response = f'${round(crypto.price(id),4)} USD'
        await message.channel.send(response)

    if message.content.startswith('g ollie'):

        for
        response = 'Howdily-doodily, neighborino'
        await message.channel.send(response)





client.run(TOKEN)


