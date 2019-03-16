import os
import yaml
import random
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters)


with open('config.yaml') as file:
    config = yaml.safe_load(file)
    objects = config['objects']
    answers = config['answers']
    yes = config['yes_answers']
    no = config['no_answers']


def run_bot():
    api_token = os.environ['token']
    bot = Bot(token=api_token)
    
    updater = Updater(bot=bot)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler(command='start', 
        callback=start_button))
    dispatcher.add_handler(MessageHandler(callback=process, 
        filters=filters.Filters.photo))
    dispatcher.add_handler(CallbackQueryHandler(pattern='(yes|no)',
        callback=yes_no_button))
    updater.start_polling(poll_interval=5, timeout=5) 


def start_button(bot, update):
    if update.message.from_user.username is not None:
        user = update.message.from_user.username
    else:
        user = 'землянин'

    try:
        bot.send_message(chat_id=update.message.chat_id,
            text='Привет, {}! '.format(user) + \
                 'Я умею распознавать картинки. Попробуем?')
    except Exception as e:
        print('Exception: {}'.format(e))


def process(bot, update):
    try:
        percent = str(random.randint(50,100))
        object_name = objects[random.randint(0,len(objects)-1)]
        template = answers[random.randint(0,len(answers)-1)]
        template = template.replace('{{object}}', object_name)
        template = template.replace('{{percent}}', percent)

        y = InlineKeyboardButton("Да!", callback_data='yes')
        n = InlineKeyboardButton("Нет!", callback_data='no')
        buttons = InlineKeyboardMarkup([[y,n]])
        bot.send_message(chat_id=update.message.chat_id,
                         text=template,
                         reply_markup=buttons)
    except Exception as e:
        print('Exception: {}'.format(e))


def yes_no_button(bot, update):
    if update.callback_query.data == 'yes':
        answer = yes[random.randint(0,len(yes)-1)]
    else:
        answer = no[random.randint(0,len(no)-1)] 

    try:
        bot.send_message(chat_id=update.callback_query.from_user.id, 
            text=answer)
    except Exception as e:
        print('Exception: {}'.format(e))
    finally:
        bot.answer_callback_query(callback_query_id=update.callback_query.id)


if __name__ == '__main__':
    run_bot()
