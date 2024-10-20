import nest_asyncio
import discord
from discord.ext import commands
from utility import os, DiscordMessageIngestor, LlamaIndexEngine, load_and_cache_messages, handle_index 

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
DISCORD_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_IDS = list(map(int, os.getenv("CHANNEL_IDS").split(",")))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def chat(ctx, *, message):
    try:
        ingestor = DiscordMessageIngestor(discord_token=DISCORD_TOKEN, channel_ids=CHANNEL_IDS)
        messages = ingestor.load_messages()
        documents = ingestor.combine_messages(messages)
        engine = LlamaIndexEngine(api_key=os.getenv("OPENAI_API_KEY"))
        
        new_messages = load_and_cache_messages(documents)
        index = handle_index(engine, documents, new_messages)
        response = engine.query_index(index, message)
        
        await ctx.send(response)
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

if __name__ == "__main__":
    nest_asyncio.apply()
    bot.run(DISCORD_TOKEN)
