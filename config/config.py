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
STRING_SESSION = getenv("STRING_SESSION", "BABkpntXi5JT0HBEa-pJQVmuZmCCSCcwWtDYG93ALKd80EnbV3oc8AtZ-6L4nq4qsz06f9o0Fhyg_DMVPaflP_fO9I8K0FOk98orDWWWr-qexi8xFEm6kn4tQCJNXlju10LoyuDaByIwscV3dvH27L4T-sQkOEG6dNXZJXkhPzzV3t2IbQBv5z0UC9JHLKpidpMIFAkSIABBs_Qs5gyGlv3iWoGK4RuS3_Dz5ZbQ7yObPS6ry0X8CPkLCdkqe-yjOXQ9qeQsuRv9599CP9Fg6Jx6WRjEsiMX0QRivT9dWrqvROpKYse9aDB1KIbAAuEUF2rx8e0Z8jOGYZ29N4zQS92aAAAAAW3f2RcA")
BOT_USERNAME = getenv("BOT_USERNAME", "stetchfybot")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1964861305").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "1404114574").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1964861305")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
#________________________ Updates  & Music bot name________________
NETWORK = getenv("NETWORK", "xl444")
GROUP = getenv("GROUP", "xl444")
BOT_NAME = getenv("BOT_NAME", "Music")
BANNED_USERS = filters.user()

#************************* Image Stuff  ****************************

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.png")

aiohttpsession = aiohttp.ClientSession()


