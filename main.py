#main.py
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
GUILD_ID = discord.Object(id=1236510922625777715)

#Discord Bot
class Client(commands.Bot):
    async def setup_hook(self):
        self.tree.clear_commands(guild=GUILD_ID)
        await self.load_extension("cogs.names") #loads cog (calls the setup() function in "cogs.name")
        #await self.tree.sync(guild=GUILD_ID) #Testing
        await self.tree.sync(guild=GUILD_ID) #Global
        print("Ready!")

    async def on_ready(self):
        print(f"Logged on as {self.user}!")
    
intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix='!', intents=intents)

client.run(token)