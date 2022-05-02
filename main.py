import sys
import os
import discord
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()


@client.event
async def on_ready():
    print("bot is ready")
    # Search for my guild
    for guild in client.guilds:
        if guild.name == "my bot test":
            # found
            break
    else:
        print("Unable to find the guild")
        sys.exit(-1)
    # Search for bot channel
    for channel in guild.channels:
        if isinstance(channel, discord.TextChannel):
            if channel.name == "bot":
                # found
                break
    else:
        # not found ? Create it !
        channel = await guild.create_text_channel("bot")

    # And say hello on it
    await channel.send("Bot is ready !")


@client.event
async def on_message(message):

    if message.content == "ping":
        # Retrieve the number of ping in the last 200 messages
        messages = await message.channel.history(limit=200).flatten()
        nb_ping = len(list(filter(lambda m: m.content == "ping", messages)))
        await message.channel.send(f"pong ({nb_ping} times)")


if __name__ == "__main__":
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    if not DISCORD_TOKEN:
        print("No DISCORD_TOKEN env var found")
        sys.exit(-1)
    client.run(DISCORD_TOKEN)
