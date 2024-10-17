import os
from openai import OpenAI
import discord
from discord.ext import commands
from llama_index.readers.discord import DiscordReader

# Initialize the Discord bot with intents
intents = discord.Intents.default()
intents.messages = True  # Ensure you have the messages intent enabled
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix='!', intents=intents)

# Set your OpenAI API key
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"))

# Set your Discord token
DISCORD_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_IDS = list(map(int, os.getenv("CHANNEL_IDS").split(",")))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def chat(ctx, *, message):
    try:
        
# Context for OpenAI
        context = "You are a Discord bot. Respond appropriately like a Discord bot will do."

        # Use ChatGPT API for a response
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": context,
                },
                {
                    "role": "user",
                    "content": message,
                }
            ],
            model="gpt-4o-mini",
        )
        
        # Send the response back to Discord
        await ctx.send(chat_completion.choices[0].message.content)
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

bot.run(DISCORD_TOKEN)
