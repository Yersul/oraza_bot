from telegram import Update
from telegram import (
    InlineKeyboardButton, InlineKeyboardMarkup
)

from bot.models import User
from telegram import Update
from telegram.ext import CallbackContext
from bot_messages.models.message import Message


def command_start(update: Update, context: CallbackContext):
    user = User.get_user(update, context)

    keyboard = [
        [InlineKeyboardButton("Қазақ тілінде", callback_data="kz")],
        [InlineKeyboardButton("На русском языке", callback_data="ru")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = Message.get_text(user, 1)
    update.message.reply_text(text, reply_markup=reply_markup)
