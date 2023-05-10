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

API_ID = int(getenv("API_ID", "14041145"))
API_HASH = getenv("API_HASH", "0ed849f5e7ab2df61d969317de2ca64c")
BOT_TOKEN = getenv("BOT_TOKEN", "6208176104:AAGVedl1SxFis3GdLOX0XBWlCGVacz1CmOQ")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION", "BABeoPb8_V9H6tvmz3bdDuWQJ_eHVWjOL1Fnpiaioua8xW4kVgt4GW3f4IP8wLtPgyrZMXhHZRpCg8dKb8daR5U2o9iKX_olDr4Jj9K29LhUdr7WXu-WyNEQAv95TQj_V89NULLqcgzOe43TE-65-MuQrWV4VZD_9u7n_G_rNjwFjE1RSQeQhkssAYc3hTIoF5tkwehRPzPfnXpu1DxkMjtrzVQ7nbhzOgKzkCSO9GXLRSLDA2l1gURoU1TPjV2qyAkiFdLWOO-xcb7Tp--Ae_S6a8-oURC1VgfeJ6EathAUYS_SjZqdcty3laSAyOM7jTP0lf42ekvcTDaJAYF6Y42mAAAAAW3f2RcA")
BOT_USERNAME = getenv("BOT_USERNAME", "stetchfybot")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1404114574").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "1404114574").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001964861305")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://joepsychoo:<password>@cluster0.q0ox4m3.mongodb.net/?retryWrites=true&w=majority")
#________________________ Updates  & Music bot name________________
NETWORK = getenv("NETWORK", "its_stetch")
GROUP = getenv("GROUP", "ev_lj")
BOT_NAME = getenv("BOT_NAME", "Stetchfy")
BANNED_USERS = filters.user()

#************************* Image Stuff  ****************************

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.png")

aiohttpsession = aiohttp.ClientSession()


