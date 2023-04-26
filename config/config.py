import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
   load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
que = {}
admins = {}

#------------------------ Important Stuff 🤎 -----------------------

API_ID = int(getenv("API_ID", "8934899"))
API_HASH = getenv("API_HASH", "bf3e98d2c351e4ad06946b4897374a1e")
BOT_TOKEN = getenv("BOT_TOKEN", "6225451353:AAGFd-lpSA5gKccHjxqzKcRRxPaZPB_E-XU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION", "AgAiI3dT0jimOCn6RiMLYMdEMQKpqksonYkDy_TCaCP0kH-y91nZ9Ps48mFl75iglw9xakyB38XQxzU9yi4x8OgJJl2mZF2CilIBoSG18nCAq5G6bWAjDC1axBJ5FTG-4sUbWfK9ZvQOanqB9MMKDzTYYFnrVggQTNJQTBuz-zc9WLiP_z32YQUoQ-lS7MeqTx--MVH9kpz9YXyjbQJExCCxi_3JwWs8IYi4DT6bo2qKxywljydrUxme6REPhey2yLX76loKQRcvT3nEZJavuYJypdym9_WEbfaXuKxJYkCeeYAP--E0ygr-xHYkTPgah9lXYxpQsWGgKG4gScatlTETAAAAAVLAQooA")
BOT_USERNAME = getenv("BOT_USERNAME", "Saiadjabot")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "-1001731222858").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "-1001731222858").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001731222858")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
#________________________ Updates  & Music bot name________________
NETWORK = getenv("NETWORK", "e87p5m")
GROUP = getenv("GROUP", "e87p5m")
BOT_NAME = getenv("BOT_NAME", "Music")
BANNED_USERS = filters.user()

#************************* Image Stuff  ****************************

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/ff43de16d318f461088c7.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/ff43de16d318f461088c7.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/ff43de16d318f461088c7.png") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/ff43de16d318f461088c7.png")

aiohttpsession = aiohttp.ClientSession()


