from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram import Update
from telegram.ext import CallbackContext
from bot.handlers.utils.btn_chanker import chunker
from bot_messages.models.action import Action
from bot_messages.models.pray import Pray
from bot_messages.models.schedule import Schedule
from bot_messages.models.message import Message


def command_pray_items_list(update: Update, context: CallbackContext):
    message = Message.get_text_obj(type=4)
    
    data = update.callback_query.data.split('_')
    
    action = Action.objects.get(command=data[-1])
    prays = Pray.objects.filter(pray_type=1, action=action)
    
    list_len = len(prays)
    try:
        offset = int(data[-1])
    except:
        offset = 0

    if(not len(data) == 4):
        offset = 0

    prays = prays[(offset*10):(offset*10 + 10)]
    keyboard = []
    for chunk in chunker(prays, message.inline_count):
        line = []
        for pray in list(chunk):
            btn = InlineKeyboardButton(
                str(pray.name_kk), callback_data=f"cat_pray_{pray.id}")
            line.append(btn)
        keyboard.append(line)

    if((list_len - (offset*10)) > 10):
        keyboard.append([InlineKeyboardButton(
            'Алға', callback_data=f"{update.callback_query.data}_{offset+1}")])

    if((offset*10) > 0):
        keyboard.append([InlineKeyboardButton(
            'Артқа', callback_data=f"{update.callback_query.data}_{offset-1}")])
    else:
        keyboard.append([InlineKeyboardButton(
            'Артқа', callback_data=f"cmd_1")])

    keyboard.append([InlineKeyboardButton(
        'Негізгі меню', callback_data="menu")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.message.reply_text(
        message.message_kk, reply_markup=reply_markup)
