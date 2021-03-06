# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import re

from . import *

STRINGS = {
    1: """๐ **Thanks for Deploying Ultroid Userbot!**

โข Here, are the Some Basic stuff from, where you can Know, about its Usage.""",
    2: """๐** About sachin9742s-Ultroid**

๐งฟ Ultroid is Pluggable and powerful Telethon Userbot, made in Python from Scratch. It is Aimed to Increase Security along with Addition of Other Useful Features.

โฃ Made by **@sachin_official_admin**""",
    3: """**๐กโข FAQs โข**

-> [Username Tracker](https://t.me/sachin_official_admin)
-> [Request Group](https://t.me/KicchaRequest)
-> [Movie update Channel](https://t.me/gd_film)
-> [Cme Movie Collection Channel](https://t.me/CME_Movie)
-> [New Movie Update Channel](https://t.me/ROCKHDMOVIES2021)
-> [๐๐๐/๐๐๐/๐๐๐ ๐๐๐๐๐](https://t.me/KR_ROCKERS_DVD_WEB_OTT_MOVIES)
-> [Tv Series Channel](https://t.me/TV_VIRISION)
-> [Sachin Studio17](https://t.me/Sachin_studio17)
-> [Anikha Music Channel](https://t.me/AnikhaX_Music2)
-> [YouTube video Song Channel](https://t.me/youtube_videosong_Downloader)

**โข To Know About Updates**
  - Join My Boss Movie Request Group @KicchaRequest.""",
    4: f"""โข `To Know All Available Commands`

  - `{HNDLR}help`
  - `{HNDLR}cmds`""",
    5: """โข **For Any Other Query or Suggestion**
  - Move to **@KicchaRequest**.

โข Thanks for Reaching till END.""",
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
