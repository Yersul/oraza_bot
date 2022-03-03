from telegram import Update
from telegram import (
    InlineKeyboardButton, InlineKeyboardMarkup
)

from bot.handlers.utils.btn_chanker import chunker
from telegram import Update
from telegram.ext import CallbackContext
from bot_messages.models.city import City
from bot_messages.models.message import Message
from bot_messages.models.pray import Pray


def command_pray_list(update: Update, context: CallbackContext):
    message = Message.get_text_obj(type=5)

    prays = Pray.objects.all()
    # print(prays[0].text.all())
    data = update.callback_query.data.split('cmd_2_')
    list_len = len(prays)
    try:
        offset = int(data[-1])
    except:
        offset = 0

    prays = prays[(offset*10):(offset*10 + 10)]
    keyboard = []
    for chunk in chunker(prays, message.inline_count):
        line = []
        for pray in list(chunk):
            btn = InlineKeyboardButton(
                str(pray.name_kk), callback_data=f"pray_{pray.id}")
            line.append(btn)
        keyboard.append(line)

    if((list_len - (offset*10)) > 10):
        keyboard.append([InlineKeyboardButton(
            'алға', callback_data=f"cmd_2_{offset+1}")])
    
    if((offset*10)>0):
        keyboard.append([InlineKeyboardButton(
            'кери', callback_data=f"cmd_2_{offset-1}")])

    keyboard.append([InlineKeyboardButton(
        'Негізгі меню', callback_data="menu")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.message.reply_text(
        message.message_kk, reply_markup=reply_markup)

