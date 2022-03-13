from telegram import Update
from telegram import (
    InlineKeyboardButton, InlineKeyboardMarkup
)

from telegram import Update
from telegram.ext import CallbackContext
from bot_messages.models.chadis import Chadis
from bot_messages.models.message import Message
import random


def command_chadis(update: Update, context: CallbackContext):
    chadis = Chadis.rand_obj()
    keyboard = [
        [InlineKeyboardButton("Тағы", callback_data="cmd_14")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.message.edit_text(
        chadis.text_kk, reply_markup=reply_markup)
