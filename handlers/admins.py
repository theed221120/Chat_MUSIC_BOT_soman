from asyncio import QueueEmpty

from pyrogram import Client
from pyrogram.types import Message, Chat

from callsmusic import callsmusic, queues

from helpers.filters import command
from helpers.decorators import errors, authorized_users_only


@Client.on_message(command(["pause", "p"]))
@errors
@authorized_users_only
async def pause(_, message: Message):
    if callsmusic.pause(message.chat.id):
        await message.reply_text("⏸ തല്‍ക്കാലത്തേക്ക് പാട്ട് നിർത്തി")
    else:
        await message.reply_text("❗️ ഒന്നും പാടുന്നില്ല")


@Client.on_message(command(["resume", "r"]))
@errors
@authorized_users_only
async def resume(_, message: Message):
    if callsmusic.resume(message.chat.id):
        await message.reply_text("🎧 പാട്ട് വീണ്ടും ആരംഭിക്കുന്നു എല്ലാരും Dance കളി 🕺")
    else:
        await message.reply_text("❗️ഒറ്റ പാട്ടും pause ചെയ്തിട്ടില്ല")


@Client.on_message(command(["stop", "s"]))
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.active_chats:
        await message.reply_text("❗️ ഒന്നും പാടുന്നില്ല")
    else:
        try:
            queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        await callsmusic.stop(message.chat.id)
        await message.reply_text("✅ പാട്ട് നിർത്തി എല്ലാം കൂടി എടുത്ത് കണ്ടത്തില്‍ എറിഞ്ഞിട്ടുണ്ട് 😬 and left the Voice Chat!")


@Client.on_message(command(["skip", "f"]))
@errors
@authorized_users_only
async def skip(_, message: Message):
    if message.chat.id not in callsmusic.active_chats:
        await message.reply_text("❗️ ഒന്നും പാടുന്നില്ല")
    else:
        queues.task_done(message.chat.id)

        if queues.is_empty(message.chat.id):
            await callsmusic.stop(message.chat.id)
        else:
            await callsmusic.set_stream(
                message.chat.id, queues.get(message.chat.id)["file"]
            )

        await message.reply_text("അടുത്ത പാട്ട് ഇട്ടിട്ടുണ്ട്!")


@Client.on_message(command(["mute", "m"]))
@errors
@authorized_users_only
async def mute(_, message: Message):
    result = callsmusic.mute(message.chat.id)

    if result == 0:
        await message.reply_text("🔇 വായ അടുപ്പിച്ചു🙌 ")
    elif result == 1:
        await message.reply_text("🔇 ഞാൻ വായ മൂടി ഇരിക്കുകയാണ് പൊട്ടാ 😁")
    elif result == 2:
        await message.reply_text("❗️ Voice chat ഇല് തന്നെ ഇല്ലെടോ പൊട്ടാ 😬")


@Client.on_message(command(["unmute", "u"]))
@errors
@authorized_users_only
async def unmute(_, message: Message):
    result = callsmusic.unmute(message.chat.id)

    if result == 0:
        await message.reply_text("🔈 വായ തുറപ്പിച്ചു 🙌")
    elif result == 1:
        await message.reply_text("🔈 ഞാൻ എപ്പഴോ വായ തുറന്നു 🤣 നീ ശശി ആയി 🤣")
    elif result == 2:
        await message.reply_text("❗️ Voice chat ഇല് തന്നെ ഇല്ലെടോ പൊട്ടാ 😬")
