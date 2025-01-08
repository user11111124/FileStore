#(©)t.me/CodeFlix_Bots




import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7953135595:AAGOrdlcpr3ZMD4E5_y9ugVUlzNsZNxz2FM")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22469064"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c05481978a217fdb11fa6774b15cba32")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002440147748"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "XSeries")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6820461647"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://munkog:6mOVQ1GqWD5P30XE@cluster245.e2vmr.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001868871195')) #Log channel id ( make sure bot is admin )

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002395014488"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002220095389"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/ec17880d61180d3312d6a.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg")

HELP_TXT = "<b>ᴛʜɪs ɪs ᴀɴ 𝕏ғɪʟᴇ ʙᴏᴛ ғᴏʀ @xseriesfy\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/xseriesofficial>𝕏𝕊𝕖𝕣𝕚𝕖𝕤</a></b>"
ABOUT_TXT = "<b>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/davdxp>S0L0™</a>\n◈ ꜱᴇʀɪᴇꜱ ᴄʜᴀɴɴᴇʟ: <a href=https://t.me/xseriesfy>𝕏𝕊𝕖𝕣𝕚𝕖𝕤</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/xseriesofficial>xᴏꜰꜰɪᴄɪᴀʟ</a></b>"
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {first}\n\n ɪ ᴀᴍ 𝕏ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ғɪʟᴇs.</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {mention}\n\n<b><blockquote>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ "Try Again" button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</blockquote></b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @xseriesfy</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "YOU... NOT... ADMIN"

ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
