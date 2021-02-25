from classcom import Command
from random import randint
import vkapi
import params

messs = ["Справедливо", "Ты обратился по адресу"]

def memes(message, attachment, user_id):
    global messs
    attachment = vkapi.get_random_wall_picture(-109125388, 'wall')
    message = messs[randint(0, len(messs)-1)]
    return message, attachment


com_hello = Command()

com_hello.keys = ['Годнота', 'годнота']
com_hello.description = 'Годнота'
com_hello.process = memes

