import os
import discord
import random
from pytube import YouTube

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

def getNumber(text):
    text = text[1]
    num1, num2 = text.split(",")
    return int(num1), int(num2)

@client.event
async def on_message(message):

    if message.content.startswith('$hello'):
        await message.channel.send('Hello, how are you?')

    if(message.content.startswith("$choose")):
        text = message.content.split(" ")
        text = text[1:]
        await message.channel.send(random.choice(text))

    if(message.content.startswith("$add")):
        text = message.content.split(" ")
        num1, num2 = getNumber(text)
        await message.channel.send(int(num1) + int(num2))   

    if(message.content.startswith("$sub")):
        text = message.content.split(" ")
        num1, num2 = getNumber(text)
        await message.channel.send(int(num1) - int(num2))

    if(message.content.startswith("$multiply")):
        text = message.content.split(" ")
        num1, num2 = getNumber(text)
        await message.channel.send(int(num1) * int(num2))
    
    if(message.content.startswith("$div")):
        text = message.content.split(" ")
        num1, num2 = getNumber(text)
        await message.channel.send(int(num1) + int(num2))
    
    if(message.content.startswith("$mod")):
        text = message.content.split(" ")
        num1, num2 = getNumber(text)
        await message.channel.send(int(num1) % int(num2))

client.run("<your discord developer token here>")