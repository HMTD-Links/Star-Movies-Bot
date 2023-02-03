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

MOVIE_BUTTONS = [
            [
                InlineKeyboardButton('📃 1/5', callback_data="pages"),
                InlineKeyboardButton('Next ➡️', callback_data="page 2")
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
    if query.data=="page 2":
        MOVIE_PAGE2_BUTTONS = [
            [
                InlineKeyboardButton("⬅️ BACK", callback_data="page 1"),
                InlineKeyboardButton('📃 2/5', callback_data="pages"),
                InlineKeyboardButton('Next ➡️', callback_data="page 3")
            ]
            ]
        reply_markup = InlineKeyboardMarkup(MOVIE_PAGE2_BUTTONS)
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

    elif query.data=="page 3":
        MOVIE_PAGE3_BUTTONS = [
            [
                InlineKeyboardButton("⬅️ BACK", callback_data="page 2"),
                InlineKeyboardButton('📃 3/5', callback_data="pages"),
                InlineKeyboardButton('Next ➡️', callback_data="page 4")
            ]
            ]
        reply_markup = InlineKeyboardMarkup(MOVIE_PAGE3_BUTTONS)
        try:
            await query.edit_message_text(
                text = MOVIES.ALIEN_COVENANT_PAGE3.format(
                        mention = query.from_user.mention
                    ),
                reply_markup=reply_markup
            ),
        photo="https://telegra.ph/file/206f9013802376b39ad03.jpg",
        quote=True
    )
        except MessageNotModified:
            pass    

    elif query.data=="page 4":
        MOVIE_PAGE4_BUTTONS = [
            [
                InlineKeyboardButton("⬅️ BACK", callback_data="page 3"),
                InlineKeyboardButton('📃 4/5', callback_data="pages"),
                InlineKeyboardButton('Next ➡️', callback_data="page 5")
            ]
            ]
        reply_markup = InlineKeyboardMarkup(MOVIE_PAGE4_BUTTONS)
        try:
            await query.edit_message_text(
                text = MOVIES.ALIEN_COVENANT_PAGE4.format(
                        mention = query.from_user.mention
                    ),
                reply_markup=reply_markup
            ),
        photo="https://telegra.ph/file/206f9013802376b39ad03.jpg",
        quote=True
    )
        except MessageNotModified:
            pass      
          
    elif query.data=="page 5":
        MOVIE_PAGE5_BUTTONS = [
            [
                InlineKeyboardButton("⬅️ BACK", callback_data="page 4"),
                InlineKeyboardButton('📃 5/5', callback_data="pages"),
            ]
        ]

        reply_markup = InlineKeyboardMarkup(MOVIE_PAGE5_BUTTONS)
        try:
            await query.edit_message_text(
                text = MOVIES.ALIEN_COVENANT_PAGE5.format(
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
