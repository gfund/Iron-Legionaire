import discord, datetime, time
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
class InfoCog(commands.Cog):
   def __init__(self, bot):
        self.bot = bot
   @commands.Cog.listener()
   async def on_message(self,message):
     pass
   @commands.command()
   async def ping(self,ctx):
    await ctx.send((str((self.bot.latency*1000))) + "ms")
   @commands.command()
   async def setpref(self,ctx,*,pref):
    self.bot.command_prefix=pref
    await ctx.send("Prefix is "+self.bot.command_prefix)
   

    
def setup(bot):
        bot.add_cog(InfoCog(bot))