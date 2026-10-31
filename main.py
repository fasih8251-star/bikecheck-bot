import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot Online: {bot.user}")

@bot.command()
async def olx(ctx, *, bike):
    await ctx.send(f"OLX par {bike} search kar raha hun...")

@bot.command()
async def reg(ctx, number):
    await ctx.send(f"{number} ka record check ho raha hai...")

bot.run(os.getenv("DISCORD_TOKEN"))
