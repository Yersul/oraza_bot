import sys
import logging

import telegram.error
from telegram import Bot, Update
from telegram.ext import (
    Updater, Dispatcher, Filters,
    CommandHandler, MessageHandler,
    CallbackQueryHandler, ConversationHandler
)
from bot.handlers.chadis.random_chadis import command_chadis
from bot.handlers.faq.item_faq import command_category_faq_item
from bot.handlers.faq.list_category import command_faq_list
from bot.handlers.faq.list_category_faqs import command_category_faq_list

from bot.handlers.menu.menu import command_menu
from bot.handlers.plan.plan_item import command_ramazan_day_item
from bot.handlers.plan.plan_list import command_ramazan_day_list
from bot.handlers.plan.plan_menu import command_ramazan
from bot.handlers.pray.CategoryItem import command_category_pray
from bot.handlers.pray.CategoryItems import command_pray_items_list
from bot.handlers.pray.CategoryList import command_pray_categories_list
from bot.handlers.pray.item import command_pray
from bot.handlers.pray.list import command_pray_list
from bot.handlers.request.request import command_request, command_request_updator
from bot.handlers.schedule.cities import command_select_city, command_select_region_city
from bot.handlers.schedule.schedule import command_schedule
from bot.handlers.start.start import command_start

from oraza_bot.settings import TELEGRAM_TOKEN, DEBUG

from telegram import Update
from telegram.ext import CallbackContext


def cmd_stop(update: Update, context: CallbackContext):
    text = """Пока в разработке"""
    update.callback_query.message.reply_text(text)


def setup_dispatcher(callback):
    # start
    callback.add_handler(CommandHandler("start", command_start))

    # change language
    callback.add_handler(CallbackQueryHandler(command_menu, pattern='kz'))
    callback.add_handler(CallbackQueryHandler(command_menu, pattern='menu'))

    callback.add_handler(CallbackQueryHandler(
        command_chadis, pattern=f'cmd_14'))

    for i in range(10, 20):
        callback.add_handler(CallbackQueryHandler(
            cmd_stop, pattern=f'cmd_{i}'))

    callback.add_handler(CallbackQueryHandler(
        command_select_city, pattern='cmd_0'))

    callback.add_handler(CallbackQueryHandler(
        command_pray_categories_list, pattern='cmd_1'))

    callback.add_handler(CallbackQueryHandler(
        command_pray_list, pattern='cmd_2'))

    callback.add_handler(CallbackQueryHandler(
        command_faq_list, pattern='cmd_3'))

    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(
            command_request, pattern='cmd_4')],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, command_request_updator)],
        },
        fallbacks=[CommandHandler('start', command_menu)],
        per_message=False
    )
    callback.add_handler(conv_handler)

    callback.add_handler(CallbackQueryHandler(
        command_ramazan, pattern=f'cmd_6'))

    callback.add_handler(CallbackQueryHandler(
        command_select_region_city, pattern='select_region_city'))

    callback.add_handler(CallbackQueryHandler(
        command_schedule, pattern=f'city_'))

    callback.add_handler(CallbackQueryHandler(
        command_pray, pattern=f'pray_'))

    callback.add_handler(CallbackQueryHandler(
        command_category_pray, pattern=f'cat_pray_'))

    callback.add_handler(CallbackQueryHandler(
        command_pray_items_list, pattern=f'category_pray_'))

    callback.add_handler(CallbackQueryHandler(
        command_category_faq_list, pattern='cat_faq_'
    ))

    callback.add_handler(CallbackQueryHandler(
        command_category_faq_item, pattern='faq_'
    ))

    callback.add_handler(CallbackQueryHandler(
        command_ramazan_day_list, pattern='list_plan'
    ))

    callback.add_handler(CallbackQueryHandler(
        command_ramazan_day_item, pattern='plan_'
    ))

    callback.add_handler(CallbackQueryHandler(cmd_stop, pattern='ru'))

    return callback


def run_pooling():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp = setup_dispatcher(dp)

    bot_info = telegram.Bot(TELEGRAM_TOKEN).get_me()
    bot_link = f"https://t.me/" + bot_info["username"]

    print(f"'{bot_link}' started")
    updater.start_polling()
    updater.idle()


bot = Bot(TELEGRAM_TOKEN)
bot.set_webhook(max_connections=10000)

def process_telegram_event(update_json):
    update = Update.de_json(update_json, bot)
    dispatcher.process_update(update)

try:
    TELEGRAM_BOT_USERNAME = bot.get_me()["username"]
except telegram.error.Unauthorized:
    logging.error(f"Invalid TELEGRAM_TOKEN.")
    sys.exit(1)

n_workers = 1 if DEBUG else 4
dispatcher = setup_dispatcher(Dispatcher(bot, update_queue=None, workers=n_workers, use_context=True))