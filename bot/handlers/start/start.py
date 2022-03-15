from telegram import Update
from telegram import (
    InlineKeyboardButton, InlineKeyboardMarkup
)
from bot.handlers.utils.info import extract_user_data_from_update

from bot.models import User
from telegram import Update
from telegram.ext import CallbackContext
from bot_messages.models.message import Message


def command_start(update: Update, context: CallbackContext):
    data = extract_user_data_from_update(update)
    if(len(User.objects.filter(user_id=data['user_id'])) == 0):
        user = User.objects.create(
            user_id=data['user_id'],
            username=data['username'],
            first_name=data['first_name'],
            is_blocked_bot=data['is_blocked_bot'],
            language_code=data['language_code'],
        )
        user.save()
    user = User.get_user(update, context)
    keyboard = [
        [InlineKeyboardButton("Қазақ тілінде", callback_data="kz")],
        [InlineKeyboardButton("На русском языке", callback_data="ru")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = Message.get_text(user, 1)
    update.message.reply_text(text, reply_markup=reply_markup)
