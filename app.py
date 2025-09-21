import os, discord
from discord.ext import commands

# Renderに環境変数で入れる（後で設定）
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("✅ Logged in as", bot.user)

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

if not TOKEN:
    print("❌ 環境変数 DISCORD_TOKEN が未設定です。")
else:
    bot.run(TOKEN)
