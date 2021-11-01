# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import re

from . import *

STRINGS = {
    1: """🎇 **Thanks for Deploying Ultroid Userbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage.""",
    2: """🎉** About sachin9742s-Ultroid**

🧿 Ultroid is Pluggable and powerful Telethon Userbot, made in Python from Scratch. It is Aimed to Increase Security along with Addition of Other Useful Features.

❣ Made by **@sachin_official_admin**""",
    3: """**💡• FAQs •**

-> [Username Tracker](https://t.me/sachin_official_admin)
-> [Request Group](https://t.me/KicchaRequest)
-> [Movie update Channel](https://t.me/gd_film)
-> [Cme Movie Collection Channel](https://t.me/CME_Movie)
-> [New Movie Update Channel](https://t.me/ROCKHDMOVIES2021)
-> [𝐃𝐕𝐃/𝐖𝐄𝐁/𝐎𝐓𝐓 𝐌𝐎𝐕𝐈𝐄](https://t.me/KR_ROCKERS_DVD_WEB_OTT_MOVIES)
-> [Tv Series Channel](https://t.me/TV_VIRISION)
-> [Sachin Studio17](https://t.me/Sachin_studio17)
-> [Anikha Music Channel](https://t.me/AnikhaX_Music2)
-> [YouTube video Song Channel](https://t.me/youtube_videosong_Downloader)

**• To Know About Updates**
  - Join My Boss Movie Request Group @KicchaRequest.""",
    4: f"""• `To Know All Available Commands`

  - `{HNDLR}help`
  - `{HNDLR}cmds`""",
    5: """• **For Any Other Query or Suggestion**
  - Move to **@KicchaRequest**.

• Thanks for Reaching till END.""",
}


@callback(re.compile("initft_(\\d+)"))
async def init_depl(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 5:
        return await e.edit(
            STRINGS[5],
            buttons=Button.inline("<< Back", "initbk_" + str(4)),
            link_preview=False,
        )
    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", "initbk_" + str(CURRENT - 1)),
            Button.inline(">>", "initft_" + str(CURRENT + 1)),
        ],
        link_preview=False,
    )


@callback(re.compile("initbk_(\\d+)"))
async def ineiq(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 1:
        return await e.edit(
            STRINGS[1],
            buttons=Button.inline("Start Back >>", "initft_" + str(2)),
            link_preview=False,
        )
    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", "initbk_" + str(CURRENT - 1)),
            Button.inline(">>", "initft_" + str(CURRENT + 1)),
        ],
        link_preview=False,
    )
