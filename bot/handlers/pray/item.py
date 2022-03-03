from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram import Update
from telegram.ext import CallbackContext
from bot_messages.models.pray import Pray
from bot_messages.models.schedule import Schedule


def command_pray(update: Update, context: CallbackContext):
    print(update)
    pray_id = int(update.callback_query.data.split('pray_')[-1])
    pray = Pray.objects.filter(id=pray_id).last()
    if(pray == None):
        update.callback_query.message.reply_text("""Пока в разработке""")
        return
    
    
    keyboard = [
      [InlineKeyboardButton('артқа', callback_data="cmd_2")],
      [InlineKeyboardButton('Негізгі меню', callback_data="menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    messages = pray.text.all()
    for i in range(len(messages)):
        if(i == (len(messages)-1)):
            update.callback_query.message.reply_text(messages[i].text_kk, reply_markup=reply_markup)
        else:
            update.callback_query.message.reply_text(messages[i].text_kk)
