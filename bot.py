import discord
from discord.ext import commands
from config import BOT_TOKEN, TWITCH_URL, COMMAND_PREFIX
from ranked import ranked, help
from casual import casual

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents, case_insensitive=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="R6 Stats", url=TWITCH_URL))
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title="Unknown Command!",
            description=f"The command you entered does not exist. `{COMMAND_PREFIX}help to view a list of commands`.",
            color=0xFF0000 
        )
        await ctx.send(embed=embed)

bot.add_command(ranked)
bot.add_command(help)
bot.add_command(casual)
bot.run(BOT_TOKEN)
