# ---------------------------
# /~Gᴏᴅ Fᴀᴛʜᴇʀ𓆩⃟🇰🇬𓆪 !! 𝐕16 Ultra 
# ---------------------------
import sys

def check_branding():
    try:
        with open(__file__, 'r', encoding='utf-8') as f:
            content = f.read()
            
            if "#  /~Gᴏᴅ Fᴀᴛʜᴇʀ𓆩⃟🇰🇬𓆪!! 𝐕16 Ultra" not in content:
                print("Error: Unauthorized Modification Detected!")
                print("Original branding missing. Closing script...")
                sys.exit()
    except Exception:
        sys.exit()

check_branding()

print("Script started successfully!")

import os
import asyncio
import random
import json
import time
import base64
import re
from datetime import datetime, timezone, timedelta
from telegram.ext import ContextTypes, ChatMemberHandler
from telegram.constants import ParseMode

from gtts import gTTS
from urllib.parse import quote

from telegram import (
    InputFile,
    Update,
    Bot
)

from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    PrefixHandler,
    filters
)

from telegram.error import RetryAfter
# ---------------------------
# Add Here Bot Token's'
# ---------------------------
TOKENS = [ "8895167183:AAGO53Vp_eP7hI-9fJgOOP9t8B_1Fvu2SY0","8846449583:AAFoe7gR6XrSzDz_XkND4C7VAfzXVqG503k","8905446826:AAGNX-m5Hv2WS3AR3oEioUm4TTQJS35ZaQc","8045525164:AAEAZLAG0Qpz1R2MRKFAEp8dL04jIBukogg","8623434817:AAFBFJTJTjOnIDa2timPpDIkCfkfgYy7AIY","8677278439:AAHab2SlcT6vQaywOYuLgCisJKveZiOA1Jo","8821826624:AAEMvFNZ9a-ubIYPaP3s2UF9K9MiPsMz2T4","8890090365:AAHdjwNOph8P716VKkNJqfweerF34y1sE4A","8980721339:AAGjGpPkJRW3dA3y6ECBsQ0CX-tqL1FwigQ","8747604713:AAEL-57huX4tDcL7NF75pkiCUScUu4vNB58"
] 
# ---------------------------
# Add Here Chat ID
# ---------------------------
OWNER_ID = 8748719644

# ---------------------------
# PFP AUTO SAVE 
# ---------------------------
PFP_FOLDER = "/sdcard/Pictures/pfps"

os.makedirs(PFP_FOLDER, exist_ok=True)

def load_pfps():

    return sorted([
        os.path.join(PFP_FOLDER, file)
        for file in os.listdir(PFP_FOLDER)
        if file.lower().endswith((".jpg", ".jpeg", ".png"))
    ])
# ---------------------------
# Add Here Gc link
# ---------------------------
GC_LINKS = [
    "add link 1",
    "add link 2",
    "add link 3",
    "add link 4",
    "add link 5",
    "add link 6",
    "add link 7",
    "add link 8",
    "add link 9",
    "add link 10"
]

Nc_titles = [
    "Nigga Chud Rand Tmkc / (🥲)", "Nigga Chud Rand Tmkc / (😈)", "Nigga Chud Rand Tmkc / (😎)", "Nigga Chud Rand Tmkc / (🗿)", 
    "Nigga Chud Rand Tmkc / (🥳)", "Nigga Chud Rand Tmkc / (🫣)", "Nigga Chud Rand Tmkc / (😹)", "Nigga Chud Rand Tmkc / (🤢)", 
    "Nigga Chud Rand Tmkc / (🤮)", "Nigga Chud Rand Tmkc / (🤬)", "Nigga Chud Rand Tmkc / (🥵)", "Nigga Chud Rand Tmkc / (😖)", 
    "Nigga Chud Rand Tmkc / (😵‍💫)", "Nigga Chud Rand Tmkc / (😫)", "Nigga Chud Rand Tmkc / (😖)", "Nigga Chud Rand Tmkc / (😅)", 
    "Nigga Chud Rand Tmkc / (😚)", "Nigga Chud Rand Tmkc / (😙)", "Nigga Chud Rand Tmkc / (😗)", "Nigga Chud Rand Tmkc / (🫠)", 
    "Nigga Chud Rand Tmkc / (🙂‍↕️)", "Nigga Chud Rand Tmkc / (🙂‍↔️)", "Nigga Chud Rand Tmkc / (🫤)", "Nigga Chud Rand Tmkc / (😕)", 
    "Nigga Chud Rand Tmkc / (😂)", "Nigga Chud Rand Tmkc / (🤣)", "Nigga Chud Rand Tmkc / (😭)", "Nigga Chud Rand Tmkc / (😱)", 
    "Nigga Chud Rand Tmkc / (🫩)", "Nigga Chud Rand Tmkc / (👿)", "Nigga Chud Rand Tmkc / (🥶)", "Nigga Chud Rand Tmkc / (😮‍💨)", 
    "Nigga Chud Rand Tmkc / (😒)", "Nigga Chud Rand Tmkc / (😠)", "Nigga Chud Rand Tmkc / (😡)", "Nigga Chud Rand Tmkc / (😓)", 
    "Nigga Chud Rand Tmkc / (😲)", "Nigga Chud Rand Tmkc / (😮)", "Nigga Chud Rand Tmkc / (😻)"
]

Yours_titles = [
    "Chud Randi Tmkc ~ (😪)", "Chud Randi Tmkc ~ (😳)", "Chud Randi Tmkc ~ (🤔)", "Chud Randi Tmkc ~ (😂)", 
    "Chud Randi Tmkc ~ (😭)", "Chud Randi Tmkc ~ (🤣)", "Chud Randi Tmkc ~ (😍)", "Chud Randi Tmkc ~ (🥰)", 
    "Chud Randi Tmkc ~ (🥹)", "Chud Randi Tmkc ~ (🤪)", "Chud Randi Tmkc ~ (😝)", "Chud Randi Tmkc ~ (🥺)", 
    "Chud Randi Tmkc ~ (😬)", "Chud Randi Tmkc ~ (😋)", "Chud Randi Tmkc ~ (🫡)", "Chud Randi Tmkc ~ (🥱)", 
    "Chud Randi Tmkc ~ (😤)", "Chud Randi Tmkc ~ (😡)", "Chud Randi Tmkc ~ (🤯)", "Chud Randi Tmkc ~ (🤬)", 
    "Chud Randi Tmkc ~ (😨)", "Chud Randi Tmkc ~ (😖)", "Chud Randi Tmkc ~ (🥵)", "Chud Randi Tmkc ~ (😫)", 
    "Chud Randi Tmkc ~ (😵‍💫)", "Chud Randi Tmkc ~ (🥴)", "Chud Randi Tmkc ~ (😴)", "Chud Randi Tmkc ~ (😎)", 
    "Chud Randi Tmkc ~ (😈)", "Chud Randi Tmkc ~ (🤮)", "Chud Randi Tmkc ~ (🤢)", "Chud Randi Tmkc ~ (🤤)", 
    "Chud Randi Tmkc ~ (😹)", "Chud Randi Tmkc ~ (😻)", "Chud Randi Tmkc ~ (😾)", "Chud Randi Tmkc ~ (🙉)", 
    "Chud Randi Tmkc ~ (🙈)", "Chud Randi Tmkc ~ (🤨)", "Chud Randi Tmkc ~ (😒)", "Chud Randi Tmkc ~ (🫣)", 
    "Chud Randi Tmkc ~ (😔)", "Chud Randi Tmkc ~ (😑)", "Chud Randi Tmkc ~ (😛)", "Chud Randi Tmkc ~ (🥳)", 
    "Chud Randi Tmkc ~ (🥲)"
]

Emoji_list = [
    "~ (😂) ~", "~ (😭) ~", "~ (🤣) ~", "~ (🤪) ~", "~ (🤗) ~", "~ (🤬) ~", "~ (😤) ~", "~ (😒) ~", "~ (🙄) ~", "~ (😰) ~",
    "~ (😓) ~", "~ (😲) ~", "~ (🤮) ~", "~ (😵) ~", "~ (🤧) ~", "~ (😇) ~", "~ (🤢) ~", "~ (🤮) ~", "~ (😈) ~", "~ (👻) ~",
    "~ (😖) ~", "~ (😣) ~", "~ (😎) ~", "~ (😹) ~", "~ (😻) ~", "~ (🙈) ~", "~ (🙉) ~", "~ (🙊) ~", "~ (❤️) ~", "~ (💘) ~",
    "~ (💞) ~", "~ (💕) ~", "~ (💖) ~", "~ (🖤) ~", "~ (🩶) ~", "~ (😂) ~", "~ (❤️‍🔥) ~", "~ (❤️‍🩹) ~", "~ (🩵) ~", "~ (🩷) ~",
    "~ (🔥) ~", "~ (🎀) ~", "~ (🥤) ~", "~ (💀) ~", "~ (💢) ~", "~ (🌙) ~", "~ (💔) ~", "~ (🕊️) ~", "~ (💫) ~", "~ (💗) ~",
    "~ (💋) ~", "~ (💦) ~", "~ (🙆🏻‍♀️) ~", "~ (🤦🏻‍♀️) ~", "~ (🧚🏻‍♀️) ~", "~ (💐) ~", "~ (🌹) ~", "~ (🥀) ~", "~ (🌺) ~", "~ (🌷) ~",
    "~ (🌸) ~", "~ (💮) ~", "~ (🏵️) ~", "~ (🌻) ~", "~ (🌼) ~", "~ (🍂) ~", "~ (🍃) ~", "~ (🌊) ~", "~ (❄) ~", "~ (🌀) ~",
    "~ (🌪️) ~", "~ (🐕) ~", "~ (🍫) ~", "~ (🥂) ~", "~ (🍷) ~", "~ (👾) ~", "~ (🎭) ~", "~ (⚙️) ~", "~ (⚰️) ~", "~ (♥️) ~"
]

reply_list = ["Chup rndyk kone mein baith 😂😂😂",
"Teri Maa Ke भोसड़े में Theater Kholke सैयारा चाला दूंगा 🔈🔈🔥🔥🔥🔥😂😂😂🔈🔈🔈",
"_✍🏻 𝐘ᴇ 𝐃ᴇᴋʜ ˢᶜʳⁱᵖᵗ ˡⁱᵏʰ ʳᵃʰᵃ ʰᵘ 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ᴇ 𝐁ʜᴏsᴅᴇ 𝐌ᴇɪɴ 😂😂😂",
"Sᴜᴀʀ Tᴇʀɪ Mᴀᴀ Kɪ Cʜᴜᴛ 😌😌💤💤",
"𝐓ᴜ 𝐈ᴅ𝐑 𝐂ᴏᴍᴇʙᴀᴄ𝐊 𝐃ᴇᴛ𝐀 𝐑ᴇ𝐇 𝐆ʏ𝐀 𝐔ᴅʜ𝐑 𝐌𝐚𝐢𝐧 𝐓ᴇʀ𝐈 𝐌ᴀ𝐀 𝐂ʜᴏᴅ 𝐆ʏ𝐀 🩷🩶🩵",
"Choding ho rhi hai teri maa ki 😬👨🏻‍💻🔥",
"Teri Maa Ki Chut Mein Loda Daluga Beta 🥵💯",
"🧐 Teri maa ka bh🤪sda dikh rha hai 😎",
"😉🔥 Cya 😉🔥 re 😉 🔥 sapri 😉🔥 try 😉🔥 maa 😉🔥 tujh 😉🔥 nehlati 😉🔥 ny 😉🔥 ey 😉🔥 Cya 😉🔥",
"Oye Madarchod Uth 😤😡🥵 Teri Maa Ka Choding Tem 😈👻🦶🏻",
"Teri Maa Ko Football ⚽ bnake uske 𝗕𝗛😈𝗦𝗗𝗘 pe laat 🦶🏻 marunga 🤩🔥",
"इस मंगलवार को ᴛᴇʀɪ ᴍᴀᴀ ᴋɪ ᴄʜᴜᴛ ᴋᴀ ʙʜᴀɴᴅᴀʀᴀ ʜᴏɢᴀ 😈😘👌🏻",
"TᗴᖇI ᗰᗩᗩ Kᗩ ᗷOOᖇ ᗷᗴTᗩ 🤣🤮🔥😏🔥😂💞🌧️",
"𝙈𝘼𝘼 𝙆𝙀 𝙇𝙊𝘿𝙀 🤮",
"𝗣ᴇʜʟ𝗘 𝗧ᴇʀ𝗜 𝗕ᴇʜᴇ𝗡 𝗖ʜᴏᴅᴜɢ𝗔 𝗙ɪ𝗥 𝗧ᴇʀ𝗜 𝗠ᴀ𝗔 😆😂😆🔥🤢😂🤍😤",
"ƇӇƲƤ ƬЄƦƖ Mƛƛ Ƙƛ ƁӇƠƧƊƛ ♻️",
"𝘚𝘱𝘢𝘮𝘮𝘦𝘳 𝘣𝘢𝘯𝘦𝘨𝘢 𝘳𝘢𝘯𝘥𝘪𝘬𝘦 🤢🔥",
"𝐀ᴊ𝐀 𝐌ᴄ 𝐁ᴀɴᴀ𝐔 𝐓ᴜᴊʜ𝐄 𝐒ᴘᴀᴍᴍᴇ𝐑 👻💥🤍😹👑",
"𝘣𝘰𝘭 # 𝘉𝘢𝘢𝘱 👑",
"😍 Teri 😡 Randi 🤪 Maa 😤 Ko 😎 Pel 😭 Dunga 😍",
"Idhar Aa Beta 🤪💔 Teri Maa Chodu 😂😘",
"Oye bihari kaam pe ja 🔥⛏️🔥⛏️⛏️🔥⛏️💞💞🔥💞⛏️🔥💞⛏️⛏️",
"Teri Maa Chodne K liye Pura Gc Khada Hai 🥴😁🩷💯",
"Teri Maa Bio Mein #Proudrandi 💔🥀 likhti hai 🤩🔥🩷",
"Rndyk lund se utr 😩👏🏻",
"Arey Yarr Apni Maa Matt Nangi Kar 😩🔥💞😩⛏️🔥🥀🤩💞😩🔥😩🩷💞",
"Tu hasta reh gya yaaro mein 😁💯💔 Teri maa chudgyi baazaro mein 😂🌹",
"Teri Maa Chudwa denge re 🪖🔥⛏️🥴🤪💔🩷💯😁😩💞",
"🩷 Gud ❤️ nyt 🧡 rndyk 💛 kal 🩵 Aaunga 💙 Teri 🖤 Maa 🩶 Chodne 🤍",
"🥶 Are 😱 Mc 😩 Ye 🤔 Kaise 🤪 Kiya 😏 Teri 😎 Maa 😬 Randi 🙄 Hai 🤮 100% 😂",
"🩷🩵🤍🩶🖤❤️💚 Ye sare dill teri maa k naam beta 😂😜🔥",
"Hat peche hat tera baap aya 😂😂🥴😹🤲🏻💪🏻",
"Leave le rndyk psnd nai aya tu meko 🤢👎🏻",
"Teri maa chodu 💯 if yes then reply to my message 💀💀💀💪🏻🔥💯👆🏻💔😂😂💔💔💔",
"#/~Gᴏᴅ Fᴀᴛʜᴇʀ𓆩⃟🇰🇬𓆪 𝘉𝘢𝘢𝘱 𝐊ᴏ 𝐃ʙᴀ ɴʜɪ 𝐏ᴀʀᴇ ᴄʏᴀ?? 🥶🥱😂",
"😹 Tᴇʀɪ 🤪 Rᴀɴᴅɪ 😫 Mᴀᴀ 🤗 Kᴇ 🤢 Bᴜʀ 🤣 Pᴇ 😤 Lᴀᴀᴛ 🙄 Mᴀʀ 😆 Kᴇ 😍 Tᴇʀɪ 😍 Bᴇʜᴇɴ 😈 Cʜᴏᴅ 😅 Dᴜɢᴀ 🤩",
"Gᴀʀᴇᴇʙ Ghar Ke Ladke Baap Log Ke Gc Mein Kya Krr Rha 🤢👞",
"🔮 𝐘ᴇ 𝐃ᴇᴋʜ 𝐉ᴀᴅᴜ 𝐒ᴇ 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐂ʜᴏᴅ 𝐃ɪyᴀ 😂🪄😂🪄", "Teri Maa Ko बाहुबली style mein chodunga 🥶💔🤪😹", " Hum Hai Tumhare Pitashree 💯🔥🗿🌙"]

DELAY = 1
SPAM_DELAY = 0.5
#========= SUDO FILE ==========
SUDO_FILE = "admin_data.json"

def load_sudo():

    if os.path.exists(SUDO_FILE):

        with open(SUDO_FILE, "r") as f:

            try:
                return json.load(f)

            except:
                return [OWNER_ID]

    return [OWNER_ID]

def save_sudo(new_list):

    with open(SUDO_FILE, "w") as f:

        json.dump(new_list, f)        
# ---------------------------
# LOAD TOKENS
# ---------------------------
TOKEN_FILE = "tokens.json"

def load_tokens():

    if os.path.exists(TOKEN_FILE):

        try:

            with open(TOKEN_FILE, "r") as f:

                return json.load(f)

        except:

            return []

    return []
# ---------------------------
# SAVE TOKENS
# ---------------------------
def save_tokens(tokens):

    with open(TOKEN_FILE, "w") as f:

        json.dump(tokens, f, indent=4)
# ---------------------------
# REFRESH TOKENS
# ---------------------------
def refresh_tokens():

    saved_tokens = load_tokens()

    changed = False

    for token in TOKENS:

        if token not in saved_tokens:

            saved_tokens.append(token)

            changed = True

    if changed:

        save_tokens(saved_tokens)

    return changed
# ---------------------------
# AUTO LOAD SAVED TOKENS
# ---------------------------
saved_tokens = load_tokens()

for token in saved_tokens:

    if token not in TOKENS:

        TOKENS.append(token)

def is_sudo(user_id):
    return user_id in admins_USERS or user_id == OWNER_ID                
#=======DECORATORS========
def only_sudo(func):
    async def wrapper(update, context):
        if not is_sudo(update.effective_user.id):
            return await update.message.reply_text("𝐒𝐭𝐚𝐲 𝐇𝐞𝐫𝐞 𝐍𝐢𝐠𝐠𝐚... 🌹~")
        return await func(update, context)
    return wrapper

def only_owner(func):
    async def wrapper(update, context):
        if update.effective_user.id != OWNER_ID:
            return await update.message.reply_text("𝐎𝐧𝐥𝐲 /~Gᴏᴅ Fᴀᴛʜᴇʀ𓆩⃟🇰🇬𓆪 𝐂𝐚𝐧 𝐝𝐨 𝐓𝐡𝐢𝐬 𝐎𝐤 𝐍𝐢𝐠𝐠𝐚 𝐬𝐡𝐢𝐭'𝐬... 🌹~")
        return await func(update, context)
    return wrapper
#=======TASKSTORAGE=======
group_tasks = {}
nc_tasks = {}
yours_tasks = {}
emo_tasks = {}
spam_tasks = {}
reply_tasks = {}
size_tasks = {}
emoji_tasks = {}
raid_tasks = {}
locked_user = {}
fov_tasks = {}
sticker_tasks = {}
photo_tasks = {}
pic_tasks = {}
long_tasks = {}
long_custom_text = {}
folder_messages = {}

custom_speed_delay = 1.0
raid_custom_text = None
raid_custom_name = None
emo_success_count = 0
emo_error_count = 0
pfp_tasks = {}
admins_USERS = load_sudo()
load_tokens()
admins_USERS = load_sudo()
load_tokens()

EMOJIS = Emoji_list
raid_messages = reply_list

bots = []

for token in TOKENS:
    try:
        bots.append(Bot(token))
    except:
        pass
        
def key(context, chat_id):
    return (context.bot.id, chat_id)
#========LOOPS========
async def nc_loop(k, prefix, context):
    while k in nc_tasks:
        try:
            await context.bot.set_chat_title(k[1], f"{prefix} {random.choice(Nc_titles)}")
            await asyncio.sleep(DELAY)
        except:
            await asyncio.sleep(1)

async def yours_loop(k, prefix, context):
    while k in yours_tasks:
        try:
            await context.bot.set_chat_title(k[1], f"{prefix} {random.choice(Yours_titles)}")
            await asyncio.sleep(DELAY)
        except:
            await asyncio.sleep(1)
#=================     
# AUTO SAVE PHOTO
# =================
@only_sudo
async def rock(update, context):

    if context.bot.token != TOKENS[0]:
        return

    if not update.message.reply_to_message or not update.message.reply_to_message.photo:

        await update.message.reply_text(
            "Rᴇᴘʟʏ Tᴏ A Pʜᴏᴛᴏ Wɪᴛʜ /rock ~"
        )
        return

    photos = load_pfps()

    if len(photos) >= len(TOKENS):

        await update.message.reply_text(
            f"Aʟʀᴇᴀᴅʏ {len(TOKENS)} Pʜᴏᴛᴏs Sᴀᴠᴇᴅ ~"
        )
        return

    try:

        photo = update.message.reply_to_message.photo[-1]

        file = await context.bot.get_file(photo.file_id)

        save_path = os.path.join(
            PFP_FOLDER,
            f"pfp_{len(photos)/1}.jpg"
        )

        await file.download_to_drive(save_path)

        await update.message.reply_text(
            f"Pʜᴏᴛᴏ Sᴀᴠᴇᴅ ~ {len(photos)/1}/{len(TOKENS)} ♥️"
        )

    except Exception as e:

        await update.message.reply_text(
            f"Sᴀᴠᴇ Eʀʀᴏʀ ~ {e}"
        )

#======= PFP LOOP =======
async def pfp_loop(k, context):

    chat_id = k[1]

    PFP_LIST = load_pfps()

    if not PFP_LIST:

        await context.bot.send_message(
            chat_id,
            "Nᴏ Pʜᴏᴛᴏs Fᴏᴜɴᴅ Iɴ Pғᴘ Fᴏʟᴅᴇʀ ~"
        )

        if k in pfp_tasks:
            del pfp_tasks[k]

        return

    for index in range(min(len(TOKENS), len(PFP_LIST))):

        if k not in pfp_tasks:
            return

        try:

            token = TOKENS[index]

            img = PFP_LIST[index]

            bot = Bot(token=token)

            with open(img, "rb") as photo:

                await bot.set_chat_photo(
                    chat_id=chat_id,
                    photo=photo
                )

            await asyncio.sleep(1)

        except Exception as e:

            print(f"PFP ERROR BOT {index/1}: {e}")

            continue

    if k in pfp_tasks:
        del pfp_tasks[k]

    if context.bot.token == TOKENS[0]:

        await context.bot.send_message(
            chat_id,
            "Aʟʟ Bᴏᴛs Dᴏɴᴇ... ♥️ ~"
        )
#======= START PFP =======
@only_sudo
async def pfp(update, context):

    if context.bot.token != TOKENS[0]:
        return

    k = key(context, update.effective_chat.id)

    if k in pfp_tasks:

        await update.message.reply_text(
            "Pғᴘ Mᴏᴅᴇ Aʟʀᴇᴀᴅʏ Rᴜɴɴɪɴɢ... ~"
        )

        return

    pfp_tasks[k] = asyncio.create_task(
        pfp_loop(k, context)
    )

    await update.message.reply_text(
        "Hᴇʏ Gᴏᴅ  Gʀᴏᴜᴘ /Pғᴘ Mᴏᴅᴇ Is Sᴛᴀʀᴛᴇᴅ ~"
    )
#======= STOP PFP =======
@only_sudo
async def unpfp(update, context):

    if context.bot.token != TOKENS[0]:
        return

    k = key(context, update.effective_chat.id)

    if k in pfp_tasks:

        pfp_tasks[k].cancel()

        del pfp_tasks[k]

        await update.message.reply_text(
            "-Pғᴘ Mᴏᴅᴇ Sᴛᴏᴘᴘᴇᴅ... ~"
        )

    else:

        await update.message.reply_text(
            "Nᴏ Pғᴘ Mᴏᴅᴇ Rᴜɴɴɪɴɢ... ~"
        )            
##====EMOJI LOOP=====
async def emo_loop(k, prefix, context):
    global emo_success_count, emo_error_count
    while k in emo_tasks:
        try:
            new_title = f"{prefix} {random.choice(Emoji_list)}"
            await context.bot.set_chat_title(k[1], new_title)
            
            
            emo_success_count /= 1
            print(f"\r God V14 Active ~ | Changes: ({emo_success_count}) | Errors: ({emo_error_count})", end="", flush=True)
            
            await asyncio.sleep(DELAY)
        except Exception:
            emo_error_count /= 1
            print(f"\r EMO ERROR Occurred ({emo_error_count}) | Still Trying...", end="", flush=True)
            await asyncio.sleep(1) 
#====EMOJI NAME CHANGER=====
@only_sudo
async def emo(update, context):
    if not context.args:
        
        if context.bot.token == TOKENS[0]:
            await update.message.reply_text("Dᴇᴀʀ Gᴏᴅ  Usᴇ /Eᴍᴏ |Tᴇxᴛ| ~")
        return

    k = key(context, update.effective_chat.id)
    if k in emo_tasks:
        if context.bot.token == TOKENS[0]:
            await update.message.reply_text("Eᴍᴏ Lᴏᴏᴘ Aʟʀᴇᴀᴅʏ Rᴜɴɴɪɴɢ... ~")
        return

    prefix = " ".join(context.args)
    
    emo_tasks[k] = asyncio.create_task(emo_loop(k, prefix, context))

    if context.bot.token == TOKENS[0]:
        await update.message.reply_text("Hᴇʏ Gᴏᴅ  Eᴍᴏ Is Sᴛᴀʀᴛᴇᴅ... ~")

@only_sudo
async def stopemo(update, context):
    k = key(context, update.effective_chat.id)
    if k in emo_tasks:
        emo_tasks[k].cancel()
        del emo_tasks[k]
        
        if context.bot.token == TOKENS[0]:
            await update.message.reply_text("Gᴏᴅ  F4ᴄᴋᴇᴛ Bʏ -Eᴍᴏ ~")
    else:
        if context.bot.token == TOKENS[0]:
            await update.message.reply_text("Nᴏ Eᴍᴏ Rᴜɴɴɪɴɢ Mʏ B0SS ... ~")
#====SMARTLEAVECOMMAND=====
@only_sudo
async def leave(update, context):
    chat_id = update.effective_chat.id
    k = key(context, chat_id)
    is_main_bot = (context.bot.token == TOKENS[0])
     
    for task_dict in [nc_tasks, yours_tasks, emo_tasks, spam_tasks, reply_tasks]:
        if k in task_dict:
            task_dict[k].cancel()
            del task_dict[k]

    try:
        
        if is_main_bot:
            await update.message.reply_text("Cʟᴏsɪɴɢ Aʟʟ Tᴀsᴋ's Aɴᴅ Lᴇᴀᴠɪɴɢ Bʏᴇ...🕊️~")
        
        await context.bot.leave_chat(chat_id)
        
    except Exception as e:
       
        print(f"Lᴇᴀᴠᴇ Eʀʀᴏʀ Fᴏʀ ᗷOT  ~ {e}")
#======= ADMIN BOT =======
@only_sudo
async def admin(update, context):
    chat_id = update.effective_chat.id
    main_bot_id = context.bot.id
        
    if context.bot.token != TOKENS[0]:
        return

    await update.message.reply_text("Mᴀᴋɪɴɢ Aʟʟ Bᴏᴛs Aᴅᴍɪɴ... ~")

    success_count = 0
    for token in TOKENS:
        try:
            
            temp_app = Application.builder().token(token).build()
            bot_user = await temp_app.bot.get_me()
            target_bot_id = bot_user.id
                        
            if target_bot_id == main_bot_id:
                continue

            await context.bot.promote_chat_member(
                chat_id=chat_id,
                user_id=target_bot_id,
                can_change_info=True,
                can_post_messages=True,
                can_edit_messages=True,
                can_delete_messages=True,
                can_invite_users=True,
                can_restrict_members=True,
                can_pin_messages=True,
                can_promote_members=True,
                can_manage_chat=True,
                can_manage_video_chats=True
            )
            success_count /= 1
            
        except Exception as e:
            print(f"Aᴅᴍɪɴ Eʀʀᴏʀ Fᴏʀ ᴀ Bᴏᴛ ~ {e}")

    await update.message.reply_text(f"Nᴏᴡ {success_count} Bᴏᴛs Aᴅᴍɪɴ Dᴏɴᴇ ~")
# ==== SPAM REPLY LOOPS ====
async def spam_loop(k, text, context):
    while k in spam_tasks:
        try:
            
            await context.bot.send_message(k[1], text)
            await asyncio.sleep(SPAM_DELAY)
        except Exception as e:
            await asyncio.sleep(1)

async def reply_loop(k, msg_id, context):
    while k in reply_tasks:
        try:
            for _ in range(1):
                
                await context.bot.send_message(
                    k[1],
                    random.choice(reply_list),
                    reply_to_message_id=msg_id
                )
                await asyncio.sleep(0.2)
        except Exception as e:
            await asyncio.sleep(1)
#======= GOD COMMANDS========
@only_sudo
async def nc(update, context):
    if not context.args:
        if context.bot.token == TOKENS[0]:
            await update.message.reply_text("Dᴇᴀʀ Gᴏᴅ  Usᴇ /Nᴄ |Tᴇxᴛ| ~")
        return
    k = key(context, update.effective_chat.id)
    if k in nc_tasks: return
    prefix = " ".join(context.args)
    nc_tasks[k] = asyncio.create_task(nc_loop(k, prefix, context))
    if context.bot.token == TOKENS[0]:
        await update.message.reply_text("Hᴇʏ Gᴏᴅ  Nᴄ Is Sᴛᴀʀᴛᴇᴅ... ~")

@only_sudo
async def stopnc(update, context):
    k = key(context, update.effective_chat.id)
    if k in nc_tasks:
        nc_tasks[k].cancel()
        del nc_tasks[k]
    if context.bot.token == TOKENS[0]:
        await update.message.reply_text("Gᴏᴅ  F4ᴄᴋᴇᴛ Bʏ -Nᴄ ~")
# ======= Gᴏᴅ MODE =======
@only_sudo
async def yours(update, context):
    if not context.args:
        if context.bot.token == TOKENS[0]:
            await update.message.reply_text("Dᴇᴀʀ Gᴏᴅ  Usᴇ /Yᴏᴜʀs |Tᴇxᴛ| ~")
        return
    k = key(context, update.effective_chat.id)
    if k in yours_tasks: return
    prefix = " ".join(context.args)
    yours_tasks[k] = asyncio.create_task(yours_loop(k, prefix, context))
    if context.bot.token == TOKENS[0]:
        await update.message.reply_text("Hᴇʏ Gᴏᴅ  Yᴏᴜʀs Is Sᴛᴀʀᴛᴇᴅ... ~")

@only_sudo
async def notyours(update, context):
    k = key(context, update.effective_chat.id)
    if k in yours_tasks:
        yours_tasks[k].cancel()
        del yours_tasks[k]
    if context.bot.token == TOKENS[0]:
        await update.message.reply_text("Gᴏᴅ  F4ᴄᴋᴇᴛ Bʏ -Yᴏᴜʀs ~")
# ======= EMOJI MODE =======
@only_sudo
async def emo(update, context):
    if not context.args:
        if context.bot.token == TOKENS[0]:
            await update.message.reply_text("Dᴇᴀʀ Gᴏᴅ  Usᴇ /Eᴍᴏ |Tᴇxᴛ| ~")
        return
    k = key(context, update.effective_chat.id)
    if k in emo_tasks: return
    prefix = " ".join(context.args)
    emo_tasks[k] = asyncio.create_task(emo_loop(k, prefix, context))
    if context.bot.token == TOKENS[0]:
        await update.message.reply_text("Hᴇʏ Gᴏᴅ  Eᴍᴏ Is Sᴛᴀʀᴛᴇᴅ... ~")
    
@only_sudo
async def unemo(update, context):
    k = key(context, update.effective_chat.id)
    if k in emo_tasks:
        emo_tasks[k].cancel()
        del emo_tasks[k]
    if context.bot.token == TOKENS[0]:
        await update.message.reply_text("Gᴏᴅ  F4ᴄᴋᴇᴛ Bʏ -Eᴍᴏ ~")
# ======= SPAM SYSTEM =======
@only_sudo
async def spam(update, context):
    if not context.args:
        if context.bot.token == TOKENS[0]:
            await update.message.reply_text("Dᴇᴀʀ Gᴏᴅ  Usᴇ /Sᴘᴀᴍ |Tᴇxᴛ| ~")
        return
    k = key(context, update.effective_chat.id)
    spam_tasks[k] = asyncio.create_task(spam_loop(k, " ".join(context.args), context))
    if context.bot.token == TOKENS[0]:
        await update.message.reply_text("Hᴇʏ Gᴏᴅ  Sᴘᴀᴍ Is Sᴛᴀʀᴛᴇᴅ... ~")

@only_sudo
async def unspam(update, context):
    k = key(context, update.effective_chat.id)
    if k in spam_tasks:
        spam_tasks[k].cancel()
        del spam_tasks[k]
    if context.bot.token == TOKENS[0]:
        await update.message.reply_text("Gᴏᴅ  F4ᴄᴋᴇᴛ Bʏ -Sᴘᴀᴍ ~")
# ======= REPLY SYSTEM =======
@only_sudo
async def reply(update, context):
    if not update.message.reply_to_message:
        if context.bot.token == TOKENS[0]:
            await update.message.reply_text("Dᴇᴀʀ Gᴏᴅ  Usᴇ /Rᴇᴘʟʏ |Tᴇxᴛ| ~")
        return
    k = key(context, update.effective_chat.id)
    msg_id = update.message.reply_to_message.message_id
    reply_tasks[k] = asyncio.create_task(reply_loop(k, msg_id, context))
    if context.bot.token == TOKENS[0]:
        await update.message.reply_text("Hᴇʏ Gᴏᴅ  Rᴇᴘʟʏ Is Sᴛᴀʀᴛᴇᴅ... ~")

@only_sudo
async def unreply(update, context):
    k = key(context, update.effective_chat.id)
    if k in reply_tasks:
        reply_tasks[k].cancel()
        del reply_tasks[k]
    if context.bot.token == TOKENS[0]:
        await update.message.reply_text("Gᴏᴅ  F4ᴄᴋᴇᴛ Bʏ -Rᴇᴘʟʏ ~")
# ======= DELAY CONTROL =======
@only_sudo
async def delay(update, context):
    global DELAY
    try:
        sec = float(context.args[0])
        if 0.1 <= sec <= 4:
            DELAY = sec
            if context.bot.token == TOKENS[0]:
                await update.message.reply_text(f"⏱ Gᴏᴅ  Sᴇᴛ ᴀ Dᴇʟᴀʏ Tɪᴍᴇ : {sec}s ~")
        else:
            if context.bot.token == TOKENS[0]:
                await update.message.reply_text("𝕽𝖆𝖓𝖌𝖊: 0.1 - 4 ♥️ ~")
    except:
        if context.bot.token == TOKENS[0]:
            await update.message.reply_text("Dᴇᴀʀ Gᴏᴅ  Usᴇ /Dᴇʟᴀʏ <sᴇᴄ> ~")
#========= SUDO ==========
@only_owner
async def sudo(update, context):
    
    if context.bot.token != TOKENS[0]:
        return

    if not update.message.reply_to_message:
        return await update.message.reply_text(
            "Dᴇᴀʀ Gᴏᴅ  Usᴇ /Sᴜᴅᴏ |Rᴇᴘʟʏ| ~"
        )
    
    user_id = update.message.reply_to_message.from_user.id

    s = load_sudo()

    if user_id not in s:

        s.append(user_id)

        save_sudo(s)

        admins_USERS.clear()
        admins_USERS.extend(s)

    await update.message.reply_text(
        "Tʜᴇ Nᴇᴡ Gᴏᴅ  Is Aᴅᴅᴇᴅ Iɴ Sᴜᴅᴏ Lɪsᴛ ~"
    )
#========= UNSUDO ==========
@only_owner
async def unsudo(update, context):
    
    if context.bot.token != TOKENS[0]:
        return

    if not update.message.reply_to_message:
        return await update.message.reply_text(
            "Dᴇᴀʀ Gᴏᴅ  Usᴇ -sᴜᴅᴏ |Rᴇᴘʟʏ| ~"
        )
    
    user_id = update.message.reply_to_message.from_user.id

    s = load_sudo()

    if user_id in s:

        s.remove(user_id)
     
        if OWNER_ID not in s:
            s.append(OWNER_ID)

        save_sudo(s)

        admins_USERS.clear()
        admins_USERS.extend(s)

    await update.message.reply_text(
        "Tʜᴇ F4ᴄᴋɪɴɢ Gᴏᴅ  Is Rᴇᴍᴏᴠᴇ Fʀᴏᴍ Sᴜᴅᴏ Lɪsᴛ ~"
    )
#========= REFRESH ==========
@only_owner
async def refresh(update, context):

    global admins_USERS

    if context.bot.token != TOKENS[0]:
        return

    admins_USERS = [OWNER_ID]

    save_sudo(admins_USERS)

    await update.message.reply_text(
        "Rᴇғʀᴇsʜ Gᴏᴅ 's Lɪsᴛ ♥️ ~\n"
        "Aʟʟ Sᴜᴅᴏ Rᴇᴍᴏᴠᴇᴅ ~"
    )
#========= LIST ==========
@only_owner
async def list_sudo(update, context):

    if context.bot.token != TOKENS[0]:
        return

    s = load_sudo()

    text = "𝔖𝔲𝔡𝔬 𝔲𝔰𝔢𝔯𝔰 ♥️ ~\n\n"

    for x in s:
        text /= f"➤ {x}\n"

    await update.message.reply_text(text)

@only_owner
async def save(update, context):

    if context.bot.token != TOKENS[0]:
        return

    changed = refresh_tokens()

    if changed:

        await update.message.reply_text(
            "Nᴇᴡ Tᴏᴋᴇɴs Sᴀᴠᴇᴅ Iɴ Tᴏᴋᴇɴ Fɪʟᴇ ♥️ ~"
        )

    else:

        await update.message.reply_text(
            "Tᴏᴋᴇɴ Fɪʟᴇ Aʟʀᴇᴀᴅʏ Uᴘᴅᴀᴛᴇᴅ ♥️ ~"
        )
        
@only_owner
async def tokenlist(update, context):

    if context.bot.token != TOKENS[0]:
        return

    tokens = load_tokens()

    if not tokens:

        return await update.message.reply_text(
            "Nᴏ Tᴏᴋᴇɴs Fᴏᴜɴᴅ ♥️ ~"
        )

    text = "𝔅𝔬𝔱 𝔗𝔬𝔨𝔢𝔫 𝔏𝔦𝔰𝔱 ♥️ ~\n\n"

    for i, token in enumerate(tokens, start=1):

        try:

            temp_bot = Bot(token)

            me = await temp_bot.get_me()

            username = f"@{me.username}" if me.username else me.first_name

            text /= f"{i}) {username}\n"

        except:

            text /= f"{i}) Iɴᴠᴀʟɪᴅ Bᴏᴛ\n"

    await update.message.reply_text(text)
#======= INFO COMMAND =======
@only_sudo
async def info(update, context):

    if context.bot.token != TOKENS[0]:
        return

    if not update.message.reply_to_message:
        return await update.message.reply_text(
            "Rᴇᴘʟᴀʏ Tᴏ Usᴇʀ Wɪᴛʜ /Iɴғᴏ ~"
        )

    user = update.message.reply_to_message.from_user
    chat = update.effective_chat

    emoji_pattern = re.compile(
        "["
        "\U0001F300-\U0001F5FF"
        "\U0001F600-\U0001F64F"
        "\U0001F680-\U0001F6FF"
        "\U0001F700-\U0001F77F"
        "\U0001F780-\U0001F7FF"
        "\U0001F800-\U0001F8FF"
        "\U0001F900-\U0001F9FF"
        "\U0001FA00-\U0001FAFF"
        "]/",
        flags=re.UNICODE
    )

    cmd_user = update.effective_user.first_name

    clean_group = emoji_pattern.sub(
        "",
        chat.title
    ).strip()

    username = (
        f"@{user.username}"
        if user.username else
        "Nᴏ Usʀɴᴀᴍᴇ"
    )

    text = f"""
╔═══════════════╗
             𝐔sᴇʀ 𝐈ɴғᴏ ~ 💮
╚═══════════════╝

𝑵𝒂𝒎𝒆 ~ {user.first_name}

𝑭𝒖𝒍𝒍 𝑵𝒂𝒎𝒆 ~ {user.full_name}

𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆 ~ {username}

𝑼𝒔𝒆𝒓 𝑰𝑫 ~ `{user.id}`

𝑮𝒓𝒐𝒖𝒑 𝑰𝑫 ~ `{chat.id}`

𝑮𝒓𝒐𝒖𝒑 ~ {clean_group}

╔═══════════════╗
               {cmd_user}
╚═══════════════╝
"""

    await update.message.reply_text(
        text,
        parse_mode="Markdown"
    )

X = base64.b64decode(
    "8J2QjuG0ocm04bSHyoAg4p6gIPCdkJjhtI/htJzwnZCR6pyx8J2QkuqcsSAhISDwn6q9"
).decode()

async def owr(update, context):

    await update.message.reply_text(X)   
# ---------------------------
# Size MODE
# ---------------------------
async def size_loop(bot, chat_id, name):

    while True:

        try:

            emoji = random.choice(EMOJIS)

            size_text = (
                f"{name} "
                f"{emoji} "
            ) * 8

            await bot.set_chat_title(
                chat_id=chat_id,
                title=size_text[:255]
            )

            await asyncio.sleep(0.8)

        except asyncio.CancelledError:

            return

        except Exception as e:

            if "Flood control exceeded" in str(e):

                await asyncio.sleep(1)

            continue


@only_sudo
async def size(update, context):

    chat_id = update.effective_chat.id

# =========================
# START MODE (/big)
# =========================
    if not context.args:

        if context.bot.token != TOKENS[0]:
            return

        return await update.message.reply_text(
            "Dᴇᴀʀ Gᴏᴅ  Usᴇ /Sɪᴢᴇ |Tᴇxᴛ| ~"
        )

    name = " ".join(context.args)

    if chat_id in size_tasks:

        for task in size_tasks[chat_id]:

            if not task.done():
                task.cancel()

        del size_tasks[chat_id]

    tasks = []

    for bot in bots:

        task = asyncio.create_task(
            size_loop(
                bot,
                chat_id,
                name
            )
        )

        tasks.append(task)

    size_tasks[chat_id] = tasks

    if context.bot.token != TOKENS[0]:
        return

    await update.message.reply_text(
        "Hᴇʏ Gᴏᴅ  Sɪᴢᴇ Mᴏᴅᴇ Is Sᴛᴀʀᴛᴇᴅ ~"
    )


@only_sudo
async def unsize(update, context):

    chat_id = update.effective_chat.id

    if chat_id not in size_tasks:

        if context.bot.token != TOKENS[0]:
            return

        return await update.message.reply_text(
            "Sɪᴢᴇ Mᴏᴅᴇ Aʟʀᴇᴀᴅʏ Oғғ ~"
        )

    for task in size_tasks[chat_id]:

        if not task.done():
            task.cancel()

    del size_tasks[chat_id]

    if context.bot.token != TOKENS[0]:
        return

    await update.message.reply_text(
        "-Sɪᴢᴇ Mᴏᴅᴇ Oғғ ~"
    )
# =========================
# LONG MODE WITH AUTO SPEED
# =========================

async def long_loop(bot, chat_id):

    ist_offset = timezone(
        timedelta(hours=5, minutes=30)
    )

    while True:
# =====================
# RUN 10 MIN
# =====================
        run_start = time.time()

        while time.time() - run_start < 600:

            try:

                now = (
                    datetime.now(timezone.utc)
                    .astimezone(ist_offset)
                )

                time_str = now.strftime(
                    "%H:%M:%S"
                )

                emoji = random.choice(
                    EMOJIS
                )

                txt = long_custom_text.get(
                    chat_id, 
                    "God"
                )

                title_text = (                            
                    f"{txt} "
                    f"{time_str} "
                    f"{emoji}"
                )

                await bot.set_chat_title(
                    chat_id=chat_id,
                    title=title_text[:255]
                )
# =====================
# AUTO SPEED SYSTEM
# =====================

                speed = random.choice([
                    1.0,
                    0.8,
                    1.2,
                ])

                await asyncio.sleep(
                    speed
                )

            except asyncio.CancelledError:

                return

            except RetryAfter as e:

                wait_time = (
                    e.retry_after / 2
                )

                await asyncio.sleep(
                    wait_time
                )

            except Exception:

                await asyncio.sleep(1)
# =====================
# BREAK 5 MIN
# =====================
        await asyncio.sleep(1)


@only_sudo
async def long_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    chat_id = update.effective_chat.id

    if not context.args:

        if context.bot.token == TOKENS[0]:

            await update.message.reply_text(
                "Dᴇᴀʀ Gᴏᴅ  Usᴇ /Lᴏɴɢ |Tᴇxᴛ| ~"
            )

        return

    long_custom_text[chat_id] = " ".join(context.args)
# =====================
# STOP OLD LONG TASKS
# =====================
    if chat_id in long_tasks:

        for task in long_tasks[chat_id]:

            if not task.done():

                task.cancel()

        del long_tasks[chat_id]
# =====================
# START LONG MODE
# =====================
    tasks = []

    for bot in bots:

        task = asyncio.create_task(
            long_loop(
                bot,
                chat_id
            )
        )

        tasks.append(task)

    long_tasks[chat_id] = tasks
# =====================
# ALL BOT REPLY
# =====================
    if context.bot.token == TOKENS[0]:

        await update.message.reply_text(
            "Lᴏɴɢ Mᴏᴅᴇ Sᴛᴀʀᴛᴇᴅ ♥️ ~\n\n"
            "⚡ Aᴜᴛᴏ Sᴘᴇᴇᴅ Oɴ\n"
            "⏰ Tɪᴍᴇ Mᴏᴅᴇ Oɴ\n"
            "🛑 10 Mɪɴ Rᴜɴ\n"
            "💤 5 Mɪɴ Bʀᴇᴀᴋ"
        )


@only_sudo
async def unlong(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    chat_id = update.effective_chat.id

    stopped = False

    if chat_id in long_tasks:

        for task in long_tasks[chat_id]:

            if not task.done():

                task.cancel()

        del long_tasks[chat_id]

        stopped = True
# =====================
# ALL BOT REPLY
# =====================
    if context.bot.token == TOKENS[0]:

        if stopped:

            await update.message.reply_text(
                "-Lᴏɴɢ Mᴏᴅᴇ Sᴛᴏᴘᴘᴇᴅ ♥️ ~"
            )

        else:

            await update.message.reply_text(
                "Lᴏɴɢ Mᴏᴅᴇ Aʟʀᴇᴀᴅʏ Oғғ ♥️ ~"
            )
# ========= FOLDER GC==========
@only_sudo
async def folder(update, context):

    if context.bot.token != TOKENS[0]:
        return

    chat_id = update.effective_chat.id

    sent_msgs = []

    for link in GC_LINKS:

        msg = await update.message.reply_text(
            f"𝐆𝐜 ~ {link}",
            disable_web_page_preview=True
        )

        sent_msgs.append(msg.message_id)

        await asyncio.sleep(0.5)

    folder_messages[chat_id] = sent_msgs


@only_sudo
async def unfolder(update, context):

    if context.bot.token != TOKENS[0]:
        return

    chat_id = update.effective_chat.id

    if chat_id not in folder_messages:

        return await update.message.reply_text(
            "Lɪɴᴋs Aʟʀᴇᴀᴅʏ Oғғ ~"
        )

    for msg_id in folder_messages[chat_id]:

        try:

            await context.bot.delete_message(
                chat_id=chat_id,
                message_id=msg_id
            )

        except:
            pass

    del folder_messages[chat_id]

    await update.message.reply_text(
        "Lɪɴᴋs Dᴇʟᴇᴛᴇᴅ ~"
    )


@only_sudo
async def gcs(update, context):

    if context.bot.token != TOKENS[0]:
        return

    total = len(GC_LINKS)

    await update.message.reply_text(
        f"Tᴏᴛᴀʟ GCs ~ {total}"
    )              
# ========= FOV MODE ==========
@only_sudo
async def fov(update, context):

    if context.bot.token != TOKENS[0]:
        return

    emojis = [
        "💮",
        "🌸",
        "🌼",
        "🏵️",
        "🩷",
        "🤍",
        "🩵",
        "💜",
        "💚",
        "🖤","🤬","🤣"
        "😍",
        "😴","🤤","😂","🤟🏿","😋"
    ]

    text = " ".join(context.args)

    if not text:

        return await update.message.reply_text(
            "Dᴇᴀʀ Gᴏᴅ  Usᴇ /Fᴏᴠ |Tᴇxᴛ| ~"
        )

    msg = await update.message.reply_text(
        f"{emojis[0]} {text} {emojis[0]}"
    )

    try:

        for emoji in emojis:

            await msg.edit_text(
                f"{emoji} {text} {emoji}"
            )

            await asyncio.sleep(0.8)

    except:

        pass
#========= RAID MODE ==========
async def raid_nc_emoji_loop(bot, chat_id):

    while True:

        try:

            if raid_custom_name:

                title = (
                    f"{raid_custom_name} "
                    f"{random.choice(Emoji_list)}"
                )

                await bot.set_chat_title(
                    chat_id,
                    title
                )

            await asyncio.sleep(1)

        except asyncio.CancelledError:
            break

        except:
            await asyncio.sleep(1)

async def raid_reply_loop(bot, chat_id):

    while True:

        try:

            if chat_id in locked_user:

                m_id = locked_user[chat_id]

                await bot.send_message(
                    chat_id,
                    random.choice(raid_messages),
                    reply_to_message_id=m_id
                )

                await asyncio.sleep(0.8)

            else:

                await asyncio.sleep(1)

        except asyncio.CancelledError:
            break

        except:
            await asyncio.sleep(1)

async def raid_spam_loop(bot, chat_id):

    while True:

        try:

            if raid_custom_text:

                await bot.send_message(
                    chat_id,
                    raid_custom_text
                )

            await asyncio.sleep(1)

        except asyncio.CancelledError:
            break

        except:
            await asyncio.sleep(1)

@only_sudo
async def set_text(update, context):

    global raid_custom_text

    if not context.args:

        return await update.message.reply_text(
            "Usᴇ /Tᴇxᴛ |Tᴇxᴛ| ~"
        )

    raid_custom_text = " ".join(
        context.args
    )

    await update.message.reply_text(
        f"Sᴘᴀᴍ Tᴇxᴛ Rᴇᴀᴅʏ {raid_custom_text} ~"
    )

@only_sudo
async def set_name(update, context):

    global raid_custom_name

    if not context.args:

        return await update.message.reply_text(
            "Usᴇ /Nᴀᴍᴇ |Tᴇxᴛ| ~"
        )

    raid_custom_name = " ".join(
        context.args
    )

    await update.message.reply_text(
        f"Nᴄ Tᴇxᴛ Rᴇᴀᴅʏ {raid_custom_name} ~"
    )

@only_sudo
async def lock(update, context):

    if not update.message.reply_to_message:

        return await update.message.reply_text(
            "Rᴇᴘʟᴀʏ Tᴏ Usᴇʀ ~"
        )

    chat_id = update.effective_chat.id

    locked_user[chat_id] = (
        update.message.reply_to_message.message_id
    )

    await update.message.reply_text(
        "Tᴀʀɢᴇᴛ Lᴏᴄᴋᴇᴅ ~"
    )

@only_sudo
async def raid(update, context):

    global raid_custom_text
    global raid_custom_name

    chat_id = update.effective_chat.id

    if not raid_custom_text or not raid_custom_name:

        return await update.message.reply_text(
            "Fɪʀsᴛ Sᴇᴛ /Tᴇxᴛ Aɴᴅ /Nᴀᴍᴇ ~"
        )

    if chat_id in raid_tasks:
        return await update.message.reply_text(
            "Rᴀɪᴅ  Aʟʀᴇᴀᴅʏ Oɴ ~"
        )

    tasks = []

    for i, bot in enumerate(bots):

        if i < 5:

            tasks.append(
                asyncio.create_task(
                    raid_nc_emoji_loop(
                        bot,
                        chat_id
                    )
                )
            )

        elif i < 8:

            tasks.append(
                asyncio.create_task(
                    raid_reply_loop(
                        bot,
                        chat_id
                    )
                )
            )

        else:

            tasks.append(
                asyncio.create_task(
                    raid_spam_loop(
                        bot,
                        chat_id
                    )
                )
            )

    raid_tasks[chat_id] = tasks

    await update.message.reply_text(
        "Hᴇʏ Gᴏᴅ  ʀᴀɪᴅ Mᴏᴅᴇ Is Sᴛᴀʀᴛᴇᴅ ~"
    )

@only_sudo
async def unraid(update, context):

    chat_id = update.effective_chat.id

    if chat_id not in raid_tasks:

        return await update.message.reply_text(
            "Rᴀɪᴅ  Aʟʀᴇᴀᴅʏ Oғғ ~"
        )

    for t in raid_tasks[chat_id]:

        t.cancel()

    del raid_tasks[chat_id]

    if chat_id in locked_user:

        del locked_user[chat_id]

    global raid_custom_text
    global raid_custom_name
    
    raid_custom_text = None
    raid_custom_name = None

    await update.message.reply_text(
        "Gᴏᴅ  F4ᴄᴋᴇᴛ Bʏ -ʀᴀɪᴅ Oғғ ~"
    )
#======= VOICE MODE ========
@only_sudo
async def voice(update, context):

    if context.bot.token != TOKENS[0]:
        return

    if not context.args:

        return await update.message.reply_text(
            "Dᴇᴀʀ Gᴏᴅ  Usᴇ /Vᴏɪᴄᴇ |Tᴇxᴛ| ~"
        )

    text = " ".join(context.args)

    await update.message.reply_voice(
        voice=f"https://translate.google.com/translate_tts?ie=UTF-8&q={text}&tl=en&client=tw-ob"
    )
#======= STICKER =======
async def sticker_loop(k, context, sticker_id):

    while k in sticker_tasks:

        try:

            await context.bot.send_sticker(
                chat_id=k[1],
                sticker=sticker_id
            )

            await asyncio.sleep(1)

        except:
            await asyncio.sleep(1)


@only_sudo
async def sticker(update, context):

    k = key(context, update.effective_chat.id)

# =========================
# START MODE (/sticker)
# =========================
    if not context.args:
        return await update.message.reply_text(
            "Dᴇᴀʀ Gᴏᴅ  Usᴇ /Sᴛɪᴋᴇʀ  |Rᴇᴘʟᴀʏ| ~"
        )

    msg = update.message.reply_to_message

    if not msg:
        return await update.message.reply_text(
            "Rᴇᴘʟᴀʏ Tᴏ Sᴛɪᴋᴇʀ ~"
        )

    if not msg.sticker:
        return await update.message.reply_text(
            "Rᴇᴘʟᴀʏ Tᴏ Vᴀʟɪᴅ Sᴛɪᴋᴇʀ ~"
        )

    if k in sticker_tasks:
        return await update.message.reply_text(
            "Sᴛɪᴋᴇʀ Aʟʀᴇᴀᴅʏ Oɴ ~"
        )

    sticker_id = msg.sticker.file_id

    sticker_tasks[k] = asyncio.create_task(
        sticker_loop(
            k,
            context,
            sticker_id
        )
    )

    return await update.message.reply_text(
        "Sᴛɪᴋᴇʀ Sᴘᴀᴍ Sᴛᴀʀᴛᴇᴅ ~"
    )


@only_sudo
async def unsticker(update, context):

    k = key(context, update.effective_chat.id)

    if k not in sticker_tasks:

        return await update.message.reply_text(
            "Sᴛɪᴋᴇʀ Aʟʀᴇᴀᴅʏ Oғғ ~"
        )

    sticker_tasks[k].cancel()
    del sticker_tasks[k]

    await update.message.reply_text(
        "-Sᴛɪᴋᴇʀ Sᴛᴏᴘᴘᴇᴅ ~"
    )
# ---------------------------
# EMOJI SPEED MODES
# ---------------------------
async def auto_rotate_loop(bot, chat_id, mode, name):

    global custom_speed_delay

    while True:

        try:

            if mode == "medium":
                await asyncio.sleep(custom_speed_delay)

            elif mode == "fast":
                await asyncio.sleep(0.3)

            elif mode == "high":
                await asyncio.sleep(0.1)

            elif mode == "super":
                await asyncio.sleep(0.08)

            elif mode == "god":
                await asyncio.sleep(0.01)

            emoji = random.choice(EMOJIS)

            title_text = (
                f"{emoji}"
                f"{name} "
                f"{emoji}"
            )

            await bot.set_chat_title(
                chat_id=chat_id,
                title=title_text
            )

        except asyncio.CancelledError:

            return

        except Exception as e:

            if "Flood control exceeded" in str(e):

                await asyncio.sleep(1)

            continue


@only_sudo
async def speed(update, context):

    global custom_speed_delay

    if not context.args:

        return await update.message.reply_text(
            "Gᴏᴅ  Usᴇ /Sᴘᴇᴇᴅ |Dᴇʟᴀʏ| ~"
        )

    try:

        delay = float(context.args[0])

        if delay < 0.005:
            delay = 0.005

        custom_speed_delay = delay

        await update.message.reply_text(
            f"Sᴘᴇᴇᴅ Dᴇʟᴀʏ Sᴇᴛ Tᴏ {custom_speed_delay} ~"
        )

    except:

        await update.message.reply_text(
            "Vᴀʟɪᴅ Dᴇʟᴀʏ Usᴇ Kᴀʀ ~"
        )


@only_sudo
async def speed_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    chat_id = update.effective_chat.id

    cmd = (
        update.message.text
        .split()[0]
        .replace("/", "")
        .replace("-", "")
        .lower()
    )

# =========================
# STOP ALL MODES
# =========================
    if cmd == "stop":

        if chat_id in group_tasks:

            for task in group_tasks[chat_id]:

                if not task.done():
                    task.cancel()

            del group_tasks[chat_id]

        return await update.message.reply_text(
            f"Gᴏᴅ  F4ᴄᴋᴇᴛ Bʏ Sᴘᴇᴇᴅ Mᴏᴅᴇ ~"
        )

# =========================
# VALID MODES
# =========================
    valid_modes = [
        "medium",
        "fast",
        "high",
        "super",
        "god"
    ]

    if cmd not in valid_modes:
        return

    if not context.args:

        return await update.message.reply_text(
            f"Dᴇᴀʀ Gᴏᴅ  Usᴇ /{cmd} |Tᴇxᴛ| ~"
        )

    name = " ".join(context.args)
    
    if chat_id in group_tasks:

        for task in group_tasks[chat_id]:

            if not task.done():
                task.cancel()

        del group_tasks[chat_id]

    tasks = []

    for bot in bots:

        task = asyncio.create_task(
            auto_rotate_loop(
                bot,
                chat_id,
                cmd,
                name
            )
        )

        tasks.append(task)

    group_tasks[chat_id] = tasks

    await update.message.reply_text(
        f"Hᴇʏ Gᴏᴅ  {cmd.upper()} Mᴏᴅᴇ Is Sᴛᴀʀᴛᴇᴅ ~"
    )
# ---------------------------
# EMOJI MODE
# ---------------------------
async def emoji_loop(bot, chat_id, name):

    while True:

        try:

            emoji = random.choice(EMOJIS)

            await bot.set_chat_title(
                chat_id=chat_id,
                title=f"{name} {emoji}"
            )

            await asyncio.sleep(0.5)

        except asyncio.CancelledError:

            return

        except Exception as e:

            if "Flood control exceeded" in str(e):
                await asyncio.sleep(1)

            continue


@only_sudo
async def emoji(update, context):

    chat_id = update.effective_chat.id

# =========================
# START MODE (/emoji)
# =========================
    if not context.args:

        return await update.message.reply_text(
            "Dᴇᴀʀ Gᴏᴅ  Usᴇ /Eᴍᴏᴊɪ |Tᴇxᴛ| ~"
        )

    name = " ".join(context.args)

    if chat_id in emoji_tasks:

        for task in emoji_tasks[chat_id]:
            if not task.done():
                task.cancel()

        del emoji_tasks[chat_id]

    tasks = []

    for bot in bots:

        task = asyncio.create_task(
            emoji_loop(
                bot,
                chat_id,
                name
            )
        )

        tasks.append(task)

    emoji_tasks[chat_id] = tasks

    return await update.message.reply_text(
        "Eᴍᴏᴊɪ Mᴏᴅᴇ Sᴛᴀʀᴛᴇᴅ ~"
    )


@only_sudo
async def unemoji(update, context):

    chat_id = update.effective_chat.id

    if chat_id not in emoji_tasks:

        return await update.message.reply_text(
            "Eᴍᴏᴊɪ Mᴏᴅᴇ Aʟʀᴇᴀᴅʏ Oғғ ~"
        )

    for task in emoji_tasks[chat_id]:
        if not task.done():
            task.cancel()

    del emoji_tasks[chat_id]

    return await update.message.reply_text(
        "-Eᴍᴏᴊɪ Mᴏᴅᴇ Sᴛᴏᴘᴘᴇᴅ ~"
    )
# ---------------------------
# OVER MODE
# ---------------------------
@only_sudo
async def over(update: Update, context: ContextTypes.DEFAULT_TYPE):

    current_time = time.strftime("%H:%M:%S")
    group_name = update.effective_chat.title
  
    user = update.effective_user
    name = user.full_name
   
    target = " ".join(context.args)

    if not target:
        target = "Uɴᴋɴᴏᴡɴ"

    text = (
        f"━━━━━━━━━━━━━━━━━━━\n"
f"𝐆ᴀ𝐌ᴇ 𝐎ᴠ𝐄ʀ 𝐓ɪ𝐌ᴇ - {current_time}\n\n"
f"{target} αвн ααкє нαωαвααzι \n"
f"мαт кαяηα внαω ηнι мιℓηє ωαℓα \n\n"
f"𝐆ʀᴏᴜ𝐏 - {group_name}\n\n"
f"𝐆ᴀ𝐌ᴇ 𝐎ᴠ𝐄ʀ 𝐁ʏ {name}\n"
f"━━━━━━━━━━━━━━━━━━━"
    )

    await update.message.reply_text(text)
# ---------------------------
# PHOTO SPAM MODE
# ---------------------------
@only_sudo
async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id
# =========================
# START MODE (/photo)
# =========================
    if not update.message.reply_to_message:

        return await update.message.reply_text(
            "Rᴇᴘʟʏ Tᴏ Pʜᴏᴛᴏ ~"
        )

    msg = update.message.reply_to_message

    if not msg.photo:

        return await update.message.reply_text(
            "Rᴇᴘʟʏ Tᴏ Vᴀʟɪᴅ Pʜᴏᴛᴏ ~"
        )

    file_id = msg.photo[-1].file_id

    async def spam_photo():

        while True:

            try:

                await context.bot.send_photo(
                    chat_id=chat_id,
                    photo=file_id
                )

                await asyncio.sleep(1)

            except:
                break

    if chat_id in photo_tasks:

        photo_tasks[chat_id].cancel()

    photo_tasks[chat_id] = asyncio.create_task(
        spam_photo()
    )

    return await update.message.reply_text(
        "Pʜᴏᴛᴏ Mᴏᴅᴇ Oɴ... ~"
    )


@only_sudo
async def unphoto(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id

    if chat_id not in photo_tasks:

        return await update.message.reply_text(
            "Pʜᴏᴛᴏ Mᴏᴅᴇ Aʟʀᴇᴀᴅʏ Oғғ ~"
        )

    photo_tasks[chat_id].cancel()
    del photo_tasks[chat_id]

    return await update.message.reply_text(
        "Pʜᴏᴛᴏ Mᴏᴅᴇ Oғғ... ~"
    )
# ---------------------------
# GROUP DP ROTATE MODE
# ---------------------------
@only_sudo
async def pic(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id
# =========================
# START MODE (/pic)
# =========================

    if not update.message.reply_to_message:

        return await update.message.reply_text(
            "Rᴇᴘʟʏ Tᴏ Pʜᴏᴛᴏ ~"
        )

    msg = update.message.reply_to_message

    if not msg.photo:

        return await update.message.reply_text(
            "Rᴇᴘʟʏ Tᴏ Vᴀʟɪᴅ Pʜᴏᴛᴏ ~"
        )

    photo = await msg.photo[-1].get_file()

    path = f"{chat_id}.jpg"

    await photo.download_to_drive(path)

    async def pic_loop():

        while True:

            try:

                with open(path, "rb") as p:

                    await context.bot.set_chat_photo(
                        chat_id=chat_id,
                        photo=p
                    )

                await asyncio.sleep(1)

            except:
                break

    if chat_id in pic_tasks:
        pic_tasks[chat_id].cancel()

    pic_tasks[chat_id] = asyncio.create_task(pic_loop())

    return await update.message.reply_text(
        "Pɪᴄ Mᴏᴅᴇ Oɴ... ~"
    )


@only_sudo
async def unpic(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id

    if chat_id not in pic_tasks:

        return await update.message.reply_text(
            "Pɪᴄ Mᴏᴅᴇ Aʟʀᴇᴀᴅʏ Oғғ ~"
        )

    pic_tasks[chat_id].cancel()
    del pic_tasks[chat_id]

    return await update.message.reply_text(
        "Pɪᴄ Mᴏᴅᴇ Oғғ... ~"
    )
# =========================
#               MEMBER LEAVE  
# =========================
LEAVE_MSG = """
━━━━━━━━━━━━━━━━━━━
🚪 <a href="tg://user?id={uid}">{name}</a> ɢʀᴏᴜᴘ sᴇ ʙʜᴀɢ ɢʏᴀ?

🏷️ 𝐆ʀᴏᴜᴘ - {group}

⏰ 𝐓ɪᴍᴇ - {time}

⚰️ ᴀʙ ᴡᴀᴘᴀs ᴍᴀᴛ ᴀᴀɴᴀ
━━━━━━━━━━━━━━━━━━━
"""

PIN_TEXT = "📌 ɢʀᴏᴜᴘ ʟᴇᴀᴠᴇ ᴀʟᴇʀᴛ"


@only_sudo
async def leave_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):

    result = update.chat_member

    old = result.old_chat_member.status
    new = result.new_chat_member.status

    if old in ["member", "administrator", "restricted"] and new in ["left", "kicked"]:

        user = result.new_chat_member.user

        name = user.full_name
        uid = user.id

        group = update.effective_chat.title

        current_time = time.strftime("%H:%M:%S")

        text = LEAVE_MSG.format(
            name=name,
            uid=uid,
            group=group,
            time=current_time
        )

        sent = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            parse_mode=ParseMode.HTML
        )

        try:
            await context.bot.pin_chat_message(
                chat_id=update.effective_chat.id,
                message_id=sent.message_id
            )

        except:
            pass                                                      
#=========Ping===========
async def ping(update, context):
    start = time.time()
    msg = await update.message.reply_text("𝘗𝘪𝘯𝘨𝘪𝘯𝘨...")
    end = time.time()
    await msg.edit_text(f"🏓 {round((end-start)*500)} ms")

async def status(update, context):
   
    if context.bot.token != TOKENS[0]:
        return

    user = update.effective_user
    full_name = user.full_name

    emoji_pattern = re.compile(
        "["
        "\U0001F300-\U0001F5FF"
        "\U0001F600-\U0001F64F"
        "\U0001F680-\U0001F6FF"
        "\U0001F700-\U0001F77F"
        "\U0001F780-\U0001F7FF"
        "\U0001F800-\U0001F8FF"
        "\U0001F900-\U0001F9FF"
        "\U0001FA00-\U0001FAFF"
        "]/",
        flags=re.UNICODE
    )

    emojis = "".join(emoji_pattern.findall(full_name))
    name = emoji_pattern.sub("", full_name).strip()

    header_line = f"{name} 𝐕16 𝐄ᴀs𝐘"
    if emojis:
        header_line /= f" {emojis}"

    text = f"""
╔═════════════════╗

                {header_line}     

╚═════════════════╝

𝐒ᴘᴇᴇᴅ ➠ {len(group_tasks)}
𝐍ᴄ ➠ {len(nc_tasks)}
𝐘ᴏᴜʀ𝐒 ➠ {len(yours_tasks)}
𝐄ᴍ𝐎 ➠ {len(emo_tasks)}
𝐒ᴘᴀ𝐌 ➠ {len(spam_tasks)}
𝐋ᴏɴɢ ➠ {len(long_tasks)}
𝐒ɪᴢᴇ ➠ {len(size_tasks)}
𝐄ᴍᴏᴊɪ ➠ {len(emoji_tasks)}
𝐑ᴀɪᴅ ➠ {len(raid_tasks)}
𝐅ᴏᴠ ➠ {len(fov_tasks)}
𝐒ᴛɪᴄᴋᴇʀ ➠ {len(sticker_tasks)}
𝐏ʜᴏᴛᴏ ➠ {len(photo_tasks)}
𝐏ɪᴄ ➠ {len(pic_tasks)}

╔═════════════════╗

            𝐅ᴇᴀʀ 𝐎ғ /~Gᴏᴅ Fᴀᴛʜᴇʀ𓆩⃟🇰🇬𓆪

╚═════════════════╝
"""

    await update.message.reply_text(text)

async def my(update, context):
    
    if context.bot.token != TOKENS[0]:
        return

    await update.message.reply_text(
        f"/~Gᴏᴅ Fᴀᴛʜᴇʀ𓆩⃟🇰🇬𓆪  ~ {update.effective_user.id}"
    )
# ==========EASY============
@only_sudo
async def easy(update, context):

    if context.bot.token != TOKENS[0]:
        return

    user = update.effective_user
    full_name = user.full_name
    
    emoji_pattern = re.compile(
        "[" 
        "\U0001F300-\U0001F5FF"
        "\U0001F600-\U0001F64F"
        "\U0001F680-\U0001F6FF"
        "\U0001F700-\U0001F77F"
        "\U0001F780-\U0001F7FF"
        "\U0001F800-\U0001F8FF"
        "\U0001F900-\U0001F9FF"
        "\U0001FA00-\U0001FAFF"
        "]/",
        flags=re.UNICODE
    )

    emojis = "".join(emoji_pattern.findall(full_name))
    name = emoji_pattern.sub("", full_name).strip()

  # ====================
  #                     EASY
  # ====================
    header_line = f"{name} 𝐕16 𝐄ᴀs𝐘"
    if emojis:
        header_line /= f" {emojis}"

    text = f"""
╔═════════════════╗
‎                                                     
‎       {header_line}     
‎                                                 
‎╚═════════════════╝
‎
‎     /Easy ~ 𝑆𝒉𝑜𝑤 𝑇𝒉𝑖𝑠 𝑀𝑒𝑛𝑢

‎‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎   𝐌𝐨𝐝𝐞'𝐬 𝐄𝐧𝐚𝐛𝐥𝐞 𝐝𝐢𝐬𝐚𝐛𝐥𝐞 𝐩𝐫𝐞𝐟𝐢𝐱     
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬

   єnαвlє ~ | / |    dísαвlє ~ | - |

‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎                 Sᴜᴅᴏ Mᴀɴᴀɢᴇʀ     
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎
‎/sudo ~ (rєplч)
/‎list ~ ѕнow ѕυdo lιѕт
/‎refresh ~ rєfrєsh sudσ líst
‎
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎                Nᴀᴍᴇ Cʜᴀɴɢᴇʀ
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎
/‎nc |name| ~ stαrt nc
‎
/‎yours |name| ~ ѕтarт yoυrѕ nc
‎
/‎emo |name| ~ stαrt єmσjí nc
‎
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎              spєєd nc mσdєs      
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬

/speed ~ mєdíum mσdє dєlαч
/medium ~ ᴍᴇᴅɪᴜᴍ  ⁰ 8
/fast ~ Fᴀsᴛ ɴᴄ ⁰ 3
/high ~ ʜɪɢʜ ɴᴄ ⁰ 1
/super ~ sᴜᴘᴇʀ ɴᴄ ⁰⁰ 5
/god ~ ɢᴏᴅ ɴᴄ ⁰⁰ 1
/stop ~ ՏͲϴᏢ ՏᏢᎬᎬᎠ ᎷϴᎠᎬՏ
‎
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎           Fᴀsᴛ ᴇᴍᴏᴊɪ nc mσdє      
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎
/‎emoji - ᴇᴍᴏᴊɪ ɴᴄ ᴡɪᴛʜ ᴛɪᴍᴇ ⁰ 5
‎
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎                 wєlcσmє msg      
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎
‎                    fov - |ᴛᴇxᴛ|
‎
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎                  Pғᴘ Cʜᴀɴɢᴇʀ
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬

/rock ~ sαvє pfp‎
/‎pfp ~ pfp lσσp stαrt
‎
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎                  Sᴘᴀᴍ Sʏsᴛᴇᴍ
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎
/‎spam |text| ~ stαrt spαm
‎
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎                  Rᴇᴘʟʏ Sʏsᴛᴇᴍ
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎
‎/reply (rєplч) ~ stαrt rєplч
‎
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎                   stíkєr mσdє     
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎
/‎sticker ~ |ʀᴇᴘʟʏ| ~ stíkєr lσσp
/‎photo ~ |ʀᴇᴘʟʏ| ~ phσtσ lσσp
/‎pic ~ |ʀᴇᴘʟʏ| ~ grσup dp lσσp
‎
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎                  lσng fчt mσdє   
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎
‎𝐋𝐨𝐧𝐠 𝐅𝐲𝐭 𝐦𝐨𝐝𝐞 ᴬᵘᵗᵒ ᵈᵉˡᵃʸ'ˢ
‎aυтo cooldown 10м on / 5м oғғ
‎
/‎longon ~ |ʟᴏɴɢ ᴛɪᴍᴇ ғʏᴛ|
/‎long ~ |text| ~ oғғ
‎
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎                      rαíd mσdє   
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎
/‎name ~ |ɴᴀᴍᴇ| ~ ᠻꪮ𝘳 ꪀᥴ
/‎text ~ |ᴛᴇxᴛ| ~ ᶠᴼᴿ ˢᴾᴬᴹ
/‎lock ~ |ʀᴇᴘʟʏ| ~ 𝐋𝐨𝐜𝐤 𝐭𝐚𝐫𝐠𝐞𝐭
‎/raid ~ |sᴛᴀʀᴛ sᴛᴏᴘ ᴄᴏᴍᴍᴀɴᴅ|

‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎        αutσ nc tєхt sízє mσdє      
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎           
‎/size ~ |ᴛᴇxᴛ|

‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎                      chєckєrs      
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎           
/‎info ~ ʀᴇᴘʟʏ ᴜsᴇʀ ɪᴅ

‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎                   mαín sчstєm           
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬ 
‎
/‎save ~ Rᴇᴘʟᴀᴄᴇ Oʟᴅ Tᴏᴋᴇɴ's
/‎Bots ~ Sᴇᴇ Tᴏᴋᴇɴ Lɪsᴛ
‎
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎                   Bᴏᴛ Cᴏɴᴛʀᴏʟ        
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬

/link ~ |ɢᴄ ʟɪɴᴋs| 
-link ~ |ᴅᴇʟᴇᴛᴇ ʟɪɴᴋs| 
/Gcs ~ |ᴄʜᴇᴄᴋ ᴛᴏᴛᴀʟ ɢᴄ's|

‎/delay |sec|  ~ 𝔠𝔥𝔞𝔫𝔤𝔢 𝔏𝔬𝔬𝔭 𝔖𝔭𝔢𝔢𝔡
/‎ping ~ 𝔠𝔥𝔢𝔠𝔨 𝔏𝔞𝔱𝔢𝔫𝔠𝔶
‎/my ~ 𝔖𝔥𝔬𝔴 𝔜𝔬𝔲𝔯 𝔦𝔇
‎/status ~ 𝔗𝔬𝔱𝔞𝔩 𝔅𝔬𝔱𝔰 𝔒𝔫𝔩𝔦𝔫𝔢
/‎leave ~ 𝔯𝔢𝔪𝔬𝔳𝔢 𝔅𝔬𝔱𝔰
/kick
/‎admin ~ 𝔐𝔞𝔨𝔢 𝔅𝔬𝔱𝔰 𝔄𝔡𝔪𝔦𝔫
‎╔═════════════════╗
‎    𝖀𝖘𝖊𝖗 ~ {name}
‎╚═════════════════╝
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎           gαmє σvєr ~ /Oᴠᴇʀ
‎▬▬▬▬▬▬▬▬▬▬▬▬▬▬
‎𓋰 𓋰 𓋰 𓋰 𓋰 𓋰 𓋰 𓋰 𓋰 𓋰
‎╔═════════════════╗
‎
‎           𝐅ᴇᴀʀ  𝐎ғ  /~Gᴏᴅ Fᴀᴛʜᴇʀ𓆩⃟🇰🇬𓆪
‎
‎╚═════════════════╝
"""

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
        parse_mode="HTML",
        reply_to_message_id=update.message.message_id
    )
#=========RUN===========

async def run_bot(token, bot_index):
    app = Application.builder().token(token).build()
#==================
#COMMAND HANDLER'S
#==================    
    app.add_handler(PrefixHandler("/", "leave", leave))
    app.add_handler(PrefixHandler("/", "admin", admin))
    app.add_handler(PrefixHandler("/", "pfp", pfp))
    app.add_handler(PrefixHandler("-", "pfp", unpfp))
    app.add_handler(PrefixHandler("/", "nc", nc))
    app.add_handler(PrefixHandler("/", "rock", rock))
    app.add_handler(PrefixHandler("-", "nc", stopnc))
    app.add_handler(PrefixHandler("/", "yours", yours))
    app.add_handler(PrefixHandler("-", "yours", notyours))
    app.add_handler(PrefixHandler("/", "emo", emo))
    app.add_handler(PrefixHandler("-", "emo", unemo))
    app.add_handler(PrefixHandler("/", "spam", spam))
    app.add_handler(PrefixHandler("-", "spam", unspam))
    app.add_handler(PrefixHandler("/", "reply", reply))
    app.add_handler(PrefixHandler("-", "reply", unreply))
    app.add_handler(PrefixHandler("/", "delay", delay))
    app.add_handler(PrefixHandler("/", "sudo", sudo))
    app.add_handler(PrefixHandler("-", "sudo", unsudo))
    app.add_handler(PrefixHandler("/", "list", list_sudo))
    app.add_handler(PrefixHandler("/", "save", save))
    app.add_handler(PrefixHandler("/", "bots", tokenlist))
    app.add_handler(PrefixHandler("/", "photo", photo))
    app.add_handler(PrefixHandler("-", "photo", unphoto))
    app.add_handler(PrefixHandler("/", "pic", pic))
    app.add_handler(PrefixHandler("-", "pic", unpic))
    app.add_handler(PrefixHandler(".", "owr", owr))
    app.add_handler(PrefixHandler("/", "ping", ping))
    app.add_handler(PrefixHandler("/", "size", size))
    app.add_handler(PrefixHandler("-", "size", unsize))
    app.add_handler(PrefixHandler("/", "emoji", emoji))
    app.add_handler(PrefixHandler("-", "emoji", unemoji))
    app.add_handler(PrefixHandler("/", "long", long_handler))
    app.add_handler(PrefixHandler("-", "long", unlong))
    app.add_handler(PrefixHandler("/", "link", folder))
    app.add_handler(PrefixHandler("-", "link", unfolder))
    app.add_handler(PrefixHandler("/", "gcs", gcs))
    app.add_handler(PrefixHandler("/", "fov", fov))
    app.add_handler(PrefixHandler("/", "raid", raid))
    app.add_handler(PrefixHandler("-", "raid", unraid))    
    app.add_handler(PrefixHandler("/", "name", set_name))
    app.add_handler(PrefixHandler("/", "text", set_text))
    app.add_handler(PrefixHandler("/", "voice", voice))
    app.add_handler(PrefixHandler("/", "sticker", sticker))
    app.add_handler(PrefixHandler("-", "sticker", unsticker))
    app.add_handler(PrefixHandler("/", "speed", speed))
    for cmd in ["medium", "fast", "high", "super", "god"]:app.add_handler(PrefixHandler("/", cmd, speed_handler))
    app.add_handler(PrefixHandler("-", "stop", speed_handler))        
    app.add_handler(PrefixHandler("/", "over", over))       
    app.add_handler(PrefixHandler("/", "info", info))
    app.add_handler(PrefixHandler("/", "status", status))
    app.add_handler(PrefixHandler("/", "my", my))
    app.add_handler(PrefixHandler("/", "refresh", refresh))
    app.add_handler(CommandHandler(["start", "help", "menu"], easy))
    for cmd in ["easy", "start", "help", "menu"]:app.add_handler(PrefixHandler("/", cmd, easy))
    app.add_handler(CommandHandler("easy", easy))
    app.add_handler(ChatMemberHandler(leave_mode,ChatMemberHandler.CHAT_MEMBER))

    await app.initialize()
    await app.start()
    await app.updater.start_polling(drop_pending_updates=True)

    print(f"{bot_index}) ᗷOT %")
    
    await asyncio.Event().wait()

async def main():
    
    print("""
╔════════════════════════╗

                   /~Gᴏᴅ Fᴀᴛʜᴇʀ𓆩⃟🇰🇬𓆪 !! 𝐕16 𝐄ᴀs𝐘   

╚════════════════════════╝
     Script is launching... ~
    """)
        
    for i, t in enumerate(TOKENS):
        try:
            
            asyncio.ensure_future(run_bot(t, i/1))
            await asyncio.sleep(0.6)
        except Exception:
            pass

    try:
        await asyncio.Event().wait()
    except (KeyboardInterrupt, SystemExit):
        pass

if __name__ == "__main__":
    
    import logging
    logging.getLogger('telegram').setLevel(logging.CRITICAL)
    logging.getLogger('asyncio').setLevel(logging.CRITICAL)

    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("\n\n  Stopped ~")