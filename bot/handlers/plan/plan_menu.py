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


def command_ramazan(update: Update, context: CallbackContext):
    message = Message.get_text_obj(type=7)
    action_1 = Action.objects.get(command=6)
    action_2 = Action.objects.get(command=15)
    keyboard = [
        [InlineKeyboardButton(str(action_1.name_kk), callback_data="list_plan")],
        [InlineKeyboardButton(str(action_2.name_kk), url=action_2.link)],
        [InlineKeyboardButton('Негізгі меню', callback_data="menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.message.reply_text(
        message.message_kk, reply_markup=reply_markup)
