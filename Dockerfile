FROM python:3.6-alpine

ADD bot.py /demo/bot.py
ADD config.yaml /demo/config.yaml

RUN pip install python-telegram-bot PyYAML

CMD ["python", "/demo/bot.py"]