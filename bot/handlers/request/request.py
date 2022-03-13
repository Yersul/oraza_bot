from telegram import Update
from telegram import (
    InlineKeyboardButton, InlineKeyboardMarkup
)

from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler
from bot.models import User
from bot_messages.models.message import Message
from bot_messages.models.request import Request


def command_request(update: Update, context: CallbackContext):
    message = Message.get_text_obj(type=8)
    context.bot.send_message(update.effective_user.id, message.message_kk)
    return 1


def command_request_updator(update: Update, context: CallbackContext):
    user = User.get_user(update, context)
    msg = update.message.text
    request = Request.objects.create(user=user, text=msg)
    if(request):
        context.bot.send_message(update.effective_user.id, '✅')
    else:
        context.bot.send_message(update.effective_user.id, 'Қате')
    return ConversationHandler.END
