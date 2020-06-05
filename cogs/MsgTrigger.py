import discord
import asyncio
from discord.ext import commands

# NO COMMANDS HERE, only 1 listener for on_message()
# Designed only for Heavenly Realm
class MsgTrigger(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        msgContentLower = msg.content.lower()
        trigger = msgContentLower.split()

        # if msg was sent in DM (not in a guild)
        if msg.guild == None:
            return

        # if not Heavenly, then return
        if msg.guild.id != 256988924390408193:
            return

        try:
            botrole = msg.guild.get_role(272888325940051969)  # get bot role
            authorRoles = msg.author.roles
        except AttributeError:
            return

        # if msg from bots
        if botrole in authorRoles:
            return

        # Emote reaction triggers
        if "f" in trigger:
            femote = self.bot.get_emoji(471008964021059586)
            await msg.add_reaction(femote)
        if msgContentLower == "no u":
            await msg.channel.send("<:ThanosNOU:571052438619029524>")
        if "owo" in trigger:  # owo combo emotes!
            o1 = self.bot.get_emoji(490916040964964354)
            w2 = self.bot.get_emoji(490916041166159872)
            o3 = self.bot.get_emoji(490921532734963722)
            await msg.add_reaction(o1)
            await asyncio.sleep(0.1)
            await msg.add_reaction(w2)
            await asyncio.sleep(0.1)
            await msg.add_reaction(o3)
        if "220997668355178496" in msg.content:  # ping jiango
            emote = self.bot.get_emoji(560468390154731530)
            await msg.add_reaction(emote)
        if "436643551993004033" in msg.content or "thano" in msgContentLower:  # ping thanos
            t1 = self.bot.get_emoji(611039828003389440)
            t2 = self.bot.get_emoji(585580175031533597)
            await msg.add_reaction(t1)
            await msg.add_reaction(t2)
        if "gay" in msgContentLower:
            emote = self.bot.get_emoji(480073530466107392)
            await msg.add_reaction(emote)
        if "jojo" in msgContentLower or "jjba" in trigger:
            emote1 = self.bot.get_emoji(540669998725857290)
            emote2 = self.bot.get_emoji(540669998834909194)
            emote3 = self.bot.get_emoji(540669998809481276)
            await msg.add_reaction(emote1)
            await msg.add_reaction(emote2)
            await msg.add_reaction(emote3)
        if "deus" in msgContentLower or "vult" in msgContentLower:
            emote = self.bot.get_emoji(416072792560238592)
            await msg.add_reaction(emote)
        if "crusade" in msgContentLower or "templar" in msgContentLower:
            emote = self.bot.get_emoji(480073411532554242)
            await msg.add_reaction(emote)

        # unflip the damn table!
        if "(╯°□°）╯︵ ┻━┻" in msg.content:
            await msg.channel.send("┬─┬ ノ( ゜-゜ノ)")

        # howdy greeting - only for lurkers/newfags
        if (msgContentLower.startswith("hi") or msgContentLower.startswith("hey") or 
            msgContentLower.startswith("hello") or msgContentLower.startswith("hai") or 
            msgContentLower.startswith("howdy") or msgContentLower.startswith("sup")):

            demigod1 = msg.guild.get_role(257006648583913472)  # demigod I
            if demigod1 not in authorRoles:
                await msg.channel.send(f'{msg.author.mention} Howdy! <:TipHat:585587679798886411>')
                await msg.channel.send("<:GWjiangoPepeFedora:389447036329656323> <a:0PepeHowdy:594175419801141273>")


def setup(bot):
    bot.add_cog(MsgTrigger(bot))
