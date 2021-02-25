from classcom import Command
from random import randint
import vkapi
import params

messs = ["Только не уписайся", "Зачем ты спрашиваешь меня? Подпишись на [реклама] уже))0)"]


def memes(message, attachment, user_id):
    global messs
    attachment = vkapi.get_random_wall_picture(-143031608, "wall")
    message = messs[randint(0, len(messs)-1)]
    return message, attachment


com_hello = Command()

com_hello.keys = ['мем', 'мем', 'мемес', 'meme']
com_hello.description = 'Мемчик'
com_hello.process = memes

