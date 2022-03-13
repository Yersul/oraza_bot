from telegram import Update
from telegram import (
    InlineKeyboardButton, InlineKeyboardMarkup
)

from telegram import Update
from telegram.ext import CallbackContext
from bot_messages.models.faq import FAQ
from bot_messages.models.message import Message


def command_category_faq_item(update: Update, context: CallbackContext):
    data = update.callback_query.data.split('_')
    id = int(data[-1])
    faq = FAQ.objects.get(id=id)

    keyboard = [
        [InlineKeyboardButton("Артқа", callback_data="cmd_3")],
        [InlineKeyboardButton("Негізгі меню", callback_data="menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.callback_query.message.reply_text(
        faq.body_kk, reply_markup=reply_markup)
