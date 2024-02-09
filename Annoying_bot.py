import discord
from discord.ext import commands

BOT_TOKEN = "Paste Bot Token here"
CHANNEL_ID = 123456789 #channel you wish the bot to communicate in
# enter victims names and Discord User_ID
NAME = int("user_id")
# For example JOE = 123456789101112

bot = commands.Bot(command_prefix='!' , intents=discord.Intents.all())

# ready message
@bot.event
async def on_ready():
    print("Cause Terror")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hey I'm ready to run")

# The actual process
@bot.command()
async def ruin (ctx, name: str, *, times: int ):
    # Currently the largest if statement I've made just to determine the user that you wish to hate you
    if name == "name":
        user_id = "user_id"
    elif name == "name2":
        user_id = "user_id2"
    else:
        user_id = " Make sure you spellled the name correctly"

# Send the message
    for _ in range(times):
        await ctx.send(f"<@{user_id}>")


bot.run(BOT_TOKEN)