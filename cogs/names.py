#names.py
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os
import json
import random
from datetime import datetime

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
GUILD_ID = discord.Object(id=1236510922625777715)

#Initializing JSON Name Storing
def load_names():
    if os.path.exists('name_stores.json'):
        with open('name_stores.json', 'r') as f:
            return json.load(f)
    else:
        return []
    
def save_names(names):
    with open('name_stores.json', 'w') as f:
        json.dump(names, f, indent=4)

#Discord Bot
class Names(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Add Name to 'name_stores.json' for storing.
    @app_commands.command(name="addname", description="Add a name to the name list")
    async def addname(self, interaction: discord.Interaction, addname: str):
        checkname = addname.lower()
        names = load_names()
        if checkname in names:
            await interaction.response.send_message(f"Name: **{addname}** already exists in file, name will not be added.")
        else:
            names.append(checkname)
            save_names(names)
            await interaction.response.send_message(f"Added Name: **{addname}** to file.")

    #Remove Name from 'name_stores.json'.
    @app_commands.command(name="removename", description="Remove a name from the name list")
    async def removename(self, interaction: discord.Interaction, removename: str):
        checkname = removename.lower()
        names = load_names()
        if checkname in names:
            names.remove(checkname)
            save_names(names)
            await interaction.response.send_message(f"Removed Name: **{removename}** from the list.")
        else:
            await interaction.response.send_message(f"Name: **{removename}** does not exist in the file, and will not be removed.")

    #Display Names from 'name_stores.json'.
    @app_commands.command(name="displaynames", description="Display all names from name list")
    async def displaynames(self, interaction: discord.Interaction):
        names = load_names()
        await interaction.response.send_message(names)

async def setup(bot):
    cog = Names(bot)
    #await bot.add_cog(cog, guilds = [GUILD_ID]) #Testing
    await bot.add_cog(cog) #Global
