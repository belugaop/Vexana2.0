import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from vexana.events import register
from vexana import telethn as tbot


PHOTO = "https://telegra.ph/file/4a7d5037bcdd1e74a517a.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Vexana .** \n\n"
  TEXT += "⚪ **I'm Working Properly** \n\n"
  TEXT += '⚪ **My Master : [Aksr-aashish](https://t.me/itzz_Axel1)** \n\n'
  TEXT += f"⚪ **Library Version :** `{telever}` \n\n"
  TEXT += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("Help", "https://t.me/Vexana_Robot?start=help"), Button.url("Support", "https://t.me/vexana_support")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
