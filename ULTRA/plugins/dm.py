from telethon import *

from ULTRA import CMD_HELP
from ULTRA.utils import admin_cmd
from ULTRA import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "KING FIGHTER"

# Fixed by LEGDND X
@borg.on(admin_cmd(pattern="dm ?(.*)"))
async def _(dc):
    Kingfighter = bot.uid
    USERNAME = f"tg://user?id={KING FIGHTER}"
    
    d = dc.pattern_match.group(1)

    c = d.split(" ")

    chat_id = c[0]
    try:
        chat_id = int(chat_id)

    except BaseException:

        pass

    msg = ""
    masg = await dc.get_reply_message()  # ghantaππ
    if dc.reply_to_msg_id:
        await borg.send_message(chat_id, masg)
        await dc.edit(f"ββ\n\n**[{DEFAULTUSER}]({USERNAME})** : ππππ πππππππ πππ ππππππππππππ πππππππππ\n\nββ")
    for i in c[1:]:
        msg += i + " " 
    if msg == "":  # hoho
        return
    try:
        await borg.send_message(chat_id, msg)
        await dc.edit(f"ββ\n\n**[{DEFAULTUSER}]({USERNAME})** : ππππ πππππππ πππ ππππππππππππ πππππππππ\n\nββ")
    except BaseException:  # hmmmmmmmmmπ€π€
        await dc.edit("__.dm <@username> <text>__")


CMD_HELP.update
(
  {
    "dm": "**Plugin :** `dm`\
    \n\n**Syntax : **`.dm <username> <text>`\
    \n**Usage : ** Sends the <text> msg to the given <username>\
    \n\n**Syntax : **`.dm <username> (reply to a msg)`\
    \n**Usage : ** Forwards the (replied msg) to the given <username>"
  }
)
