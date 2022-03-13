from telegram import Update
from telegram import (
    InlineKeyboardButton, InlineKeyboardMarkup
)

from telegram import Update
from telegram.ext import CallbackContext
from bot.handlers.utils.btn_chanker import chunker
from bot_messages.models.message import Message


def command_pray_categories_list(update: Update, context: CallbackContext):
    message = Message.get_text_obj(type=4)

    if(message == None):
        update.callback_query.message.reply_text("""Пока в разработке""")
        return

    keyboard = []
    for chunk in chunker(message.actions.all(), message.inline_count):
        line = []
        for action in list(chunk):
            btn = InlineKeyboardButton(
                str(action.name_kk), callback_data=f"category_pray_{action.command}")
            line.append(btn)
        keyboard.append(line)
    
    keyboard.append([InlineKeyboardButton(
        'Артқа', callback_data="menu")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.message.reply_text(
        message.message_kk, reply_markup=reply_markup)
