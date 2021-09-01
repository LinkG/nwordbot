import discord
import asyncpraw
import random

client = discord.Client()
reddit = asyncpraw.Reddit(
  client_id = "M-NSwA7CoBeCqIp_eq9mKA",
  client_secret="cDjfp58VOjH2t_zc-kA7sQLisSwV6A",
  user_agent="reddit discord bot by u/Lank69G"
)
print(reddit.read_only)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):  
  if message.author == client.user or message.author.bot:
    return
  
  if message.content.startswith('*tr'):
    params = message.content.split()
    subreddit, nums = "gonewild", 1
    if len(params) > 1:
      subreddit = params[1]
    if len(params) > 2:
      nums = int(params[2])
    subreddit = await reddit.subreddit(subreddit)
    posts = subreddit.top(limit=30)
    posts_num = random.sample(range(1, 30), nums)
    posts_num.sort()
    i = 0
    async for post in posts:
      if len(posts_num) == 0:
        break
      if i == posts_num[0]:
        await message.channel.send(post.title)
        await message.channel.send(post.url)
        posts_num.pop(0)
      i += 1
    return

  if message.content.startswith('*hr'):
    params = message.content.split()
    subreddit, nums = "gonewild", 1
    if len(params) > 1:
      subreddit = params[1]
    if len(params) > 2:
      nums = int(params[2])
    subreddit = await reddit.subreddit(subreddit)
    posts = subreddit.hot(limit=30)
    posts_num = random.sample(range(1, 30), nums)
    posts_num.sort()
    i = 0
    async for post in posts:
      if len(posts_num) == 0:
        break
      if i == posts_num[0]:
        await message.channel.send(post.title)
        await message.channel.send(post.url)
        posts_num.pop(0)
      i += 1
    return


client.run('NDI2NzQ1ODY4MDg3OTg0MTQ5.WrUMDw.a_lbbWRqve5pa5YPsGQifhvw5fc')