FROM python:3.6

RUN pip install python-telegram-bot PyYAML

ADD bot.py /demo/bot.py
ADD config.yaml /demo/config.yaml

WORKDIR /demo
CMD ["python", "bot.py"]