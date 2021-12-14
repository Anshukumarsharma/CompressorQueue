#    This file is part of the CompressorQueue distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    await event.reply(
        f"Hi `{event.sender.first_name}`\nThis is A CompressorQueue Which Can Encode Videos.\nReduce Size of Videos With Negligible Quality.",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.url("MOVIE BOT", url="https://t.me/Katil_hassena_bot"),
                Button.url("DEVELOPER", url="t.me/Anshu888o"),
            ],
        ],
    )


async def help(event):
    await event.reply(
        "** A Quality CompressorQueue**\n\n+This Bot Compress Videos With Negligible Quality Change.\n-Easy to Use\n-Due to Quality Settings Bot Takes Time To Compress.\nSo Be patience Nd Send videos One By One After Completing.\nDont Spam Bot.\n\nJust Forward Video To Start"
    )


async def ihelp(event):
    await event.edit(
        "** A Quality CompressorQueue**\n\n+This Bot Compress Videos With Negligible Quality Change.\n-Easy to Use\n-Due to Quality Settings Bot Takes Time To Compress.\nSo Be patience Nd Send videos One By One After Completing.\nDont Spam Bot.\n\nJust Forward Video To Start",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def beck(event):
    await event.edit(
        f"Hi `{event.sender.first_name}`\nThis is A CompressorQueue Which Can Encode Videos.\nReduce Size of Videos With Negligible Quality Change.",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.url("MOVIE BOT", url="https://t.me/Katil_hassena_bot"),
                Button.url("DEVELOPER", url="t.me/Anshu888o"),
            ],
        ],
    )
