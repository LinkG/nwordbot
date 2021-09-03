import discord
import asyncpraw
import random
from collections import defaultdict
from threading import Timer
import dropbox
import pickle

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

datafile = open('data.txt', 'w')
dbx = dropbox.Dropbox('ehlGLhaDgTcAAAAAAAAAAcTolrHEUpn6kSiG_G-GoEm4NzxdGudXY2EGe98CMZNB')
count = defaultdict(int)
aliases = ["nigger", "nigga", "nig", "nibba", "nibber", "negro", "kneegar", "kneeger"]
client = discord.Client()
reddit = asyncpraw.Reddit(
  client_id = "M-NSwA7CoBeCqIp_eq9mKA",
  client_secret="cDjfp58VOjH2t_zc-kA7sQLisSwV6A",
  user_agent="reddit discord bot by u/Lank69G"
)

for line in datafile.readlines():
  u, c = line.split(',')
  count[u] = int(c)

def backupdata():
  datafile.truncate()
  mess = '\n'.join([str(x) + "," + str(count[x]) for x in count])
  datafile.write(mess)
  dbx.files_upload(datafile.read().encode('utf-8'), '\data.txt', mode=dropbox.files.WriteMode.overwrite)

rt = RepeatedTimer(600, backupdata)
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
    posts = subreddit.top(limit=60)
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
  
  if message.content.startswith('*ncount'):
    mess = '\n'.join([str(x) + " : " + str(count[x]) for x in count])
    await message.channel.send(mess)

  lower  = message.content.lower()
  for alias in aliases:
    if alias in lower:
      count[str(message.author)] += 1
      


client.run('NDI2NzQ1ODY4MDg3OTg0MTQ5.WrUMDw.a_lbbWRqve5pa5YPsGQifhvw5fc')
# client.run('NDI1NDk1Njg0NDk0NjU1NDk4.WrB_vA.o4t7MvhPGsafR0cBmbUGgOOQ2D0')