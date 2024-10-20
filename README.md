# Discord-Bot

## Introduction
This is a Discord bot that uses Discord API to load, combine, and ingest messages, and LlamaIndex to create and query indexes.

## Prerequisites
1. Python 3.12+
2. Discord bot token
3. OpenAI API key

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Swastikmohanty2k/Discord-bot
    cd Discord-bot
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Environment variables:**
    Create a `.env` file in the root directory and add your configuration details:
    ```env
    BOT_TOKEN=your-discord-bot-token
    OPENAI_API_KEY=your-openai-api-key
    CHANNEL_IDS=channel_id1,channel_id2
    ```

## Usage

1. Run the bot:
    ```sh
    python bot.py
    ```

2. Once the bot is online, you can interact with it using the `!chat <message>` command in the specified Discord channels.

## Bot Commands

- `!chat <message>`: Sends a message to the OpenAI API and returns the response.

## Acknowledgments

- [Discord.py](https://github.com/Rapptz/discord.py)
- [OpenAI](https://www.openai.com/)

