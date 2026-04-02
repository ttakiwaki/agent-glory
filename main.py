#main.py
import discord
from discord.ext import commands, tasks
from discord import app_commands
from dotenv import load_dotenv
from datetime import time
import json
import os
import random
import pytz

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
GUILD_ID = discord.Object(id=1489040034324811776)

def load_names():
    if os.path.exists('name_stores.json'):
        with open('name_stores.json', 'r') as f:
            return json.load(f)
    else:
        return []

#Discord Bot
class Client(commands.Bot):
    async def setup_hook(self):
        self.tree.clear_commands(guild=GUILD_ID)
        await self.load_extension("cogs.names") #loads cog (calls the setup() function in "cogs.name")
        await self.tree.sync(guild=GUILD_ID) #Testing
        #await self.tree.sync(guild=GUILD_ID) #Global
        self.daily_name.start()
        print("Ready!")

    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    @tasks.loop(time=time(hour=0, minute=0, second=0, tzinfo=pytz.timezone("America/Vancouver")))
    async def daily_name(self):
        channel = self.get_channel(1489043508583989378)
        randomname = random.choice(load_names())
        embed = discord.Embed(title="🗓️ Name of the day", description=f"Today's name is {randomname}!", color=0x89CFF0)
        await channel.send(embed=embed)
    
intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix='!', intents=intents)

client.run(token)