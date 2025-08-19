# Korean Word of the Day AI Assistant

A Python application that fetches the Korean Word of the Day, generates AI-powered example sentences, and sends them to Discord via webhook.

## Features

- Fetches daily Korean words from Transparent.com's word-of-the-day service
- Uses OpenAI's API to generate contextual example sentences with varying difficulty levels
- Sends formatted messages to Discord channels via webhooks
- Provides English explanations and translations for Korean learners

## Requirements

- OpenAI API key
- Discord webhook URL

## Environment Variables

- `OPEN_AI_KEY`: Your OpenAI API key
- `DISCORD_WEBHOOK`: Discord webhook URL for message delivery

## Usage

Run the application to automatically fetch today's Korean word, generate AI examples, and send to Discord:

```bash
uv run src/kwod_ai/main.py
```

## Modules

- `kwod.py`: Fetches Korean Word of the Day from external API
- `ai.py`: Interfaces with OpenAI to generate example sentences and explanations
- `discord.py`: Handles Discord webhook message delivery
- `main.py`: Main application orchestrator
