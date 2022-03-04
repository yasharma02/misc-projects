import discord
from discord.ext import commands

# bot = commands.Bot(command_prefix='/')
bot = discord.Client()

channel1id = 931663414156197889
channel2id = 939473536408485958

@bot.event
async def on_ready():
    print("Bot is ready")

# @bot.command()
# async def wassup(message):
#     await message.reply('sup!')

@bot.event
async def on_message(message):
    if message.channel.id == channel1id:
        channeltosend = bot.get_channel(channel2id)
        await channeltosend.send(message.content)

bot.run("OTM5NDY4MTk5MTkwMjMzMTU4")

# , embed=message.embeds[0]
