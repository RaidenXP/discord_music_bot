import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

from help_cog import help_cog
from music_cog import music_cog

load_dotenv()
bot_token = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="!!")

bot.remove_command("help")

bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

bot.run(bot_token)