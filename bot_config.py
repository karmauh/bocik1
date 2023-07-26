import discord
import random

class bocik1(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0
        self.load_counter()  # Load counter value from memory
        
    # Load the counter value from a file (if it exists)
    def load_counter(self):
        try:
            with open("env\counter.txt", "r") as file:
                self.counter = int(file.read())
        except FileNotFoundError:
            pass

    # Write the counter value to a file
    def save_counter(self):
        with open("env\counter.txt", "w") as file:
            file.write(str(self.counter))

        
    async def on_ready(self):
        print(f'We have logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        content = message.content.lower()
        emojis = message.guild.emojis
        
        
        # We check if the message is sent by admin
        is_admin = False
        for role in message.author.roles:
            if role.permissions.administrator:
                is_admin = True
                break
            
        if is_admin:
            if content == '=ping':
                latency = round(self.latency * 1000) # seconds to milliseconds
                await message.channel.send(f"Pong: {latency}ms")
 
            
        # Test if bot works
        if '=test' in content:
            await message.channel.send(f'everything\'s fine {discord.utils.get(emojis, name="Okayge")}')
        
        # Counting uuh emojis 
        elif 'uuh' in content:
            self.counter += 1  # Increase counter after occurrence of the phrase "uuh"
            await message.channel.send(f'It\'s {self.counter} uuh')
            self.save_counter()  # Save the counter value to memory

            
        # Checking the syntax of the pyramid
        if content.startswith('=pyrimid'):
            args = content.split()  # Splitting the command into words
            if len(args) != 2 or not args[1].isdigit():
                await message.channel.send('Incorrect syntax. Use: pyrimid [max_length].')
                return
            
            max_length = int(args[1])
            if max_length < 1 or max_length > 15:
                await message.channel.send('The maximum length must be a number from 1 to 15.')
                return
            
            if emojis:
                # Selecting a random emoji
                random_emoji = random.choice(emojis)

                # Creating a pyramid from emojis
                pyramid = ""
                for i in range(1, max_length * 2):
                    if i <= max_length:
                        pyramid += str(random_emoji) * i + "\n"
                    else:
                        pyramid += str(random_emoji) * (max_length * 2 - i) + "\n"

                await message.channel.send(pyramid)
                