from classcom import Command
from random import randint
import vkapi


def searcher(message, attachment, user_id):
    global randint
    words = message.split()
    if len(words) > 0:
        message = vkapi.searcher_of_likes(words[1])
    return str(message), ""

com_searcher_of_likes = Command()

com_searcher_of_likes.keys = ['найди']
com_searcher_of_likes.description = 'В процессе разработки'
com_searcher_of_likes.process = searcher