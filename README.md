# Dismarkov
A simple to setup + use Discord selfbot written in Python, that uses a Markov chain using markovify.
# Requirements
You will need Python 3.9+.                
You will need to install the packages `discord.py-self` and `markovify`.                
For the Markov chain, you will need a proper working dataset.                
For the Discord selfbot, you will need your Discord user token.            
# Setting up
First, git clone the repository.
`git clone https://github.com/realgreekster/dismarkov.git`
`cd dismarkov`
Then install the packages:
`pip install discord.py-self markovify`
Get a dataset, and rename it to `dataset.txt` if it hasnt been already.
Get your Discord user token, and input it into `bot.run`
Then just run the script:
`py -3 main.py` or `python3 main.py` (if you're on Linux)
If you see `logged in as (username)`, then you should be good to go!
# Known errors
## Empty message
This could possibly occur from an issue from the dataset, first print the Markov chain's response to see if it properly generates.
If it shows `None`, it could be an issue from the dataset.
