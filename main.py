import discord
from discord.ext import commands

# Anti-Raid Bot Implementation
class AntiRaidBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        # Check if the member is a bot
        if member.bot:
            await member.kick(reason='Kicked due to potential raid bot')
            print(f'Kicked {member.name} for being a bot')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def set_raid_mode(self, ctx, mode: bool):
        """
        Set the raid mode for the server.
        If mode is True, all new bot members will be kicked immediately.
        """
        # Store raid mode setting
        if mode:
            await ctx.send('Raid mode is now ON. Bots will be kicked.')
        else:
            await ctx.send('Raid mode is now OFF. Bots will not be kicked.')

# Adding the bot to the server
bot = commands.Bot(command_prefix='!')
bot.add_cog(AntiRaidBot(bot))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Replace 'YOUR_TOKEN_HERE' with your bot's token
bot.run('YOUR_TOKEN_HERE')