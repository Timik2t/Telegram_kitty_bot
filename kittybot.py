import logging
import os

import requests
from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater

load_dotenv()

secret_token = os.getenv('BOT_TOKEN')

URL = 'https://api.thecatapi.com/v1/images/search'
DOGS_URL = 'https://api.thedogapi.com/v1/images/search'

ERROR_MESSAGE = 'Ошибка при запросе к основному API: {error}'


def get_new_image():
    try:
        response = requests.get(URL)
    except Exception as error:
        logging.error(ERROR_MESSAGE.format(error=error))
        new_url = DOGS_URL
        response = requests.get(new_url)

    response = response.json()
    random_cat = response[0].get('url')
    return random_cat


def get_new_dog_image():
    try:
        response = requests.get(DOGS_URL)
    except Exception as error:
        logging.error(ERROR_MESSAGE.format(error=error))
        new_url = URL
        response = requests.get(new_url)

    response = response.json()
    random_cat = response[0].get('url')
    return random_cat


RESPONSE_USERNAME = 'Картинку {image_name} запросил: {username}, {name}'


def new_cat(update, context):
    chat = update.effective_chat
    logging.info(RESPONSE_USERNAME.format(
        image_name='котека',
        username=update.message.chat.username,
        name=update.message.chat.first_name
    ))
    context.bot.send_photo(chat.id, get_new_image())


GREETING_MESSAGE = 'Привет, {name}. Посмотри какого котика я тебе нашел'


def wake_up(update, context):
    print(update)
    chat = update.effective_chat
    button = ReplyKeyboardMarkup(
        [['/newcat', '/newdog']],
        resize_keyboard=True
    )

    context.bot.send_message(
        chat_id=chat.id,
        text=GREETING_MESSAGE.format(name=update.message.chat.first_name),
        reply_markup=button
    )

    context.bot.send_photo(chat.id, get_new_image())


def main():
    updater = Updater(token=secret_token)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        handlers=[logging.FileHandler(__file__ + ".log"),
                  logging.StreamHandler()]
    )
    main()
