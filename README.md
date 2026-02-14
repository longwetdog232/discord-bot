# Discord Anti-Raid Bot

A Python-based Discord bot designed to protect your server from raid attacks by detecting and preventing mass joins and spam.

## Features

- **Raid Detection**: Automatically detects when multiple users join within a short timeframe
- **Spam Prevention**: Tracks and mutes users who send too many messages too quickly
- **Auto-Kick**: Kicks potential raid accounts automatically
- **Configurable Thresholds**: Easy to adjust raid and spam detection parameters

## Installation

1. Clone the repository
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file based on `.env.example`:
    ```bash
    cp .env.example .env
    ```

4. Add your Discord bot token to `.env`:
    ```
    DISCORD_TOKEN=your_bot_token_here
    ```

## Configuration

Edit `config.py` to adjust thresholds:

- `RAID_JOIN_THRESHOLD`: Number of joins to trigger raid detection (default: 10)
- `RAID_JOIN_THRESHOLD_SECONDS`: Time window for counting joins (default: 30 seconds)
- `SPAM_MESSAGE_THRESHOLD`: Number of messages to trigger spam detection (default: 5)
- `SPAM_CHECK_SECONDS`: Time window for counting messages (default: 10 seconds)
- `MUTE_DURATION_SECONDS`: How long to mute spammers (default: 300 seconds)

## Usage

1. Start the bot:
    ```bash
    python main.py
    ```

2. Use admin commands:
- `!antiraid` - Check bot status and current settings
- `!clearraid` - Clear raid history

## Permissions

The bot requires the following permissions:
- Kick Members
- Manage Messages
- Mute Members
- Read Message History

## License

MIT