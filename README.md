# Discord-bot

This is a Discord bot that utilizes the OpenAI API to provide chat responses using the ChatGPT model. The bot is implemented using the Discord.py library.

## Prerequisites

- Python 3.12+
- `discord.py` library
- OpenAI API key
- Discord bot token

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/Swastikmohanty2k/Discord-bot.git
    cd Discord-bot
    ```

2. Install the required Python packages:
    ```sh
    pip install discord.py openai 
    ```

3. Set up your environment variables:
    ```sh
    export OPENAI_API_KEY='your_openai_api_key'
    export BOT_TOKEN='your_discord_bot_token'
    export CHANNEL_IDS='comma_separated_channel_ids'
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

