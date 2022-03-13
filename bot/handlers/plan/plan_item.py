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


def command_ramazan_day_item(update: Update, context: CallbackContext):
    data = update.callback_query.data.split('plan_')
    plan = Plan.objects.get(id=int(data[-1]))
    keyboard = []
    keyboard.append([InlineKeyboardButton(
        'Артқа', callback_data=f"list_plan")])

    keyboard.append([InlineKeyboardButton(
        'Негізгі меню', callback_data="menu")])
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.callback_query.message.reply_text(plan.text)
    update.callback_query.message.reply_photo(
        plan.image, reply_markup=reply_markup)
