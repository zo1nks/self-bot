import discord
import asyncio

class Ace: 
     def __init__(self, bot):
          self.bot = bot
    
@commands.command()
async def r(self,ctx):
    await ctx.message.send(content="t!rep 394111231474270208")

@commands.command()
async def d(self,ctx):
    await ctx.message.send(content="t!daily 394111231474270208")
    
def setup(bot):
    bot.add_cog(Ace(bot))

    
    