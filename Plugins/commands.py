import logging
logger = logging.getLogger(__name__)

from pyrogram import Client, filters
from bot import Star_Moviess_Tamil
from config import Config
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery
from translation import Translation
from pyrogram.errors import MessageNotModified, UserIsBlocked, InputUserDeactivated, FloodWait
import random
import os
import asyncio
import traceback

from pyrogram import Client
from pyrogram import StopPropagation, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
import config

################################################################################################################################################################################################################################################
# Start Command

START = "Translation.START"

TELETIPS_MAIN_MENU_BUTTONS = [
            [
                InlineKeyboardButton('👨‍💻 Creator', url='https://t.me/Star_Movies_Karthik')
            ],
            [
                InlineKeyboardButton('😎 About', callback_data="TUTORIAL_CALLBACK"),
                InlineKeyboardButton('👥 Support', callback_data="GROUP_CALLBACK"),
                InlineKeyboardButton('😁 Help', callback_data="HELP_CALLBACK")
            ],
            [
                InlineKeyboardButton('📣 Update Channel', url='https://t.me/Star_Moviess_Tamil')
            ]
        ]

@Star_Moviess_Tamil.on_message(filters.command('start') & filters.private)
async def start(client, message):
    reply_markup = InlineKeyboardMarkup(TELETIPS_MAIN_MENU_BUTTONS)
    await message.reply_text(
        text = Translation.START.format(
                mention = message.from_user.mention
            ),
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )
    raise StopPropagation

@Star_Moviess_Tamil.on_callback_query()
async def callback_query(client: Client, query: CallbackQuery):
    if query.data=="HELP_CALLBACK":
        TELETIPS_HELP_BUTTONS = [
            [
                InlineKeyboardButton("⬅️ BACK", callback_data="START_CALLBACK")
            ]
            ]
        reply_markup = InlineKeyboardMarkup(TELETIPS_HELP_BUTTONS)
        try:
            await query.edit_message_text(
                Translation.HELP,
                disable_web_page_preview=True,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="GROUP_CALLBACK":
        TELETIPS_GROUP_BUTTONS = [
            [
                InlineKeyboardButton("Star Movies Feedback", url="https://t.me/Star_Movies_Feedback_Bot")
            ],
            [
                InlineKeyboardButton("⬅️ BACK", callback_data="START_CALLBACK"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(TELETIPS_GROUP_BUTTONS)
        try:
            await query.edit_message_text(
                Translation.SUPPORT,
                disable_web_page_preview=True,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass    

    elif query.data=="TUTORIAL_CALLBACK":
        TELETIPS_TUTORIAL_BUTTONS = [
            [
                InlineKeyboardButton("🤵 Admin", url="https://t.me/Star_Movies_Karthik")
            ],
            [
                InlineKeyboardButton("⬅️ BACK", callback_data="START_CALLBACK"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(TELETIPS_TUTORIAL_BUTTONS)
        try:
            await query.edit_message_text(
                Translation.ABOUT,
                disable_web_page_preview=True,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass      
          
    elif query.data=="START_CALLBACK":
        TELETIPS_START_BUTTONS = [
            [
                InlineKeyboardButton('👨‍💻 Creator', url='https://t.me/Star_Movies_Karthik')
            ],
            [
                InlineKeyboardButton('😎 About', callback_data="TUTORIAL_CALLBACK"),
                InlineKeyboardButton('👥 Support', callback_data="GROUP_CALLBACK"),
                InlineKeyboardButton('😁 Help', callback_data="HELP_CALLBACK")
            ],
            [
                InlineKeyboardButton('📣 Update Channel', url='https://t.me/Star_Moviess_Tamil')
            ]
        ]

        reply_markup = InlineKeyboardMarkup(TELETIPS_START_BUTTONS)
        try:
            await query.edit_message_text(
                text = Translation.START.format(
                        mention = query.from_user.mention
                    ),
                disable_web_page_preview=True,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass    
        return


################################################################################################################################################################################################################################################
# Help Command

HELP = "Translation.HELP"

HELP_BUTTONS = [
            [
                InlineKeyboardButton('👨‍💻 Creator', url='https://t.me/Star_Movies_Karthik'),
                InlineKeyboardButton('📣 Update Channel', url='https://t.me/Star_Moviess_Tamil')
            ]
        ]

@Star_Moviess_Tamil.on_message(filters.command("help") & filters.private & filters.incoming)
async def help(client, message):
    text = Translation.HELP
    reply_markup = InlineKeyboardMarkup(HELP_BUTTONS)
    await message.reply_text(
        text = Translation.HELP.format(
                mention = message.from_user.mention
            ),
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

################################################################################################################################################################################################################################################
# About Command

ABOUT = "Translation.ABOUT"

ABOUT_BUTTONS = [
            [
                InlineKeyboardButton('👨‍💻 Creator', url='https://t.me/Star_Movies_Karthik'),
                InlineKeyboardButton('📣 Update Channel', url='https://t.me/Star_Moviess_Tamil')
            ]
        ]

@Star_Moviess_Tamil.on_message(filters.command("about") & filters.private & filters.incoming)
async def about(client, message):
    text = Translation.ABOUT
    reply_markup = InlineKeyboardMarkup(ABOUT_BUTTONS)
    await message.reply_text(
        text = Translation.ABOUT.format(
                mention = message.from_user.mention
            ),
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )
