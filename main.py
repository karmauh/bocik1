import discord
from bot_config import bocik1


if __name__ == '__main__':
    # Creating an instance and launching the bot
    intents = discord.Intents.default()
    intents.message_content = True
    intents.presences = True
    intents.members = True


    bot = bocik1(intents=intents)

    token = open('env/bot_token.env', 'r').read()
    bot.run(token)