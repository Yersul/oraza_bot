from telegram import Update
from telegram import (
    InlineKeyboardButton, InlineKeyboardMarkup
)

from bot.handlers.utils.btn_chanker import chunker
from bot.models import User
from telegram import Update
from telegram.ext import CallbackContext
from bot_messages.models.message import Message


def command_menu(update: Update, context: CallbackContext):
    actions = Message.objects.filter(type=2).last().actions.all()
    keyboard = []

    user = User.get_user(update, context)
    user.selected_lang = 'kk'
    user.save()

    for chunk in chunker(actions, 2):
        line = []
        for action in list(chunk):
            if(action.command == 5):
                btn = InlineKeyboardButton(
                    str(action.name_kk), url=action.link)
            elif(action.command == 4):
                btn = InlineKeyboardButton(
                    str(action.name_kk), callback_data="cmd_4")
            else:
                btn = InlineKeyboardButton(
                    str(action.name_kk), callback_data=f"cmd_{action.command}")
            line.append(btn)
        keyboard.append(line)

    text = Message.get_text(type=2)
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.message.reply_text(text, reply_markup=reply_markup)
