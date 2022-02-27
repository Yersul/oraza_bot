from telegram import Update
from telegram import Update
from telegram.ext import CallbackContext
from bot_messages.models.schedule import Schedule


def command_schedule(update: Update, context: CallbackContext):
    print(update.callback_query.data.split('city_')[-1])
    city = int(update.callback_query.data.split('city_')[-1])
    schedule = Schedule.objects.filter(city=city).last()
    update.callback_query.message.reply_text(schedule.text)
    update.callback_query.message.reply_photo(schedule.image)
