import minestat,time,discord

intents = discord.Intents().all()
bot = discord.Client(intents=intents)
token = "your_token"

ip = "play.server.lol"
port = 25565
channelid = 000000000000000000
checkdelay = 10

online_message = "🟩 Online!"
offline_message = "🟥 Offline!"

@bot.event
async def on_ready():
    channel = bot.get_channel(channelid)
    ms = minestat.MineStat(ip, port)
    if ms.online:
        if channel.name != online_message:
            await channel.edit(name=online_message)
    else:
        if channel.name != offline_message:
            await channel.edit(name=offline_message)
    while time.sleep(checkdelay):
        if ms.online:
            if channel.name != online_message:
                await channel.edit(name=online_message)
        else:
            if channel.name != offline_message:
                await channel.edit(name=offline_message)

bot.run(token)
