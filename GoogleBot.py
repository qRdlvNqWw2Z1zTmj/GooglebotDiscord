import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from Scraper import Google

client = commands.Bot(command_prefix = "")

@client.event
async def on_ready():
    print("Bot connected succesfully!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msgUpper = message.content.upper()
    
    if msgUpper.startswith("GOOGLE") or msgUpper.startswith("ΓΟΟΓΛΕ"):
                args = message.content.split(" ")
                if len(args) > 1:
                        await client.send_typing(message.channel)
                        try:
                                searchQuery = " ".join(args[1:])
                                messageString = Google(searchQuery)
                                em = discord.Embed(title="Google results for {}".format(searchQuery), description=messageString, colour=0x8FACEf)
                                await client.send_message(message.channel,embed=em)
                        except:
                                await client.send_message(message.channel,"A problem occured while trying to get results from Google")
                else:
                        await client.send_message(message.channel,"https://www.google.com/")

client.run("Your token here")
