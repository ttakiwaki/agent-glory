import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os
from datetime import datetime
from datetime import timedelta

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
#GUILD_ID = discord.Object(id=1489040034324811776) #Project Glory
GUILD_ID = discord.Object(id=1236510922625777715) #Test Server

#Discord Bot
class Bounty(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Create a new bounty
    @app_commands.command(name="newbounty", description="Add a new bounty - Difficulty (1-5) - Description (What one must do to complete this bounty)")
    async def newbounty(self, interaction: discord.Interaction, bountytitle: str, difficulty: int, description: str):
        stars = "⭐" * difficulty
        bounty_poster = interaction.user.id
        embed = discord.Embed(title=f"New Bounty: {bountytitle}",description=f"Bounty Poster: <@{bounty_poster}>", color=0x29AB87)
        embed.add_field(name="Bounty Description:", value=description, inline=True)
        embed.add_field(name="Difficulty:", value=f"{difficulty}/5 - {stars}", inline=True)
        expires_at = interaction.created_at + timedelta(hours=24) #expires in 24 hours
        timestamp = int(expires_at.timestamp())
        embed.add_field(name="Expiry:", value=f"Expires in <t:{timestamp}:R>", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=False)

async def setup(bot):
    cog = Bounty(bot)
    await bot.add_cog(cog, guilds = [GUILD_ID])