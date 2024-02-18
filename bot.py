import discord
from discord.ext import commands
from config import BOT_TOKEN
from commands import stats

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
intents.guild_messages

bot = commands.Bot(command_prefix=">", intents=intents, case_insensitive=True)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

bot.add_command(stats)
bot.run(BOT_TOKEN)
