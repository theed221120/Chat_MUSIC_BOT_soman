from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

from handlers.start import FRIEND_BOT

# close calllback

@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


# Start callback 

@Client.on_callback_query(filters.regex("startcb"))
async def startcb(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Daa മോനെ 😜 !</b>
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
    

# Command list callback

@Client.on_callback_query(filters.regex("cmdlistcb"))
async def cmdlistcb(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Daa മോനെ 😜 !</b>

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
                        "🏃‍♂️GO BACK 🚶‍♂️", callback_data="startcb"
                    )
                ]
            ]
        )
    )
