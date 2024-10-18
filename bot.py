import os
import nest_asyncio
import discord
from discord.ext import commands
from llama_index.llms.openai import OpenAI
from classes import *

# Initialize the Discord bot with intents
intents = discord.Intents.default()
intents.messages = True  
intents.message_content = True  
bot = commands.Bot(command_prefix='!', intents=intents)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY")) 

#Discord token
DISCORD_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_IDS = list(map(int, os.getenv("CHANNEL_IDS").split(",")))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def chat(ctx, *, message):
    try:
        # Discord messages ingestion
        ingestor = DiscordMessageIngestor(discord_token=DISCORD_TOKEN, channel_ids=CHANNEL_IDS)
        messages = ingestor.load_messages()
        documents = ingestor.combine_messages(messages)

        # Create and query Llama Index object
        engine = LlamaIndexEngine(api_key=os.getenv("OPENAI_API_KEY"))
        index = engine.create_index(documents)
        response = engine.query_index(index, message)

        # Send the response back to Discord
        await ctx.send(response)
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

if __name__ == "__main__":
    nest_asyncio.apply()  # Apply nest_asyncio
    bot.run(DISCORD_TOKEN)
