from telegram import Update
from telegram import (
    InlineKeyboardButton, InlineKeyboardMarkup
)

from bot.handlers.utils.btn_chanker import chunker
from telegram import Update
from telegram.ext import CallbackContext
from bot_messages.models.city import City
from bot_messages.models.message import Message


def command_select_city(update: Update, context: CallbackContext):
    cities = City.objects.filter(type=1)
    message_obj = Message.get_text_obj(type=3)

    keyboard = []
    for chunk in chunker(cities, message_obj.inline_count):
        line = []
        for city in list(chunk):
            btn = InlineKeyboardButton(
                str(city.name_kk), callback_data=f"city_{city.id}")
            line.append(btn)
        keyboard.append(line)
    keyboard.append([InlineKeyboardButton(
        'Облыс аудандары', callback_data="select_region_city")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.message.reply_text(
        message_obj.message_kk, reply_markup=reply_markup)


def command_select_region_city(update: Update, context: CallbackContext):
    cities = City.objects.filter(type=0)
    message_obj = Message.get_text_obj(type=3)

    keyboard = []
    for chunk in chunker(cities, message_obj.inline_count):
        line = []
        for city in list(chunk):
            btn = InlineKeyboardButton(
                str(city.name_kk), callback_data=f"city_{city.id}")
            line.append(btn)
        keyboard.append(line)
    keyboard.append([InlineKeyboardButton(
        'Облыс аудандары', callback_data="select_region_city")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.message.reply_text(
        message_obj.message_kk, reply_markup=reply_markup)
