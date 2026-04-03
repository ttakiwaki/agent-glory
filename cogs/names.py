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
#GUILD_ID = discord.Object(id=1489040034324811776) #Project Glory
GUILD_ID = discord.Object(id=1236510922625777715) #Test Server

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
            embed = discord.Embed(title="❌ Name Already Exists", description=f"Name: **{addname}** already exists in file, name will not be added.", color=0xe74c3c)
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            names.append(checkname)
            save_names(names)
            embed = discord.Embed(title="✅ Name Added", description=f"Added Name: **{addname}** to file.", color=0x2ecc71)
            await interaction.response.send_message(embed=embed, ephemeral=True)

    #Remove Name from 'name_stores.json'.
    @app_commands.command(name="removename", description="Remove a name from the name list")
    async def removename(self, interaction: discord.Interaction, removename: str):
        checkname = removename.lower()
        names = load_names()
        if checkname in names:
            names.remove(checkname)
            save_names(names)
            embed = discord.Embed(title="✅ Name Removed", description=f"Removed Name: **{removename}** from the list.", color=0x2ecc71)
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            embed = discord.Embed(title="❌ Name Doesn't Exist", description=f"Name: **{removename}** does not exist in the file, and will not be removed.", color=0xe74c3c)
            await interaction.response.send_message(embed=embed, ephemeral=True)

    #Display Names from 'name_stores.json'.
    @app_commands.command(name="displaynames", description="Exports a JSON file containing all names")
    async def displaynames(self, interaction: discord.Interaction):
        await interaction.response.send_message(file=discord.File("name_stores.json"), ephemeral=True)

    #Pick random name from 'name_stores.json'.
    @app_commands.command(name="randomname", description="Picks a random name from name list")
    async def randomname(self, interaction: discord.Interaction):
        names = load_names()
        picked_name = random.choice(names)
        embed = discord.Embed(title="🎲 Random Name",description=f"**{picked_name}**", color=0x89CFF0)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    #Test Command
    @app_commands.command(name="testcommand", description="Test to see if Agent Glory is working")
    async def testcommand(self, interaction: discord.Interaction):
        await interaction.response.send_message("Agent Glory is online")

    #Search for name in 'name_stores.json'.
    @app_commands.command(name="searchname", description="Search to check if a name is on the list")
    async def searchname(self, interaction: discord.Interaction, searchname: str):
        names = load_names()
        if searchname in names:
            embed = discord.Embed(title="✅ Name Exists", description=f"The name **{searchname.capitalize()}** is on the list.", color=0x2ecc71)
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            embed = discord.Embed(title="❌ Name Doesn't Exist", description=f"Name: **{searchname.capitalize()}** does not exist on the list.", color=0xe74c3c)
            await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot):   
    cog = Names(bot)
    await bot.add_cog(cog, guilds = [GUILD_ID])
