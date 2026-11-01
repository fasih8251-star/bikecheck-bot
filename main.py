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
        await ctx.send("**Format:** !bikecheck Honda 125 BKA 1234")
        return
    
    score = random.randint(7, 10)
    
    d = details.lower()
    if "125" in d:
        min_price = "1,55,000 PKR"
        max_price = "2,20,000 PKR"
    elif "70" in d or "cd" in d:
        min_price = "80,000 PKR"
        max_price = "1,35,000 PKR"
    elif "150" in d:
        min_price = "2,80,000 PKR"
        max_price = "3,60,000 PKR"
    else:
        min_price = "1,00,000 PKR"
        max_price = "2,00,000 PKR"

    embed = discord.Embed(title="BikeCheck AI - Report", color=0x00ff00)
    embed.add_field(name="Bike Details", value=f"{details}", inline=False)
    embed.add_field(name="Rating", value=f"{score}/10", inline=True)
    embed.add_field(name="Status", value="Mashallah fit hai ✅", inline=False)
    embed.add_field(name="Minimum Price", value=min_price, inline=True)
    embed.add_field(name="Maximum Price", value=max_price, inline=True)
    
    await ctx.send(embed=embed)

keep_alive()
bot.run(os.environ['TOKEN'])
