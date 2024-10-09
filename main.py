import discord, re, json, asyncio, random
from discord.ext import commands

bot = commands.Bot(command_prefix="noprefixidkshit")

@bot.event
async def on_ready():
    print(f"[READY] Logged in as {bot.user}")

config = json.load(open("config.json"))

@bot.event
async def on_message(m:discord.Message):
    if not m.guild:
       return
   
    if m.author.id == 854233015475109888 and str(m.channel.id) in config['channels']:
      if "Best name:" in m.content:
        match = re.search(r"Best name: (\w+)", m.content)
        if match:
           print(f"[SUCCESS] Detected best name: {match.group(1)}")
           async with m.channel.typing():
              await asyncio.sleep(random.choice([1, 1.2, 1.4, 1.6, 1.8, 2, 2.2]))
           await m.channel.send(f"<@716390085896962058> c {match.group(1).lower()}")
        else:
            print(f"[ERROR] Failed to detect best name")
      else:
         match = re.search(r"^(\w+): \d+\.\d+%", m.content)
         if match:
            print(f"[SUCCESS] Detected name: {match.group(1)}")
            async with m.channel.typing():
              await asyncio.sleep(random.choice([1, 1.2, 1.4, 1.6, 1.8, 2, 2.2]))
            await m.channel.send(f"<@716390085896962058> c {match.group(1).lower()}")
         else:
            print(f"[ERROR] Failed to detect name")


bot.run(config['token'])