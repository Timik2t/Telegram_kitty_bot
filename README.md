# Telegram_kitty_bot

```
@Tims_kitty_bot
```
Идея бота: он отправляет подписчикам фотки случайных котиков, для поднятия настроения. Все любят котиков, даже маркетологи.

Проект задеплоен на Heroku.
___________________________________________________
Программа написана на Python с использованием:
- requests (направление http-запроса на сервер),
- python-dotenv (загрузка и считывание переменных окружения из файла .env)
- python-telegram-bot (работа с Телеграм-ботом)

## Как работает программа:
Чат-бот Телеграм обращается к API, которое присылает рандомную картинку, при нажатии кнопки.  
Если API с котиками недоступен, бот пришлет фото песеля

## Как запустить программу:

1) Клонируйте репозитроий с программой:
```
git clone git@github.com:Timik2t/Telegram_kitty_bot.git
```
2) В созданной директории установите виртуальное окружение, активируйте его и установите необходимые зависимости:
```
python3 -m venv venv
```
```
. venv/bin/activate
```
```
pip install -r requirements.txt
```
3) Создайте чат-бота Телеграм
4) Создайте в директории файл .env и поместите туда необходимые токены в формате BOT_TOKEN = 'ххххххххххх',
5) Откройте файл kittybot.py и запустите код


