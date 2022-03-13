from unicodedata import category
from telegram import Update
from telegram import (
    InlineKeyboardButton, InlineKeyboardMarkup
)

from bot.handlers.utils.btn_chanker import chunker
from telegram import Update
from telegram.ext import CallbackContext
from bot_messages.models.faq import FAQ, FAQCategory
from bot_messages.models.message import Message


def command_faq_list(update: Update, context: CallbackContext):
    message = Message.get_text_obj(type=7)

    categories = FAQCategory.objects.all()

    data = update.callback_query.data.split('cmd_3_')
    list_len = len(categories)
    try:
        offset = int(data[-1])
    except:
        offset = 0

    categories = categories[(offset*8):(offset*8 + 8)]
    keyboard = []
    for chunk in chunker(categories, message.inline_count):
        line = []
        for category in list(chunk):
            btn = InlineKeyboardButton(
                str(category.category_kk), callback_data=f"cat_faq_{category.id}")
            line.append(btn)
        keyboard.append(line)

    if((list_len - (offset*8)) > 8):
        keyboard.append([InlineKeyboardButton(
            'Алға', callback_data=f"cmd_3_{offset+1}")])

    if((offset*8) > 0):
        keyboard.append([InlineKeyboardButton(
            'Артқа', callback_data=f"cmd_3_{offset-1}")])

    # keyboard.append([InlineKeyboardButton(
    #     'Негізгі меню', callback_data="menu")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.message.reply_text(
        message.message_kk, reply_markup=reply_markup)
