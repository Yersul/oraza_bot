from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram import Update
from telegram.ext import CallbackContext
from bot_messages.models.schedule import Schedule


def command_schedule(update: Update, context: CallbackContext):
    city = int(update.callback_query.data.split('city_')[-1])
    schedule = Schedule.objects.filter(city=city).last()
    if(schedule == None):
        update.callback_query.message.reply_text("""Пока в разработке""")
        return
    keyboard = [[InlineKeyboardButton('Негізгі меню', callback_data="menu")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.message.reply_text(schedule.text)
    update.callback_query.message.reply_photo(schedule.image, reply_markup=reply_markup)
