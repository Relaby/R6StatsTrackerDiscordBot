import discord
from discord.ext import commands
import config
from config import COMMAND_PREFIX
from siegeapi import Auth

async def get_player_info(platform, name):
    try:
        auth = Auth(config.UBISOFT_EMAIL, config.UBISOFT_PASSWORD)
        player = await auth.get_player(platform=platform, name=name)

        info = {
            "Name": player.name,
            "Profile pic URL": player.profile_pic_url
        }

        await player.load_ranked_v2()
        if hasattr(player, "casual_profile"):
            info["Wins"] = player.casual_profile.wins
            info["Losses"] = player.casual_profile.losses
            info["WL"] = info["Wins"] / info["Losses"] if info["Losses"] > 0 else info["Wins"]
            info["Kills"] = player.casual_profile.kills
            info["Deaths"] = player.casual_profile.deaths
            info["KD"] = info["Kills"] / info["Deaths"] if info["Deaths"] > 0 else info["Kills"]

        await player.load_playtime()
        info["Name"] = player.name
        info["UID"] = player.uid
        info["Level"] = player.level

        await auth.close()
        return info
    except Exception as e:
        print(f"Error fetching player information: {e}")
        return None

@commands.command()
async def casual(ctx, *, name: str = None):
    if name is None:
        embed = discord.Embed(
            title="Error",
            description=f"You must enter a username. Please use the command like this: `{COMMAND_PREFIX}casual [username]`.",
            color=0xFF0000 
        )
        await ctx.send(embed=embed)
        return
    
    api_name = name.replace("-", " ")

    platform_names = {"xbl": "Xbox", "uplay": "PC", "psn": "PlayStation"}

    platform_colors = {
        "xbl": 0x107C10,
        "uplay": 0xF4D03F,
        "psn": 0x005EA8
    }

    found = False
    for platform in ["xbl", "uplay", "psn"]:
        info = await get_player_info(platform, api_name)
        if info:
            found = True
            profile_url = f"https://r6.tracker.network/profile/{platform}/{name}"

            embed = discord.Embed(title=f"{info['Name']}'s Profile ({platform_names[platform]})", url=profile_url,
                                  color=platform_colors[platform])

            embed.set_thumbnail(url=info["Profile pic URL"])

            if "Wins" in info:
                win_loss_text = f"> Won: {info['Wins']}\n> Lost: {info['Losses']}\n> WL: {info['WL']:.2f}"
                embed.add_field(name="■ W/L", value=win_loss_text, inline=True)


                kill_death_text = f"> Kills: {info['Kills']}\n> Deaths: {info['Deaths']}\n> KD: {info['KD']:.2f}"
                embed.add_field(name="■ K/D", value=kill_death_text, inline=True)

                general_text = f"> Name: {info['Name']}\n> Level: {info['Level']}\n> UID: {info['UID']}"
                embed.add_field(name="■ General", value=general_text, inline=True)

            embed.set_footer(text=f"Requested by {ctx.author.name} *Seasonal stats only*")

            await ctx.send(embed=embed)
            break
    
    if not found:
        embed = discord.Embed(
            title="No Results",
            description=f"No player found with the username '{name}'.",
            color=0xFF0000  # Red color
        )
        await ctx.send(embed=embed)