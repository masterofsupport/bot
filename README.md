# Пример Telegram-бота

Для запуска в docker выполнить:
* docker pull masterofsupport/bot
* docker run -e token=%токен-от-@botfather% masterofsupport/bot

Для запуска локально потребуется:
* установить python3.6
* установить зависимости: pip install python-telegram-bot PyYAML
* export token=%токен-от-@botfather%
* python3.6 bot.py