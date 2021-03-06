import discord
import asyncio
from discord.ext import commands
import random
from langdetect import detect
from langdetect import lang_detect_exception
import emoji

# NO COMMANDS HERE, only 1 listener for on_message()
# Designed only for Heavenly Realm


class AutoMod1(commands.Cog):

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
            authorTopRole = msg.author.top_role  # member's highest role
            viprole = msg.guild.get_role(388850225881546752)
            botrole = msg.guild.get_role(272888325940051969)
            demigodX = msg.guild.get_role(340275236865966090) # demigod X
            demigodV = msg.guild.get_role(310541971179700224)  # demigod v
            demigod1 = msg.guild.get_role(257006648583913472) # demigod 1
            authorRoles = msg.author.roles
        except AttributeError:
            return

        # if msg from bots
        if botrole in authorRoles:
            return

        # general/media/game chat auto mod, VIP+ are immune
        if (msg.channel.id == 568437502680104960
            or msg.channel.id == 289170611849396225
                or msg.channel.id == 256993917461987328) and authorTopRole < viprole:
            text: str = msg.content
            msglist = text.split()

            # Detect non-english
            try:
                detected = detect(text)
            except lang_detect_exception.LangDetectException:
                detected = ''
            
            if (len(msglist) >= 10 and detected != "en") or \
                (not text.isascii() and not any(em in text for em in emoji.UNICODE_EMOJI) and
                 "’" not in text and "‘" not in text):
                # not ascii && no unicode emoji in text
                try:
                    await msg.delete()
                    emb = discord.Embed(title="Make sure your msg only contains ASCII codes",
                                            url="https://en.wikipedia.org/wiki/ASCII",
                                            description="(VIP+ are immune to this auto-mod)")
                    outputMsg = (f'{msg.author.mention} Please use English to chat here. '
                                + 'You may use other langs in <#309478950772670470>')
                    await msg.channel.send(outputMsg, embed=emb)
                    return
                except discord.HTTPException:
                    pass
            # all cap detection, ignore custom emotes
            if len(text) >= 10 and text.isupper() and "<" not in text and ">" not in text:
                await msg.channel.send(f'{msg.author.mention} ||shut yo bitchass up|| lmao', 
                embed = discord.Embed().set_image(url="https://i.imgur.com/LoK9MJD.png"))

        # Auto moderate emote chat  #Only custom/global emotes allowed
        if msg.channel.id == 459893562130300928:
            if msgContentLower.startswith('<:') and msgContentLower.endswith('>'):
                pass
            elif msgContentLower.startswith('<a:') and msgContentLower.endswith('>'):
                pass
            elif all(em in emoji.UNICODE_EMOJI for em in msg.content):
                pass
            else:
                try:
                    await msg.delete()
                    channel = self.bot.get_channel(
                        416385919919194113)  # spam channel
                    await channel.send(f'{msg.author.mention} Your msg was deleted in <#459893562130300928> '
                                    + '(it is only for ***CUSTOM EMOTES***)')
                    return
                except discord.HTTPException:
                    pass

        # delete Nitro or gift links
        if "discord.gift/" in msgContentLower:
            try:
                await msg.delete()
                return
            except discord.HTTPException:
                pass

        # NOTICE: no more global emotes
        if ("emot" in msgContentLower or "emoj" in msgContentLower) and \
            ("how" in msgContentLower or "global" in msgContentLower or "?" in msgContentLower or
             "where" in msgContentLower or "what" in msgContentLower or "why" in msgContentLower or
             "which" in msgContentLower):

            if (demigodX not in authorRoles or demigodV >= authorTopRole):
                # buy nitro meme
                meme = discord.Embed().set_image(url="https://i.imgur.com/0HOJ9YY.png")
                notice = (f'{msg.author.mention} Sorry. Discord Inc. removed GW (global) emotes '
                + 'so more users buy Nitro <:CrazyChamp:702640155432976475>\n'
                + 'Welcome to the era of corporations fucking everyone for more profit <:Merchant2:561548871457832970>')
                
                try:
                    await msg.channel.send(notice, embed=meme)
                except discord.HTTPException:
                    pass
                

def setup(bot):
    bot.add_cog(AutoMod1(bot))
