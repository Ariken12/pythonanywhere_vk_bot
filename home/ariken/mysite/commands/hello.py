from classcom import Command
from random import randint

messs = ["Хай", "Привет", "Даров, Как дела?", "Приветствую 8)"]


def hello(message, attachment, user_id):
    global randint, messs, len
    message = messs[randint(0, len(messs)-1)]
    if message == "Привет":
        message = "Вообще не оригинально, но привет"
    return message, ""


com_hello = Command()
com_hello.keys = []
com_hello.description = 'Поприветствую тебя'
com_hello.process = hello