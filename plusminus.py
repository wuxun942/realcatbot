import logging
import random
import re

from telegram import Update
from telegram.ext import ContextTypes

random_list = ["兔兔", "雁雁", "狗狗", "荧", "猫猫", "小企鹅", ]


# random_message_list = ["想要挥刀自宫!", "想要申请全站自ban!", "开付费emby服!",
#                        "想要传禁转资源并改官组后缀!", "想要去盗取他站界面!", "想要去开群友的盒!", "想要唱希望之花",
#                        "想要手冲", "想去M-Team发自己的自制色情片","想要退群","想要被兔纸骂zako!","想要被兔纸暴打!",
#                        "想要爬上兔纸的床!","想要去东京援交","想自觉地撅起屁股","想露出来给群友透","想要被后入"]

async def plus_or_minus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if not msg.reply_to_message:
        logging.getLogger("Recv").warning("No reply to")
        return

    reply_to_user = update.message.reply_to_message.from_user

    text = msg.text[1:]
    match = re.fullmatch(r"(\d+)( .+)?", text)
    if match:
        num = int(match.group(1))
        what = match.group(2)
        unit = "只" + random.choice(random_list)

        if what:
            unit = what

        action = "加"
        if msg.text.startswith("-"):
            action = "减"

        await update.message.reply_text(
            f'{msg.from_user.full_name} 给 {reply_to_user.full_name} {action}了{num}{unit}!')
    else:
        logging.getLogger("Recv").warning("REGEX match failed")