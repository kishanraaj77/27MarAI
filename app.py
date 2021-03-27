import telegram
import constants as keys
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import responses as R 



print("Bot started... ")

def start_command(update, context):
    update.message.reply_text('Type something')

def help_command(update, context):
    update.message.reply_text('get it from google')

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def handle_message(update,context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
  

def main():
    updater = Updater(token='1771363223:AAFE6y_hSnRy8BrRQn1WBWlSgJ8BQrzizgs', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(MessageHandler(Filters.text,echo))
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    updater.start_polling()
    updater.idle()

#main()
if __name__ == '__main__':
    main()
