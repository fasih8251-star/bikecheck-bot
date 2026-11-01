import discord
from discord.ext import commands
import os
import random
from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home():
    return "BikeCheck AI is Online 24/7!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot Online 24/7: {bot.user}")

@bot.command(name="bikecheck")
async def bikecheck(ctx, *, details=""):
    if details == "":
        await ctx.send("**Format:** `!bikecheck Honda 125 BKA 1234`")
        return
    score = random.randint(7, 10)
    embed = discord.Embed(title="BikeCheck AI - Report", color=0x00ff00)
    embed.add_field(name="Bike Details", value=f"```{details}```", inline=False)
    embed.add_field(name="Rating", value=f"**{score}/10**", inline=True)
    embed.add_field(name="Status", value="Mashallah fit hai ✅", inline=False)
    await ctx.send(embed=embed)

keep_alive()
bot.run(os.environ['TOKEN'])
