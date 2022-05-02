import discord
import os
import requests
import json
client = discord.Client()

sad_words=["sad", "depressed", "unhappy", "sucks", "end this pain"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data=json.loads(response.text)
  quote=json_data[0]['q']+" -"+json_data[0]['a']
  return(quote)
@client.event
async def on_ready():
  print("Read to go! We are {0.user}".format(client))
@client.event
async def on_message(message):
  if message.author==client.user:
      return
  if message.content.startswith('$quote'):
    quote= get_quote()
    await message.channel.send(quote)


client.run(os.getenv('TOKEN')) #env variable for token