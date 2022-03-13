from asyncio import constants
from telegram import Update
from telegram import (
    InlineKeyboardButton, InlineKeyboardMarkup
)

from bot.handlers.utils.btn_chanker import chunker
from telegram import Update
from telegram.ext import CallbackContext
from bot_messages.models.faq import FAQ, FAQCategory
from bot_messages.models.message import Message


def command_category_faq_list(update: Update, context: CallbackContext):
    data = update.callback_query.data.split('_')

    id = int(data[-1])
    offset = 0
    if(len(data) > 3):
        id = data[-2]
        try:
            offset = int(data[-1])
        except:
            pass

    cat = FAQCategory.objects.get(id=id)
    faqs = FAQ.objects.filter(category=cat)
    list_len = len(faqs)

    faqs = faqs[(offset*10):(offset*10 + 10)]
    keyboard = []
    for chunk in chunker(faqs, 1):
        line = []
        for faq in list(chunk):
            btn = InlineKeyboardButton(
                str(faq.question_kk), callback_data=f"faq_{faq.id}")
            line.append(btn)
        keyboard.append(line)

    if((list_len - (offset*8)) > 8):
        keyboard.append([InlineKeyboardButton(
            'Алға', callback_data=f"cat_faq_{offset+1}")])

    if((offset*8) > 0):
        keyboard.append([InlineKeyboardButton(
            'Артқа', callback_data=f"cat_faq_{offset-1}")])
    elif (offset == 0):
        keyboard.append([InlineKeyboardButton(
            'Артқа', callback_data=f"cmd_3")])
    keyboard.append([InlineKeyboardButton(
        'Негізгі меню', callback_data="menu")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.message.reply_text(
        cat.category_kk, reply_markup=reply_markup)
