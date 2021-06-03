import os

from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat

from helpers.filters import command, other_filters, other_filters2


## ~ Simple Config ~ ##
FRIEND_BOT = "hsk_the_editor"
USER_ACCNAME = os.getenv("USER_ACCNAME", "hsk_the_editor")


@Client.on_message(command(["start", "start@Music_for_hsk_bot "]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Hello {message.from_user.first_name} 🤝!</b>

എന്റെ പേര്‌ SOMAN music bot. എന്റെ മുതലാളി **@{FRIEND_BOT}** പറഞ്ഞിട്ടുണ്ട് വേറെ ഗ്രൂപ്പില്‍ ഒന്നും പാടാന്‍ പോവരുതെന്ന് 😏️.

എന്നെ നിനക്ക് ഉപയോഗിക്കണം എങ്കിൽ എന്റെ അണ്ണൻ വിചാരിക്കണം അതോണ്ട് മിണ്ടാതെ പൊക്കോ 😁.

My Owner 👉 <b>@hsk_the_editor</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add Me To Your Group ➕", url="https://telegra.ph/file/0e88dd7060cc6e8fd1715.jpg"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🤨️ How To Use Me 🤨️", url="https://t.me/somanFUNchannel/3"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔰️How To ENJOY 🔰️", url="https://t.me/somanFUNchannel/4"
                    ),
                    InlineKeyboardButton(
                        "⚡MY BOSS⚡", url="https://t.me/hsk_the_editor"
                    )
                ]
            ]
        )
    )
    
    
@Client.on_message(command(["help", "help@Music_for_hsk_bot "]))
async def help(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>

Nanbaa! നിനക്ക് എന്തെങ്കിലും സഹായം വേണോ! 🤔️ എനിക്കറിയാം വേണമെന്ന്! 😂

How To Use Me? 🧐️

<b> 1. @{USER_ACCNAME} വിചാരിച്ചാൽ മാത്രമെ നിനക്ക് എന്നെ ഉപയോഗിക്കാൻ പറ്റൂ! അതുകൊണ്ട്‌ ചുമ്മാ എന്നെ നോക്കി നിന്ന് സമയം കളയണ്ട🙂

 2. എനിക്ക് ഈ ഗ്രൂപ്പില്‍ പാടാന്‍ മാത്രമേ അനുവാദം ഉള്ളു 🤝😊! </b>

 
**For More Info or Know about My Commands Just Click On "♻️ Additional Help ♻️" Button!**

My Owner 👉 <b>@hsk_the_editor</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "♻️ Additional Help ♻️", callback_data="cmdlistcb"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔰️ Update Channel 🔰️", url="https://t.me/somanFUNchannel/4"
                    ),
                    InlineKeyboardButton(
                        "⚡MY BOSS⚡", url="https://t.me/hsk_the_editor"
                    )
                ]
            ]
        )
    )

    
@Client.on_message(command(["cmdlist", "cmdlist@Music_for_hsk_bot "]))
async def cmdlist(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>

Here is the list of available commands but it is only for @hsk_the_editor ! 😃️

• **Group Admin Only Commands 👮 ✓,**

 ➲ <code>/play</code> - Reply to supported url or "/play supported url"
 ➲ <code>/skip</code> - Skip currenly playing song!
 ➲ <code>/pause</code> - Pause currently playing song!
 ➲ <code>/resume</code> - Resume currently pushed song!
 ➲ <code>/mute</code> - Mutes Streamer!
 ➲ <code>/unmute</code> - Unmutes streamer!
 ➲ <code>/joingrp</code> - To Add Streamer Account To Your Group!
 ➲ <code>/leavegrp</code> - To Remove Streamer Account From Your Group!


• **Group Members Commands 👮 ✓,**

 ➲ <code>/vc</code> - Give voice chat link of your group! (Only For Public Groups)
 ➲ <code>/yts (song name)</code> - Download song by it's name!
 ➲ <code>/ytvid (song name)</code> - Download Videos From YouTube!
 ➲ <code>/saavn (song name)</code> - Download Songs From Saavn!
 ➲ <code>/deezer (song namme)</code> - Download Songs From Deezer!
 
**❌ പാട്ട് പാടിക്കൊണ്ട് നില്‍ക്കുമ്പോ Voice chat നിര്‍ത്തിയാല്‍ എന്റെ സ്വഭാവം മാറും😬 ❌**
 
Made with Power⚡ by **@hsk_the_editor**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👀️ Supported Sites 👀️", url="https://ytdl-org.github.io/youtube-dl/supportedsites.html"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚡MY BOSS⚡", url="https://t.me/hsk_the_editor"
                    )
                ],
                [
                    InlineKeyboardButton(
                    "🔰️How To ENJOY 🔰️", url="https://t.me/somanFUNchannel/4"
                    )
                ]
            ]
        )
    )
   
    
@Client.on_message(command("credits") & other_filters2)
async def credits2(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>

__Note!__ ⚠️: This Project Is <b>Not Fully Owned By Me</b> !

Credits To,

<b><a href="https://github.com/CallsMusic">CallsMusic</a></b> - For Callsmusic (Main Code ❤️) !
<b>Mr Dark Prince</b> - For Yt Download!
<b>TheHamkercat</b> - For Deezer and Saavn Download!
<b>TeamDaisyX</b>
<b>N A C</b> - For <code>/vc</code> Command

Made with Power⚡ by **@hsk_the_editor**

Respect To Code Owners! Not To Me!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰️How To ENJOY 🔰️", url="https://t.me/somanFUNchannel/4"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚡MY BOSS⚡", url="https://t.me/hsk_the_editor"
                    )
                ]
            ]
        )
    )   


@Client.on_message(command(["vc", "vc@Music_for_hsk_bot "]) & other_filters)
async def vc(_, message: Message):
    VC_LINK = f"https://t.me/{message.chat.username}?voicechat"
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>


             😌️  **Voice Chat Link** 😌️
____________________------------______________________

👉️ [Here Is Your Voice Chat Link](https://t.me/{message.chat.username}?voicechat) 👈️
____________________------------______________________

Enjoy!😌️❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "↗️ Share Voice Chat Invitation ↗️", url=f"https://t.me/share/url?url=**Join%20Our%20Group%20Voice%20Chat%20😉%20%20{VC_LINK}%20❤️**"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔰️ Update Channel 🔰️", url="https://t.me/somanFUNchannel/4"
                    ),
                    InlineKeyboardButton(
                        "⚡MY BOSS⚡", url="https://t.me/hsk_the_editor"
                    )
                ]
            ]
        )
    )

    
@Client.on_message(command(["search", "search@Music_for_hsk_bot "]))
async def search(_, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ നിനക്ക് YouTube നിന്ന് എന്തെങ്കിലും search ചെയ്യണോ 🔎?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "☑️ വേണം", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "വോ വേണ്ട 😒", callback_data="close"
                    )
                ]
            ]
        )
    )
