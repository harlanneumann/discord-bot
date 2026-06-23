import discord
import datetime

#when making a request call waitForRate
#wait for rate checks dict
#If that channel/guild combo doesnt exist, it makes it. This also means the limit should be fine so it passes
#If it does it checks the data there to determine if it can pass
#Repetedly check the above and global limit every .5 seconds until it can pass
#reurn nothing

class rateCheck():
    def __init__(self, bot:discord.Bot):
        self.bot = bot
        #A dict of tuples. The key is a str of f"{guildID}{channelID}" = 0 is the limit at that time, 1 is the cooldown
        self.rateData = {}

    async def waitForRate(self, channelID, guildID):
        try:
            item = self.rateData[str(f"{channelID}{guildID}")]
        except:
            pass
