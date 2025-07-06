import discord
import markovify
import random

with open ("dataset.txt") as f:
    text = f.read()

markov = markovify.NewlineText(text)
markov = markov.compile(inplace=True)

class Dismarkov(discord.Client):
    
	async def on_ready(self):
	    print('logged in as', self.user)

	async def on_message(self, message):
		response = kevonzai.make_short_sentence(500)
	
		if message.content.startswith("<@YOUR_SELFBOT_USERID_HERE>"):
			author = message.author
			print(f"forced message sent, message sent by {author}")
			await message.reply(response)
			return

		decisions = random.randint(1, 5)
		author = message.author
		print(f"your random number is {decisions}, message sent by {author}")
		if decisions == 3:
			await message.reply(response)
			return

bot = Dismarkov()
bot.run('YOUR_TOKEN_HERE')
