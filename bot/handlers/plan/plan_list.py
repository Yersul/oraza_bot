from telegram import Update
from telegram import (
    InlineKeyboardButton, InlineKeyboardMarkup
)

from bot.handlers.utils.btn_chanker import chunker
from telegram import Update
from telegram.ext import CallbackContext
from bot_messages.models.faq import FAQ, FAQCategory
from bot_messages.models.message import Message
from bot_messages.models.action import Action
from bot_messages.models.plan import Plan


def command_ramazan_day_list(update: Update, context: CallbackContext):
    message = Message.get_text_obj(type=6)
    plans = Plan.objects.all()
    data = update.callback_query.data.split('list_plan_')
    list_len = len(plans)
    try:
        offset = int(data[-1])
    except:
        offset = 0

    plans = plans[(offset*10):(offset*10 + 10)]
    keyboard = []
    for chunk in chunker(plans, message.inline_count):
        line = []
        for plan in list(chunk):
            btn = InlineKeyboardButton(
                str(plan.name), callback_data=f"plan_{plan.id}")
            line.append(btn)
        keyboard.append(line)

    if((list_len - (offset*10)) > 10):
        keyboard.append([InlineKeyboardButton(
            'Алға', callback_data=f"list_plan_{offset+1}")])

    if((offset*10) > 0):
        keyboard.append([InlineKeyboardButton(
            'Артқа', callback_data=f"list_plan_{offset-1}")])
    elif(offset==0):
        keyboard.append([InlineKeyboardButton(
            'Артқа', callback_data=f"cmd_6")])

    keyboard.append([InlineKeyboardButton(
        'Негізгі меню', callback_data="menu")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.message.reply_text(
        message.message_kk, reply_markup=reply_markup)
