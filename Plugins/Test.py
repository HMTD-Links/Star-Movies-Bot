import logging
logger = logging.getLogger(__name__)

from pyrogram import Client, filters
from bot import Star_Moviess_Tamil
from config import Config
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery
from movies import Movies
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

                  # Star Movies Tamil

################################################################################################################################################################################################################################################
# Alien Covenant (2017)

ALIEN_COVENANT = "MOVIES.ALIEN_COVENANT"

TELETIPS_MAIN_MENU_BUTTONS = [
            [
                InlineKeyboardButton('📃 1/4', callback_data="GROUP_CALLBACK"),
                InlineKeyboardButton('Next ➡️', callback_data="HELP_CALLBACK")
            ]
        ]

@Star_Moviess_Tamil.on_message(filters.command("alien_covenant") & filters.private & filters.incoming)
async def alien_covenant(client, message):
    await message.reply_photo(
        caption = MOVIES.ALIEN_COVENANT.format(
                mention = message.from_user.mention
            ),
        reply_markup=reply_markup,
        photo="https://telegra.ph/file/206f9013802376b39ad03.jpg",
        quote=True
    )
    raise StopPropagation

@Star_Moviess_Tamil.on_callback_query()
async def callback_query(client: Client, query: CallbackQuery):
    if query.data=="MOVIES.ALIEN_COVENANT_PAGE2":
        TELETIPS_HELP_BUTTONS = [
            [
                InlineKeyboardButton("⬅️ BACK", callback_data="START_CALLBACK"),
                InlineKeyboardButton('📃 2/4', callback_data="GROUP_CALLBACK"),
                InlineKeyboardButton('Next ➡️', callback_data="HELP_CALLBACK")
            ]
            ]
        reply_markup = InlineKeyboardMarkup(TELETIPS_HELP_BUTTONS)
        try:
            await query.edit_message_text(
                text = MOVIES.ALIEN_COVENANT_PAGE2.format(
                        mention = query.from_user.mention
                    ),
                reply_markup=reply_markup
            ),
        photo="https://telegra.ph/file/206f9013802376b39ad03.jpg",
        quote=True
    )
        except MessageNotModified:
            pass

    elif query.data=="GROUP_CALLBACK":
        TELETIPS_GROUP_BUTTONS = [
            [
                InlineKeyboardButton("⬅️ BACK", callback_data="START_CALLBACK"),
                InlineKeyboardButton('📃 3/4', callback_data="GROUP_CALLBACK"),
                InlineKeyboardButton('Next ➡️', callback_data="HELP_CALLBACK")
            ]
            ]
        reply_markup = InlineKeyboardMarkup(TELETIPS_GROUP_BUTTONS)
        try:
            await query.edit_message_text(
                text = Translation.START.format(
                        mention = query.from_user.mention
                    ),
                reply_markup=reply_markup
            ),
        photo="https://telegra.ph/file/206f9013802376b39ad03.jpg",
        quote=True
    )
        except MessageNotModified:
            pass    

    elif query.data=="TUTORIAL_CALLBACK":
        TELETIPS_TUTORIAL_BUTTONS = [
            [
                InlineKeyboardButton("⬅️ BACK", callback_data="START_CALLBACK"),
                InlineKeyboardButton('📃 4/4', callback_data="GROUP_CALLBACK"),
                InlineKeyboardButton('Next ➡️', callback_data="HELP_CALLBACK")
            ]
            ]
        reply_markup = InlineKeyboardMarkup(TELETIPS_TUTORIAL_BUTTONS)
        try:
            await query.edit_message_text(
                text = Translation.START.format(
                        mention = query.from_user.mention
                    ),
                reply_markup=reply_markup
            ),
        photo="https://telegra.ph/file/206f9013802376b39ad03.jpg",
        quote=True
    )
        except MessageNotModified:
            pass      
          
    elif query.data=="START_CALLBACK":
        TELETIPS_START_BUTTONS = [
            [
                InlineKeyboardButton("⬅️ BACK", callback_data="START_CALLBACK"),
                InlineKeyboardButton('📃 4/4', callback_data="GROUP_CALLBACK"),
            ]
        ]

        reply_markup = InlineKeyboardMarkup(TELETIPS_START_BUTTONS)
        try:
            await query.edit_message_text(
                text = Translation.START.format(
                        mention = query.from_user.mention
                    ),
                reply_markup=reply_markup
            ),
        photo="https://telegra.ph/file/206f9013802376b39ad03.jpg",
        quote=True
    )
        except MessageNotModified:
            pass    
        return


################################################################################################################################################################################################################################################
